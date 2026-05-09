"""
AK Réseaux & Bâtiment — Assistant IA
Version Replit (fichier unique)
Déploiement : coller ce fichier dans Replit et configurer les secrets
"""

import os
import json
import uuid
import logging
from datetime import datetime, timedelta

import google.generativeai as genai
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ConversationHandler, ContextTypes, filters,
)

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
OWNER_ID = os.environ.get("OWNER_ID", "")

genai.configure(api_key=GEMINI_API_KEY)
_gemini = genai.GenerativeModel("gemini-1.5-flash")

logging.basicConfig(format="%(asctime)s — %(levelname)s — %(message)s", level=logging.INFO)

DATA_FILE = "data.json"

BUSINESS = {
    "nom": "AK Réseaux & Bâtiment",
    "gerant": "Adama Koita",
    "activites": ["Câblage réseaux et télécoms", "Systèmes d'alarme et contrôle d'accès",
                  "Installation électrique courant faible", "Assistance technique BTP",
                  "Services numériques pour artisans BTP"],
    "tarifs": {"câblage réseau": "200-280€/j", "alarme/sécurité": "250-350€/j",
               "assistance technique": "180-250€/j", "électricité": "250-400€/j"},
    "marches": "France + Afrique de l'Ouest",
    "tva": "TVA non applicable — Article 293B du CGI",
    "phase": "Phase 1 — Stabilisation (0-6 mois)",
    "budget_depart": "200€",
}

# ─── MÉMOIRE COMMUNE ──────────────────────────────────────────────────────────

MEMOIRE = f"""
CONTEXTE ENTREPRISE (mémoire permanente) :
- Gérant : {BUSINESS['gerant']}
- Entreprise : {BUSINESS['nom']}
- Statut : micro-entrepreneur en démarrage, ex-demandeur d'emploi
- Formation : Objectif La Solive (BTP)
- Expérience : électricité, télécoms, câblage, réseaux, bâtiment neuf, génie civil
- Marchés : {BUSINESS['marches']}
- Phase : {BUSINESS['phase']} | Budget : {BUSINESS['budget_depart']}
- Code NAF : 4321A | {BUSINESS['tva']}
- Activités : {', '.join(BUSINESS['activites'])}
- Tarifs : {' | '.join(f"{k}: {v}" for k, v in BUSINESS['tarifs'].items())}
- Objectif 6 mois : premières missions + profil digital + réseau AOF cartographié
- Objectif 36 mois : 4 000-8 000€/mois sur 3 axes
"""

# ─── 11 AGENTS 4P ─────────────────────────────────────────────────────────────

