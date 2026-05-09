from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from handlers.menus import MENU_PRINCIPAL, MENU_DEVIS, MENU_CLIENTS, MENU_FACTURES, MENU_PLANNING, show_menu
from agents.assistant import generate_devis, chat
from data.storage import (
    add_client, get_clients, find_client, save_devis,
    save_facture, get_factures, marquer_facture_payee,
    add_planning, get_planning, get_stats
)
from datetime import datetime

# États de conversation
(
    DEVIS_CLIENT, DEVIS_DESCRIPTION, DEVIS_ADRESSE,
    CLIENT_NOM, CLIENT_TEL, CLIENT_EMAIL, CLIENT_TYPE, CLIENT_MARCHE,
    FACTURE_CLIENT, FACTURE_MONTANT, FACTURE_DEVIS_ID,
    PLANNING_DATE, PLANNING_MISSION, PLANNING_CLIENT,
    SEARCH_QUERY,
) = range(15)


# ─── DÉMARRAGE ───────────────────────────────────────────────────────────────

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    from config import BUSINESS
    nom = update.effective_user.first_name
    texte = (
        f"Bonjour {nom} 👋\n\n"
        f"*{BUSINESS['nom']}* — Assistant IA\n"
        f"Gérant : {BUSINESS['proprietaire']}\n\n"
        f"Que veux-tu faire ?"
    )
    await show_menu(update, texte, MENU_PRINCIPAL)


# ─── DASHBOARD ───────────────────────────────────────────────────────────────

