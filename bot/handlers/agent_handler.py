from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from agents.engine import run_agent, reset_agent_session, get_agents_menu_text
from agents.profiles import AGENTS, AGENT_KEYS

TYPE_EMOJIS = {"Admin": "📋", "Terrain": "🔧", "Commercial": "💼", "Stratégie": "🧠"}

TYPES_ORDER = ["Admin", "Terrain", "Commercial", "Stratégie"]


def build_agents_keyboard():
    rows = []
    types = {}
    for key, data in AGENTS.items():
        t = data["type"]
        if t not in types:
            types[t] = []
        types[t].append((key, data["emoji"], data["nom"]))

    for type_ in TYPES_ORDER:
        if type_ not in types:
            continue
        agents = types[type_]
        row = [
            InlineKeyboardButton(
                f"{emoji} {nom.replace('Agent ', '')}",
                callback_data=f"agent:{key}"
            )
            for key, emoji, nom in agents
        ]
        for i in range(0, len(row), 2):
            rows.append(row[i:i+2])

    rows.append([InlineKeyboardButton("⬅️ Menu principal", callback_data="menu_principal")])
    return InlineKeyboardMarkup(rows)


async def show_agents_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    texte = get_agents_menu_text()
    keyboard = build_agents_keyboard()
    if update.callback_query:
        await update.callback_query.edit_message_text(texte, parse_mode="Markdown", reply_markup=keyboard)
    else:
        await update.message.reply_text(texte, parse_mode="Markdown", reply_markup=keyboard)


async def agent_selected(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    agent_key = query.data.split(":")[1]
    agent = AGENTS.get(agent_key)
    if not agent:
        await query.answer("Agent introuvable")
        return

    ctx.user_data["agent_actif"] = agent_key
    ctx.user_data["conversation"] = []

    texte = (
        f"{agent['emoji']} *{agent['nom']}*\n"
        f"_{agent['description']}_\n\n"
        f"Je suis prêt. Dis-moi ce que tu veux.\n\n"
        f"Tape /agents pour changer d'agent ou /stop pour revenir au menu."
    )
    await query.edit_message_text(texte, parse_mode="Markdown")


async def handle_agent_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> bool:
    agent_key = ctx.user_data.get("agent_actif")
    if not agent_key:
        return False

    user_id = str(update.effective_user.id)
    await update.message.reply_chat_action("typing")

    reponse = run_agent(agent_key, update.message.text, user_id)
    agent = AGENTS[agent_key]

    await update.message.reply_text(
        f"{agent['emoji']} *{agent['nom']}*\n\n{reponse}",
        parse_mode="Markdown"
    )
    return True


async def agents_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.pop("agent_actif", None)
    await show_agents_menu(update, ctx)