AGENTS = {
    "devis": {
        "nom": "Agent Devis", "emoji": "📋", "type": "Admin",
        "desc": "Génère des devis professionnels complets",
        "personnage": "Expert chiffrage BTP 15 ans d'expérience, précis, ne sous-facture jamais.",
        "processus": "1. Analyse travaux → 2. Décompose en postes → 3. Prix marché → 4. Formate devis complet.",
        "preference": "Décomposer en postes, acompte 30%, validité 30j, TVA 293B, mentions légales toujours.",
        "produit": "Devis complet prêt à envoyer avec en-tête, postes, totaux HT, conditions, mentions légales.",
    },
    "factures": {
        "nom": "Agent Facturation", "emoji": "💰", "type": "Admin",
        "desc": "Crée factures, suit paiements, alerte impayés",
        "personnage": "Assistant financier rigoureux spécialisé micro-entreprises BTP.",
        "processus": "1. Crée factures conformes → 2. Calcule échéances → 3. Surveille impayés → 4. Propose relances.",
        "preference": "Délai 30j, relance J+3 (cordiale), J+15 (ferme), pénalités 3x taux légal.",
        "produit": "Factures conformes, tableau paiements, messages de relance prêts à envoyer.",
    },
    "planning": {
        "nom": "Agent Planning", "emoji": "📅", "type": "Admin",
        "desc": "Agenda chantier, missions, deadlines administratives",
        "personnage": "Conducteur de travaux organisé qui anticipe conflits et deadlines admin.",
        "processus": "1. Enregistre missions → 2. Vérifie conflits → 3. Rappels → 4. Optimise enchaînements.",
        "preference": "30min de marge entre missions, deadlines admin prioritaires sur chantiers.",
        "produit": "Planning structuré, rappels, liste deadlines du mois.",
    },
    "electricite": {
        "nom": "Agent Électricité & Réseaux", "emoji": "⚡", "type": "Terrain",
        "desc": "Expert technique élec, câblage, réseaux courants faibles et forts",
        "personnage": "Technicien électricien confirmé, maîtrise NF C 15-100, DTU, VDI, fibre.",
        "processus": "1. Identifie réglementation → 2. Solution technique → 3. Matériel → 4. Points vigilance.",
        "preference": "Vérifier conformité avant solution, marques accessibles (Legrand, Schneider), habilitations.",
        "produit": "Réponse technique claire, liste matériel, référence réglementaire, checklist mise en service.",
    },
    "surete": {
        "nom": "Agent Sûreté & Alarme", "emoji": "🔒", "type": "Terrain",
        "desc": "Expert alarme, contrôle d'accès, vidéosurveillance",
        "personnage": "Technicien sûreté électronique, normes EN 50131, NF A2P, RGPD.",
        "processus": "1. Évalue niveau protection → 2. Architecture système → 3. Matériel → 4. Réglementation.",
        "preference": "Systèmes certifiés NF A2P, RGPD vidéo obligatoire, Ajax/Somfy/Dahua recommandés.",
        "produit": "Préconisation système, liste matériel, points légaux, arguments commerciaux client.",
    },
    "normes": {
        "nom": "Agent Normes & Conformité", "emoji": "📐", "type": "Terrain",
        "desc": "Réglementation BTP France — normes, DTU, certifications",
        "personnage": "Expert réglementation BTP, NF, DTU, RE2020, Eurocodes, certifications pro.",
        "processus": "1. Identifie réglementation exacte → 2. Obligatoire vs recommandé → 3. Conséquences → 4. Certifications.",
        "preference": "Citer références exactes, distinguer neuf/rénovation, risques assurantiels.",
        "produit": "Réponse réglementaire avec références, distinction obligatoire/recommandé, impact assurance.",
    },
    "prospection": {
        "nom": "Agent Prospection France", "emoji": "🎯", "type": "Commercial",
        "desc": "Trouve des clients en France — méthodes et scripts pour débutant",
        "personnage": "Commercial BTP expérimenté, sait trouver les premiers clients sans budget pub.",
        "processus": "1. Canal adapté à la phase → 2. Méthode concrète → 3. Script → 4. Mesure résultats.",
        "preference": "Budget zéro priorité, sous-traitance en premier, Google My Business avant site web.",
        "produit": "Plan prospection, scripts prêts, 5 actions cette semaine, indicateurs résultats.",
    },
    "aof": {
        "nom": "Agent Marché AOF", "emoji": "🌍", "type": "Commercial",
        "desc": "Opportunités et stratégie commerciale Afrique de l'Ouest",
        "personnage": "Expert marchés BTP AOF (Sénégal, Côte d'Ivoire, Mali, Guinée, Burkina).",
        "processus": "1. Opportunités réseau actuel → 2. Acteurs pertinents → 3. Approche commerciale → 4. Potentiel financier.",
        "preference": "Réseau existant avant prospection froide, diaspora investisseurs prioritaire, services à distance d'abord.",
        "produit": "Cartographie opportunités, offre calibrée AOF, tarification marché, points vigilance.",
    },
    "crm": {
        "nom": "Agent CRM & Relances", "emoji": "🤝", "type": "Commercial",
        "desc": "Suit les prospects, relances naturelles, fidélisation clients",
        "personnage": "Commercial relationnel, relances sans paraître insistant, génération de recommandations.",
        "processus": "1. Classe contacts (chaud/tiède/froid) → 2. Calendrier relance → 3. Messages → 4. Recommandations.",
        "preference": "Relance utile > insistante, 48h après devis, 7j si pas de réponse, noter raison refus.",
        "produit": "Messages relance prêts (WhatsApp/SMS), calendrier suivi, script recommandation.",
    },
    "analyse": {
        "nom": "Agent Analyse & KPIs", "emoji": "📊", "type": "Stratégie",
        "desc": "Tableau de bord, indicateurs clés, lecture performance réelle",
        "personnage": "Analyste business TPE/artisans BTP, traduit données simples en insights actionnables.",
        "processus": "1. Collecte données → 2. Calcule KPIs → 3. Compare objectifs → 4. Action corrective.",
        "preference": "Max 5 KPIs en Phase 1, toujours comparer mois précédent, une action prioritaire par analyse.",
        "produit": "Tableau de bord mensuel, diagnostic 3 points, une action prioritaire, tendance.",
    },
    "strategie": {
        "nom": "Agent Décisions & Croissance", "emoji": "🧠", "type": "Stratégie",
        "desc": "Conseille sur grandes décisions, anticipe angles morts, planifie croissance",
        "personnage": "Conseiller stratégique senior, combine vision entrepreneur BTP et double marché France/AOF.",
        "processus": "1. Analyse contexte exact → 2. Angles morts → 3. Compare options → 4. Recommandation.",
        "preference": "Challenger avant valider, budget contraint = options réalistes, cohérence plan 3 phases.",
        "produit": "Analyse décision structurée, angles morts, recommandation justifiée, critères succès.",
    },
}

