from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

MENU_PRINCIPAL = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📋 Devis", callback_data="menu_devis"),
        InlineKeyboardButton("👥 Clients", callback_data="menu_clients"),
    ],
    [
        InlineKeyboardButton("💰 Factures", callback_data="menu_factures"),
        InlineKeyboardButton("📅 Planning", callback_data="menu_planning"),
    ],
    [
        InlineKeyboardButton("📊 Tableau de bord", callback_data="menu_dashboard"),
        InlineKeyboardButton("🤖 Assistant IA", callback_data="menu_assistant"),
    ],
])

MENU_DEVIS = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Nouveau devis", callback_data="devis_nouveau")],
    [InlineKeyboardButton("📋 Voir mes devis", callback_data="devis_liste")],
    [InlineKeyboardButton("⬅️ Menu principal", callback_data="menu_principal")],
])

MENU_CLIENTS = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Ajouter client", callback_data="client_ajouter")],
    [InlineKeyboardButton("🔍 Chercher client", callback_data="client_chercher")],
    [InlineKeyboardButton("📋 Tous mes clients", callback_data="client_liste")],
    [InlineKeyboardButton("⬅️ Menu principal", callback_data="menu_principal")],
])

MENU_FACTURES = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Nouvelle facture", callback_data="facture_nouvelle")],
    [InlineKeyboardButton("⏳ En attente de paiement", callback_data="facture_attente")],
    [InlineKeyboardButton("✅ Marquer comme payée", callback_data="facture_payer")],
    [InlineKeyboardButton("⬅️ Menu principal", callback_data="menu_principal")],
])

MENU_PLANNING = InlineKeyboardMarkup([
    [InlineKeyboardButton("➕ Ajouter une mission", callback_data="planning_ajouter")],
    [InlineKeyboardButton("📅 Semaine en cours", callback_data="planning_semaine")],
    [InlineKeyboardButton("📅 30 prochains jours", callback_data="planning_mois")],
    [InlineKeyboardButton("⬅️ Menu principal", callback_data="menu_principal")],
])


async def show_menu(update: Update, text: str, keyboard: InlineKeyboardMarkup):
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=keyboard, parse_mode="Markdown")
    else:
        await update.message.reply_text(text, reply_markup=keyboard, parse_mode="Markdown")
