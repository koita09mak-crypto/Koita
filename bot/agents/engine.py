"""
Moteur d'exécution des agents — combine les 4P + la mémoire + Gemini API.
"""

import google.generativeai as genai
from config import GEMINI_API_KEY
from agents.profiles import build_prompt, get_agent, list_agents, AGENTS

genai.configure(api_key=GEMINI_API_KEY)
_model = genai.GenerativeModel("gemini-1.5-flash")

_sessions: dict[str, list] = {}


def run_agent(agent_key: str, user_input: str, user_id: str = "default") -> str:
    agent = get_agent(agent_key)
    if not agent:
        return f"Agent '{agent_key}' introuvable."

    session_key = f"{user_id}:{agent_key}"
    if session_key not in _sessions:
        _sessions[session_key] = []

    history = _sessions[session_key]

    full_prompt = build_prompt(agent, user_input)

    if history:
        session = _model.start_chat(history=history)
        response = session.send_message(user_input)
    else:
        response = _model.generate_content(full_prompt)

    reply = response.text

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [reply]})

    if len(history) > 20:
        _sessions[session_key] = history[-20:]

    return reply


def reset_agent_session(agent_key: str, user_id: str = "default"):
    session_key = f"{user_id}:{agent_key}"
    _sessions.pop(session_key, None)


def get_agents_menu_text() -> str:
    types = {}
    for key, nom, emoji, type_, desc in list_agents():
        if type_ not in types:
            types[type_] = []
        types[type_].append(f"{emoji} *{nom}*\n   _{desc}_")

    lignes = ["🤖 *Tes 11 Agents IA — AK Réseaux & Bâtiment*\n"]
    type_emojis = {"Admin": "📋", "Terrain": "🔧", "Commercial": "💼", "Stratégie": "🧠"}
    for type_, agents in types.items():
        lignes.append(f"\n{type_emojis.get(type_, '')} *{type_}*")
        lignes.extend(agents)
    return "\n".join(lignes)