TYPE_ORDER = ["Admin", "Terrain", "Commercial", "Stratégie"]
TYPE_EMOJI = {"Admin": "📋", "Terrain": "🔧", "Commercial": "💼", "Stratégie": "🧠"}

# ─── STOCKAGE ─────────────────────────────────────────────────────────────────

def _load():
    if not os.path.exists(DATA_FILE):
        return {"clients": [], "devis": [], "factures": [], "planning": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def _uid(): return str(uuid.uuid4())[:8].upper()

def add_client(nom, tel="", email="", type_c="particulier", marche="France"):
    data = _load()
    c = {"id": _uid(), "nom": nom, "telephone": tel, "email": email,
         "type": type_c, "marche": marche, "statut": "prospect",
         "date": datetime.now().isoformat()}
    data["clients"].append(c)
    _save(data)
    return c

def get_clients(): return _load()["clients"]
def find_client(q): return [c for c in _load()["clients"] if q.lower() in c["nom"].lower()]

def save_devis(client_nom, description):
    data = _load()
    num = f"DEV-{datetime.now().strftime('%Y%m')}-{len(data['devis'])+1:03d}"
    d = {"id": _uid(), "numero": num, "client": client_nom, "description": description,
         "date": datetime.now().isoformat(), "statut": "envoyé"}
    data["devis"].append(d)
    _save(data)
    return d

def save_facture(client_nom, montant):
    data = _load()
    num = f"FAC-{datetime.now().strftime('%Y%m')}-{len(data['factures'])+1:03d}"
    f = {"id": _uid(), "numero": num, "client": client_nom, "montant": montant,
         "date": datetime.now().isoformat(), "statut": "en attente"}
    data["factures"].append(f)
    _save(data)
    return f

def get_factures(statut=None):
    f = _load()["factures"]
    return [x for x in f if x["statut"] == statut] if statut else f

def payer_facture(fid):
    data = _load()
    for f in data["factures"]:
        if f["id"] == fid:
            f["statut"] = "payée"
            f["date_paiement"] = datetime.now().isoformat()
    _save(data)

def add_planning(date, mission, client=""):
    data = _load()
    e = {"id": _uid(), "date": date, "mission": mission, "client": client,
         "statut": "planifié", "date_ajout": datetime.now().isoformat()}
    data["planning"].append(e)
    _save(data)
    return e

def get_planning(jours=7):
    now = datetime.now()
    limite = now + timedelta(days=jours)
    events = []
    for e in _load()["planning"]:
        try:
            if now <= datetime.fromisoformat(e["date"]) <= limite:
                events.append(e)
        except: pass
    return sorted(events, key=lambda x: x["date"])

def get_stats():
    data = _load()
    return {
        "clients": len(data["clients"]),
        "prospects": len([c for c in data["clients"] if c["statut"] == "prospect"]),
        "devis": len(data["devis"]),
        "factures": len(data["factures"]),
        "ca_encaisse": sum(f["montant"] for f in data["factures"] if f["statut"] == "payée"),
        "ca_attente": sum(f["montant"] for f in data["factures"] if f["statut"] == "en attente"),
        "missions": len([e for e in data["planning"] if e["statut"] == "planifié"]),
    }

# ─── IA ───────────────────────────────────────────────────────────────────────

def ask_agent(agent_key, user_input):
    a = AGENTS[agent_key]
    prompt = f"""{MEMOIRE}

=== PERSONNAGE ===
{a['personnage']}

=== PROCESSUS ===
{a['processus']}

=== PRÉFÉRENCE ===
{a['preference']}

=== PRODUIT ATTENDU ===
{a['produit']}

=== DEMANDE ===
{user_input}"""
    return _gemini.generate_content(prompt).text

def ask_general(messages, user_input):
    prompt = MEMOIRE + "\n\nTu es l'assistant IA d'AK Réseaux & Bâtiment. Réponds de façon directe, professionnelle et adaptée au contexte BTP France/AOF.\n\n" + user_input
    if messages:
        session = _gemini.start_chat(history=messages)
        r = session.send_message(user_input)
    else:
        r = _gemini.generate_content(prompt)
    messages.append({"role": "user", "parts": [user_input]})
    messages.append({"role": "model", "parts": [r.text]})
    return r.text

# ─── MENUS ────────────────────────────────────────────────────────────────────

def menu_principal():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📋 Devis", callback_data="m_devis"),
         InlineKeyboardButton("👥 Clients", callback_data="m_clients")],
        [InlineKeyboardButton("💰 Factures", callback_data="m_factures"),
         InlineKeyboardButton("📅 Planning", callback_data="m_planning")],
        [InlineKeyboardButton("📊 Dashboard", callback_data="m_dashboard"),
         InlineKeyboardButton("🤖 Assistant", callback_data="m_assistant")],
        [InlineKeyboardButton("🧠 Mes 11 Agents IA", callback_data="m_agents")],
    ])