async def dashboard(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    from agents.assistant import analyser_situation
    stats = get_stats()
    texte = (
        f"📊 *Tableau de bord — AK Réseaux & Bâtiment*\n\n"
        f"👥 Clients : {stats['nb_clients']} ({stats['nb_prospects']} prospects)\n"
        f"📋 Devis émis : {stats['nb_devis']}\n"
        f"💰 CA encaissé : {stats['ca_encaisse']}€\n"
        f"⏳ CA en attente : {stats['ca_en_attente']}€\n"
        f"📅 Missions planifiées : {stats['nb_missions_planifiees']}\n\n"
        f"_Analyse en cours..._"
    )
    if update.callback_query:
        await update.callback_query.edit_message_text(texte, parse_mode="Markdown")
        analyse = analyser_situation(stats)
        await update.callback_query.message.reply_text(f"🤖 *Analyse :*\n\n{analyse}", parse_mode="Markdown", reply_markup=MENU_PRINCIPAL)
    else:
        await update.message.reply_text(texte, parse_mode="Markdown")


# ─── DEVIS ───────────────────────────────────────────────────────────────────

async def devis_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text(
        "📋 *Nouveau devis*\n\nNom du client ou de l'entreprise ?",
        parse_mode="Markdown"
    )
    return DEVIS_CLIENT


async def devis_client(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["devis_client"] = update.message.text
    await update.message.reply_text("Description des travaux à réaliser ? (Sois précis : type de travaux, surface, contexte)")
    return DEVIS_DESCRIPTION


async def devis_description(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["devis_description"] = update.message.text
    await update.message.reply_text("Adresse du chantier ? (ou tape 'passer' pour ignorer)")
    return DEVIS_ADRESSE


async def devis_adresse(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    adresse = update.message.text
    if adresse.lower() == "passer":
        adresse = ""
    ctx.user_data["devis_adresse"] = adresse

    await update.message.reply_text("⏳ Génération du devis en cours...")

    devis_texte = generate_devis(
        client_nom=ctx.user_data["devis_client"],
        description=ctx.user_data["devis_description"],
        adresse=adresse,
    )

    save_devis(
        client_id="",
        client_nom=ctx.user_data["devis_client"],
        description_travaux=ctx.user_data["devis_description"],
        postes=[],
        total_ht=0,
    )

    await update.message.reply_text(devis_texte, parse_mode="Markdown", reply_markup=MENU_DEVIS)
    return ConversationHandler.END


# ─── CLIENTS ─────────────────────────────────────────────────────────────────

async def client_liste(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    clients = get_clients()
    if not clients:
        texte = "Aucun client enregistré pour l'instant."
    else:
        lignes = [f"*{c['nom']}* — {c['statut']} ({c['marche']})" for c in clients[-10:]]
        texte = "👥 *Mes clients*\n\n" + "\n".join(lignes)
    await update.callback_query.edit_message_text(texte, parse_mode="Markdown", reply_markup=MENU_CLIENTS)


async def client_ajouter_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text(
        "👤 *Nouveau client*\n\nNom complet ou raison sociale ?",
        parse_mode="Markdown"
    )
    return CLIENT_NOM


async def client_nom(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["client_nom"] = update.message.text
    await update.message.reply_text("Numéro de téléphone ? (ou 'passer')")
    return CLIENT_TEL


async def client_tel(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["client_tel"] = update.message.text if update.message.text.lower() != "passer" else ""
    await update.message.reply_text("Email ? (ou 'passer')")
    return CLIENT_EMAIL


async def client_email(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["client_email"] = update.message.text if update.message.text.lower() != "passer" else ""
    await update.message.reply_text("Type de client ?\n1 - Particulier\n2 - Artisan/PME\n3 - Promoteur/Constructeur\n4 - ONG/Collectivité")
    return CLIENT_TYPE


async def client_type(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    types = {"1": "particulier", "2": "artisan/pme", "3": "promoteur", "4": "ong/collectivité"}
    ctx.user_data["client_type"] = types.get(update.message.text, "particulier")
    await update.message.reply_text("Marché ?\n1 - France\n2 - Afrique de l'Ouest")
    return CLIENT_MARCHE


async def client_marche(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    marche = "Afrique de l'Ouest" if update.message.text == "2" else "France"
    client = add_client(
        nom=ctx.user_data["client_nom"],
        telephone=ctx.user_data.get("client_tel", ""),
        email=ctx.user_data.get("client_email", ""),
        type_client=ctx.user_data.get("client_type", "particulier"),
        marche=marche,
    )
    await update.message.reply_text(
        f"✅ Client ajouté !\n\n*{client['nom']}* (ID: {client['id']})\nMarché : {marche}",
        parse_mode="Markdown",
        reply_markup=MENU_CLIENTS,
    )
    return ConversationHandler.END


async def client_chercher_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text("🔍 Nom, téléphone ou email du client ?")
    return SEARCH_QUERY


async def client_chercher(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    resultats = find_client(update.message.text)
    if not resultats:
        texte = "Aucun client trouvé."
    else:
        lignes = [
            f"*{c['nom']}* — {c['telephone']} — {c['statut']} ({c['marche']})"
            for c in resultats
        ]
        texte = "🔍 *Résultats*\n\n" + "\n".join(lignes)
    await update.message.reply_text(texte, parse_mode="Markdown", reply_markup=MENU_CLIENTS)
    return ConversationHandler.END


# ─── FACTURES ────────────────────────────────────────────────────────────────

async def factures_attente(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    factures = get_factures(statut="en attente")
    if not factures:
        texte = "Aucune facture en attente de paiement. 🎉"
    else:
        lignes = [
            f"*{f['numero']}* — {f['client_nom']} — {f['montant_ht']}€ HT\nID : `{f['id']}`"
            for f in factures
        ]
        texte = "⏳ *Factures en attente*\n\n" + "\n\n".join(lignes)
    await update.callback_query.edit_message_text(texte, parse_mode="Markdown", reply_markup=MENU_FACTURES)


async def facture_nouvelle_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text(
        "💰 *Nouvelle facture*\n\nNom du client ?",
        parse_mode="Markdown"
    )
    return FACTURE_CLIENT


async def facture_client(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["facture_client"] = update.message.text
    await update.message.reply_text("Montant HT en euros ? (chiffre seul, ex: 850)")
    return FACTURE_MONTANT


async def facture_montant(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    try:
        montant = float(update.message.text.replace(",", ".").replace("€", "").strip())
    except ValueError:
        await update.message.reply_text("Montant invalide. Tape un chiffre, ex: 850")
        return FACTURE_MONTANT

    facture = save_facture(
        devis_id="",
        client_nom=ctx.user_data["facture_client"],
        montant_ht=montant,
    )
    await update.message.reply_text(
        f"✅ *Facture créée*\n\nNuméro : {facture['numero']}\nClient : {facture['client_nom']}\nMontant HT : {facture['montant_ht']}€\nStatut : En attente\nID : `{facture['id']}`",
        parse_mode="Markdown",
        reply_markup=MENU_FACTURES,
    )
    return ConversationHandler.END


async def facture_payer_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text(
        "✅ ID de la facture à marquer payée ? (l'ID est affiché dans la liste des factures)"
    )
    return FACTURE_DEVIS_ID


async def facture_payer(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    facture_id = update.message.text.strip().upper()
    marquer_facture_payee(facture_id)
    await update.message.reply_text(f"✅ Facture {facture_id} marquée comme payée.", reply_markup=MENU_FACTURES)
    return ConversationHandler.END


# ─── PLANNING ────────────────────────────────────────────────────────────────

async def planning_semaine(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    events = get_planning(jours=7)
    if not events:
        texte = "Aucune mission planifiée cette semaine."
    else:
        lignes = [
            f"📅 *{e['date'][:10]}* — {e['mission']}\n   Client : {e['client_nom'] or 'N/A'} | {e['type']}"
            for e in events
        ]
        texte = "📅 *Planning — 7 prochains jours*\n\n" + "\n\n".join(lignes)
    await update.callback_query.edit_message_text(texte, parse_mode="Markdown", reply_markup=MENU_PLANNING)


async def planning_mois(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    events = get_planning(jours=30)
    if not events:
        texte = "Aucune mission planifiée ce mois."
    else:
        lignes = [
            f"📅 *{e['date'][:10]}* — {e['mission']}\n   Client : {e['client_nom'] or 'N/A'}"
            for e in events
        ]
        texte = "📅 *Planning — 30 jours*\n\n" + "\n\n".join(lignes)
    await update.callback_query.edit_message_text(texte, parse_mode="Markdown", reply_markup=MENU_PLANNING)


async def planning_ajouter_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text(
        "📅 *Nouvelle mission*\n\nDate de la mission ? (format : 2026-05-15)",
        parse_mode="Markdown"
    )
    return PLANNING_DATE


async def planning_date(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["planning_date"] = update.message.text
    await update.message.reply_text("Description de la mission ?")
    return PLANNING_MISSION


async def planning_mission(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["planning_mission"] = update.message.text
    await update.message.reply_text("Client associé ? (ou 'passer')")
    return PLANNING_CLIENT


async def planning_client(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    client_nom = update.message.text if update.message.text.lower() != "passer" else ""
    event = add_planning(
        date=ctx.user_data["planning_date"],
        mission=ctx.user_data["planning_mission"],
        client_nom=client_nom,
    )
    await update.message.reply_text(
        f"✅ Mission ajoutée !\n📅 {event['date'][:10]} — {event['mission']}",
        reply_markup=MENU_PLANNING,
    )
    return ConversationHandler.END


# ─── ASSISTANT IA ─────────────────────────────────────────────────────────────

async def assistant_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["conversation"] = []
    await update.callback_query.edit_message_text(
        "🤖 *Assistant IA — AK Réseaux & Bâtiment*\n\n"
        "Pose-moi n'importe quelle question : devis, client, stratégie, BTP, AOF...\n\n"
        "Tape /stop pour revenir au menu.",
        parse_mode="Markdown"
    )


async def assistant_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if "conversation" not in ctx.user_data:
        ctx.user_data["conversation"] = []

    await update.message.reply_chat_action("typing")
    reponse = chat(ctx.user_data["conversation"], update.message.text)
    await update.message.reply_text(reponse, parse_mode="Markdown")


async def stop(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    await start(update, ctx)
    return ConversationHandler.END
