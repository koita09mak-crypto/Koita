import logging
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)
from config import TELEGRAM_TOKEN, OWNER_TELEGRAM_ID
from handlers.agent_handler import (
    show_agents_menu, agent_selected, handle_agent_message, agents_command
)
from handlers.conversations import (
    start, dashboard, assistant_start, assistant_message, stop,
    devis_start, devis_client, devis_description, devis_adresse,
    client_ajouter_start, client_nom, client_tel, client_email,
    client_type, client_marche, client_liste, client_chercher_start, client_chercher,
    facture_nouvelle_start, facture_client, facture_montant,
    factures_attente, facture_payer_start, facture_payer,
    planning_semaine, planning_mois, planning_ajouter_start,
    planning_date, planning_mission, planning_client,
    DEVIS_CLIENT, DEVIS_DESCRIPTION, DEVIS_ADRESSE,
    CLIENT_NOM, CLIENT_TEL, CLIENT_EMAIL, CLIENT_TYPE, CLIENT_MARCHE,
    FACTURE_CLIENT, FACTURE_MONTANT, FACTURE_DEVIS_ID,
    PLANNING_DATE, PLANNING_MISSION, PLANNING_CLIENT,
    SEARCH_QUERY,
)

logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)


def owner_only(handler):
    async def wrapper(update: Update, ctx):
        user_id = str(update.effective_user.id)
        if OWNER_TELEGRAM_ID and user_id != OWNER_TELEGRAM_ID:
            await update.effective_message.reply_text("Accès non autorisé.")
            return
        return await handler(update, ctx)
    return wrapper


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    conv_devis = ConversationHandler(
        entry_points=[CallbackQueryHandler(devis_start, pattern="^devis_nouveau$")],
        states={
            DEVIS_CLIENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, devis_client)],
            DEVIS_DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, devis_description)],
            DEVIS_ADRESSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, devis_adresse)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    conv_client = ConversationHandler(
        entry_points=[CallbackQueryHandler(client_ajouter_start, pattern="^client_ajouter$")],
        states={
            CLIENT_NOM: [MessageHandler(filters.TEXT & ~filters.COMMAND, client_nom)],
            CLIENT_TEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, client_tel)],
            CLIENT_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, client_email)],
            CLIENT_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, client_type)],
            CLIENT_MARCHE: [MessageHandler(filters.TEXT & ~filters.COMMAND, client_marche)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    conv_search = ConversationHandler(
        entry_points=[CallbackQueryHandler(client_chercher_start, pattern="^client_chercher$")],
        states={
            SEARCH_QUERY: [MessageHandler(filters.TEXT & ~filters.COMMAND, client_chercher)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    conv_facture = ConversationHandler(
        entry_points=[CallbackQueryHandler(facture_nouvelle_start, pattern="^facture_nouvelle$")],
        states={
            FACTURE_CLIENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, facture_client)],
            FACTURE_MONTANT: [MessageHandler(filters.TEXT & ~filters.COMMAND, facture_montant)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    conv_payer = ConversationHandler(
        entry_points=[CallbackQueryHandler(facture_payer_start, pattern="^facture_payer$")],
        states={
            FACTURE_DEVIS_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, facture_payer)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    conv_planning = ConversationHandler(
        entry_points=[CallbackQueryHandler(planning_ajouter_start, pattern="^planning_ajouter$")],
        states={
            PLANNING_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, planning_date)],
            PLANNING_MISSION: [MessageHandler(filters.TEXT & ~filters.COMMAND, planning_mission)],
            PLANNING_CLIENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, planning_client)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("agents", agents_command))
    app.add_handler(conv_devis)
    app.add_handler(conv_client)
    app.add_handler(conv_search)
    app.add_handler(conv_facture)
    app.add_handler(conv_payer)
    app.add_handler(conv_planning)

    app.add_handler(CallbackQueryHandler(start, pattern="^menu_principal$"))
    app.add_handler(CallbackQueryHandler(show_agents_menu, pattern="^menu_agents$"))
    app.add_handler(CallbackQueryHandler(agent_selected, pattern="^agent:"))
    app.add_handler(CallbackQueryHandler(dashboard, pattern="^menu_dashboard$"))
    app.add_handler(CallbackQueryHandler(assistant_start, pattern="^menu_assistant$"))
    app.add_handler(CallbackQueryHandler(lambda u, c: show_menu_devis(u, c), pattern="^menu_devis$"))
    app.add_handler(CallbackQueryHandler(lambda u, c: show_menu_clients(u, c), pattern="^menu_clients$"))
    app.add_handler(CallbackQueryHandler(lambda u, c: show_menu_factures(u, c), pattern="^menu_factures$"))
    app.add_handler(CallbackQueryHandler(lambda u, c: show_menu_planning(u, c), pattern="^menu_planning$"))
    app.add_handler(CallbackQueryHandler(client_liste, pattern="^client_liste$"))
    app.add_handler(CallbackQueryHandler(factures_attente, pattern="^facture_attente$"))
    app.add_handler(CallbackQueryHandler(planning_semaine, pattern="^planning_semaine$"))
    app.add_handler(CallbackQueryHandler(planning_mois, pattern="^planning_mois$"))

    async def smart_message_router(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        handled = await handle_agent_message(update, ctx)
        if not handled:
            await assistant_message(update, ctx)

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, smart_message_router))

    logging.info("AK Réseaux & Bâtiment — Bot démarré")
    app.run_polling()


async def show_menu_devis(update, ctx):
    from handlers.menus import MENU_DEVIS, show_menu
    await show_menu(update, "📋 *Mes Devis*\n\nQue veux-tu faire ?", MENU_DEVIS)


async def show_menu_clients(update, ctx):
    from handlers.menus import MENU_CLIENTS, show_menu
    await show_menu(update, "👥 *Mes Clients*\n\nQue veux-tu faire ?", MENU_CLIENTS)


async def show_menu_factures(update, ctx):
    from handlers.menus import MENU_FACTURES, show_menu
    await show_menu(update, "💰 *Mes Factures*\n\nQue veux-tu faire ?", MENU_FACTURES)


async def show_menu_planning(update, ctx):
    from handlers.menus import MENU_PLANNING, show_menu
    await show_menu(update, "📅 *Mon Planning*\n\nQue veux-tu faire ?", MENU_PLANNING)


if __name__ == "__main__":
    main()