def menu_agents():
    rows = []
    types = {}
    for k, a in AGENTS.items():
        types.setdefault(a["type"], []).append((k, a["emoji"], a["nom"].replace("Agent ", "")))
    for t in TYPE_ORDER:
        if t not in types: continue
        row = [InlineKeyboardButton(f"{e} {n}", callback_data=f"agent:{k}") for k, e, n in types[t]]
        for i in range(0, len(row), 2): rows.append(row[i:i+2])
    rows.append([InlineKeyboardButton("⬅️ Menu", callback_data="m_home")])
    return InlineKeyboardMarkup(rows)

def menu_back(target="m_home"):
    return InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Menu principal", callback_data=target)]])

# ─── HANDLERS ─────────────────────────────────────────────────────────────────

DEVIS_CLIENT, DEVIS_DESC, DEVIS_ADRESSE = 1, 2, 3
CLI_NOM, CLI_TEL, CLI_EMAIL, CLI_TYPE, CLI_MARCHE = 4, 5, 6, 7, 8
FAC_CLI, FAC_MONTANT = 9, 10
FAC_PAYER_ID = 11
PLAN_DATE, PLAN_MISSION, PLAN_CLIENT = 12, 13, 14
SEARCH = 15


async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    if OWNER_ID and uid != OWNER_ID:
        await update.effective_message.reply_text("Accès non autorisé.")
        return
    nom = update.effective_user.first_name
    await update.effective_message.reply_text(
        f"Bonjour {nom} 👋\n\n*AK Réseaux & Bâtiment* — Assistant IA\nGérant : Adama Koita\n\nQue veux-tu faire ?",
        reply_markup=menu_principal(), parse_mode="Markdown"
    )

async def cmd_stop(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    await cmd_start(update, ctx)
    return ConversationHandler.END

async def cb_home(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.pop("agent_actif", None)
    nom = update.effective_user.first_name
    await update.callback_query.edit_message_text(
        f"Bonjour {nom} 👋\n\n*AK Réseaux & Bâtiment* — Assistant IA\n\nQue veux-tu faire ?",
        reply_markup=menu_principal(), parse_mode="Markdown"
    )

async def cb_dashboard(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    s = get_stats()
    texte = (f"📊 *Tableau de bord*\n\n"
             f"👥 Clients : {s['clients']} ({s['prospects']} prospects)\n"
             f"📋 Devis : {s['devis']}\n💰 CA encaissé : {s['ca_encaisse']}€\n"
             f"⏳ CA en attente : {s['ca_attente']}€\n📅 Missions : {s['missions']}")
    await update.callback_query.edit_message_text(texte, parse_mode="Markdown", reply_markup=menu_back())

async def cb_agents_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lignes = ["🧠 *Tes 11 Agents IA*\n"]
    types = {}
    for k, a in AGENTS.items():
        types.setdefault(a["type"], []).append(f"{a['emoji']} *{a['nom']}* — _{a['desc']}_")
    for t in TYPE_ORDER:
        if t not in types: continue
        lignes.append(f"\n{TYPE_EMOJI[t]} *{t}*")
        lignes.extend(types[t])
    await update.callback_query.edit_message_text("\n".join(lignes), parse_mode="Markdown", reply_markup=menu_agents())

async def cb_agent_selected(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    key = update.callback_query.data.split(":")[1]
    a = AGENTS[key]
    ctx.user_data["agent_actif"] = key
    ctx.user_data["conv"] = []
    await update.callback_query.edit_message_text(
        f"{a['emoji']} *{a['nom']}*\n_{a['desc']}_\n\nJe suis prêt. Dis-moi ce que tu veux.\n\n/stop pour revenir au menu.",
        parse_mode="Markdown"
    )

async def cb_assistant(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["agent_actif"] = None
    ctx.user_data["conv"] = []
    await update.callback_query.edit_message_text(
        "🤖 *Assistant IA*\n\nPose-moi n'importe quelle question — BTP, stratégie, AOF, devis...\n\n/stop pour revenir au menu.",
        parse_mode="Markdown"
    )

async def on_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    if OWNER_ID and uid != OWNER_ID:
        return
    await update.message.reply_chat_action("typing")
    agent_key = ctx.user_data.get("agent_actif")
    conv = ctx.user_data.setdefault("conv", [])

    if agent_key:
        a = AGENTS[agent_key]
        reponse = ask_agent(agent_key, update.message.text)
        await update.message.reply_text(f"{a['emoji']} *{a['nom']}*\n\n{reponse}", parse_mode="Markdown")
    else:
        reponse = ask_general(conv, update.message.text)
        await update.message.reply_text(reponse, parse_mode="Markdown")

# ─── CONVERSATIONS ─────────────────────────────────────────────────────────────

async def devis_start(update, ctx):
    await update.callback_query.edit_message_text("📋 *Nouveau devis*\n\nNom du client ?", parse_mode="Markdown")
    return DEVIS_CLIENT

async def devis_client_h(update, ctx):
    ctx.user_data["dv_client"] = update.message.text
    await update.message.reply_text("Description des travaux ? (précise : type, surface, contexte)")
    return DEVIS_DESC

async def devis_desc_h(update, ctx):
    ctx.user_data["dv_desc"] = update.message.text
    await update.message.reply_text("Adresse du chantier ? (ou 'passer')")
    return DEVIS_ADRESSE

async def devis_adresse_h(update, ctx):
    adresse = "" if update.message.text.lower() == "passer" else update.message.text
    await update.message.reply_text("⏳ Génération du devis...")
    prompt = (f"Génère un devis professionnel complet pour AK Réseaux & Bâtiment.\n"
              f"Client : {ctx.user_data['dv_client']}\nAdresse : {adresse or 'À préciser'}\n"
              f"Travaux : {ctx.user_data['dv_desc']}\n"
              f"Inclure : en-tête, postes détaillés, prix HT marché BTP, conditions (acompte 30%, validité 30j), TVA 293B, assurance RC Pro.")
    devis_txt = ask_agent("devis", prompt)
    save_devis(ctx.user_data["dv_client"], ctx.user_data["dv_desc"])
    await update.message.reply_text(devis_txt, parse_mode="Markdown", reply_markup=menu_back())
    return ConversationHandler.END

async def cli_start(update, ctx):
    await update.callback_query.edit_message_text("👤 *Nouveau client*\n\nNom complet ou raison sociale ?", parse_mode="Markdown")
    return CLI_NOM

async def cli_nom_h(update, ctx):
    ctx.user_data["cl_nom"] = update.message.text
    await update.message.reply_text("Téléphone ? (ou 'passer')")
    return CLI_TEL

async def cli_tel_h(update, ctx):
    ctx.user_data["cl_tel"] = "" if update.message.text.lower() == "passer" else update.message.text
    await update.message.reply_text("Email ? (ou 'passer')")
    return CLI_EMAIL

async def cli_email_h(update, ctx):
    ctx.user_data["cl_email"] = "" if update.message.text.lower() == "passer" else update.message.text
    await update.message.reply_text("Type ?\n1 - Particulier\n2 - Artisan/PME\n3 - Promoteur\n4 - ONG/Collectivité")
    return CLI_TYPE

async def cli_type_h(update, ctx):
    t = {"1": "particulier", "2": "artisan/pme", "3": "promoteur", "4": "ong"}.get(update.message.text, "particulier")
    ctx.user_data["cl_type"] = t
    await update.message.reply_text("Marché ?\n1 - France\n2 - Afrique de l'Ouest")
    return CLI_MARCHE

async def cli_marche_h(update, ctx):
    m = "Afrique de l'Ouest" if update.message.text == "2" else "France"
    c = add_client(ctx.user_data["cl_nom"], ctx.user_data.get("cl_tel"), ctx.user_data.get("cl_email"), ctx.user_data.get("cl_type"), m)
    await update.message.reply_text(f"✅ *{c['nom']}* ajouté — {m} (ID: {c['id']})", parse_mode="Markdown", reply_markup=menu_back())
    return ConversationHandler.END

async def cli_liste(update, ctx):
    clients = get_clients()
    t = "👥 *Clients*\n\n" + "\n".join(f"*{c['nom']}* — {c['statut']} ({c['marche']})" for c in clients[-10:]) if clients else "Aucun client."
    await update.callback_query.edit_message_text(t, parse_mode="Markdown", reply_markup=menu_back())

async def cli_search_start(update, ctx):
    await update.callback_query.edit_message_text("🔍 Nom ou téléphone du client ?")
    return SEARCH

async def cli_search_h(update, ctx):
    r = find_client(update.message.text)
    t = "🔍 *Résultats*\n\n" + "\n".join(f"*{c['nom']}* — {c['telephone']} ({c['marche']})" for c in r) if r else "Aucun résultat."
    await update.message.reply_text(t, parse_mode="Markdown", reply_markup=menu_back())
    return ConversationHandler.END

async def fac_start(update, ctx):
    await update.callback_query.edit_message_text("💰 *Nouvelle facture*\n\nNom du client ?", parse_mode="Markdown")
    return FAC_CLI

async def fac_cli_h(update, ctx):
    ctx.user_data["fc_cli"] = update.message.text
    await update.message.reply_text("Montant HT en € ? (ex: 850)")
    return FAC_MONTANT

async def fac_montant_h(update, ctx):
    try:
        m = float(update.message.text.replace(",", ".").replace("€", "").strip())
    except:
        await update.message.reply_text("Montant invalide. Tape un chiffre (ex: 850)")
        return FAC_MONTANT
    f = save_facture(ctx.user_data["fc_cli"], m)
    await update.message.reply_text(f"✅ *{f['numero']}*\nClient : {f['client']}\nMontant : {f['montant']}€ HT\nID : `{f['id']}`", parse_mode="Markdown", reply_markup=menu_back())
    return ConversationHandler.END

async def fac_attente(update, ctx):
    fl = get_factures("en attente")
    t = "⏳ *Factures en attente*\n\n" + "\n\n".join(f"*{f['numero']}* — {f['client']} — {f['montant']}€\nID : `{f['id']}`" for f in fl) if fl else "Aucune facture en attente. 🎉"
    await update.callback_query.edit_message_text(t, parse_mode="Markdown", reply_markup=menu_back())

async def fac_payer_start(update, ctx):
    await update.callback_query.edit_message_text("✅ ID de la facture à marquer payée ?")
    return FAC_PAYER_ID

async def fac_payer_h(update, ctx):
    payer_facture(update.message.text.strip().upper())
    await update.message.reply_text(f"✅ Facture {update.message.text.strip().upper()} marquée payée.", reply_markup=menu_back())
    return ConversationHandler.END

async def plan_semaine(update, ctx):
    ev = get_planning(7)
    t = "📅 *7 prochains jours*\n\n" + "\n\n".join(f"📅 *{e['date'][:10]}* — {e['mission']}\nClient : {e['client'] or 'N/A'}" for e in ev) if ev else "Aucune mission cette semaine."
    await update.callback_query.edit_message_text(t, parse_mode="Markdown", reply_markup=menu_back())

async def plan_mois(update, ctx):
    ev = get_planning(30)
    t = "📅 *30 prochains jours*\n\n" + "\n\n".join(f"📅 *{e['date'][:10]}* — {e['mission']}" for e in ev) if ev else "Aucune mission ce mois."
    await update.callback_query.edit_message_text(t, parse_mode="Markdown", reply_markup=menu_back())

async def plan_start(update, ctx):
    await update.callback_query.edit_message_text("📅 *Nouvelle mission*\n\nDate ? (format : 2026-05-20)", parse_mode="Markdown")
    return PLAN_DATE

async def plan_date_h(update, ctx):
    ctx.user_data["pl_date"] = update.message.text
    await update.message.reply_text("Description de la mission ?")
    return PLAN_MISSION

async def plan_mission_h(update, ctx):
    ctx.user_data["pl_mission"] = update.message.text
    await update.message.reply_text("Client associé ? (ou 'passer')")
    return PLAN_CLIENT

async def plan_client_h(update, ctx):
    cli = "" if update.message.text.lower() == "passer" else update.message.text
    e = add_planning(ctx.user_data["pl_date"], ctx.user_data["pl_mission"], cli)
    await update.message.reply_text(f"✅ Mission ajoutée\n📅 {e['date'][:10]} — {e['mission']}", reply_markup=menu_back())
    return ConversationHandler.END

# Menus intermédiaires
async def cb_devis_menu(update, ctx):
    await update.callback_query.edit_message_text("📋 *Devis*", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Nouveau devis", callback_data="dv_new")],
        [InlineKeyboardButton("⬅️ Menu", callback_data="m_home")]]))

async def cb_clients_menu(update, ctx):
    await update.callback_query.edit_message_text("👥 *Clients*", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Ajouter", callback_data="cl_add"), InlineKeyboardButton("🔍 Chercher", callback_data="cl_search")],
        [InlineKeyboardButton("📋 Tous", callback_data="cl_list")],
        [InlineKeyboardButton("⬅️ Menu", callback_data="m_home")]]))

async def cb_factures_menu(update, ctx):
    await update.callback_query.edit_message_text("💰 *Factures*", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Nouvelle", callback_data="fc_new"), InlineKeyboardButton("⏳ En attente", callback_data="fc_wait")],
        [InlineKeyboardButton("✅ Marquer payée", callback_data="fc_pay")],
        [InlineKeyboardButton("⬅️ Menu", callback_data="m_home")]]))

async def cb_planning_menu(update, ctx):
    await update.callback_query.edit_message_text("📅 *Planning*", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Ajouter mission", callback_data="pl_new")],
        [InlineKeyboardButton("📅 7 jours", callback_data="pl_week"), InlineKeyboardButton("📅 30 jours", callback_data="pl_month")],
        [InlineKeyboardButton("⬅️ Menu", callback_data="m_home")]]))

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    conv_devis = ConversationHandler(
        entry_points=[CallbackQueryHandler(devis_start, pattern="^dv_new$")],
        states={DEVIS_CLIENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, devis_client_h)],
                DEVIS_DESC: [MessageHandler(filters.TEXT & ~filters.COMMAND, devis_desc_h)],
                DEVIS_ADRESSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, devis_adresse_h)]},
        fallbacks=[CommandHandler("stop", cmd_stop)],
    )
    conv_cli = ConversationHandler(
        entry_points=[CallbackQueryHandler(cli_start, pattern="^cl_add$")],
        states={CLI_NOM: [MessageHandler(filters.TEXT & ~filters.COMMAND, cli_nom_h)],
                CLI_TEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, cli_tel_h)],
                CLI_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, cli_email_h)],
                CLI_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, cli_type_h)],
                CLI_MARCHE: [MessageHandler(filters.TEXT & ~filters.COMMAND, cli_marche_h)]},
        fallbacks=[CommandHandler("stop", cmd_stop)],
    )
    conv_search = ConversationHandler(
        entry_points=[CallbackQueryHandler(cli_search_start, pattern="^cl_search$")],
        states={SEARCH: [MessageHandler(filters.TEXT & ~filters.COMMAND, cli_search_h)]},
        fallbacks=[CommandHandler("stop", cmd_stop)],
    )
    conv_fac = ConversationHandler(
        entry_points=[CallbackQueryHandler(fac_start, pattern="^fc_new$")],
        states={FAC_CLI: [MessageHandler(filters.TEXT & ~filters.COMMAND, fac_cli_h)],
                FAC_MONTANT: [MessageHandler(filters.TEXT & ~filters.COMMAND, fac_montant_h)]},
        fallbacks=[CommandHandler("stop", cmd_stop)],
    )
    conv_pay = ConversationHandler(
        entry_points=[CallbackQueryHandler(fac_payer_start, pattern="^fc_pay$")],
        states={FAC_PAYER_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, fac_payer_h)]},
        fallbacks=[CommandHandler("stop", cmd_stop)],
    )
    conv_plan = ConversationHandler(
        entry_points=[CallbackQueryHandler(plan_start, pattern="^pl_new$")],
        states={PLAN_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, plan_date_h)],
                PLAN_MISSION: [MessageHandler(filters.TEXT & ~filters.COMMAND, plan_mission_h)],
                PLAN_CLIENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, plan_client_h)]},
        fallbacks=[CommandHandler("stop", cmd_stop)],
    )

    for conv in [conv_devis, conv_cli, conv_search, conv_fac, conv_pay, conv_plan]:
        app.add_handler(conv)

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("stop", cmd_stop))
    app.add_handler(CallbackQueryHandler(cb_home, pattern="^m_home$"))
    app.add_handler(CallbackQueryHandler(cmd_start, pattern="^m_home$"))
    app.add_handler(CallbackQueryHandler(cb_dashboard, pattern="^m_dashboard$"))
    app.add_handler(CallbackQueryHandler(cb_assistant, pattern="^m_assistant$"))
    app.add_handler(CallbackQueryHandler(cb_agents_menu, pattern="^m_agents$"))
    app.add_handler(CallbackQueryHandler(cb_agent_selected, pattern="^agent:"))
    app.add_handler(CallbackQueryHandler(cb_devis_menu, pattern="^m_devis$"))
    app.add_handler(CallbackQueryHandler(cb_clients_menu, pattern="^m_clients$"))
    app.add_handler(CallbackQueryHandler(cb_factures_menu, pattern="^m_factures$"))
    app.add_handler(CallbackQueryHandler(cb_planning_menu, pattern="^m_planning$"))
    app.add_handler(CallbackQueryHandler(cli_liste, pattern="^cl_list$"))
    app.add_handler(CallbackQueryHandler(fac_attente, pattern="^fc_wait$"))
    app.add_handler(CallbackQueryHandler(plan_semaine, pattern="^pl_week$"))
    app.add_handler(CallbackQueryHandler(plan_mois, pattern="^pl_month$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))

    logging.info("AK Réseaux & Bâtiment — Bot démarré ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
