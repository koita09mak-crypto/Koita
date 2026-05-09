import google.generativeai as genai
from config import GEMINI_API_KEY, BUSINESS

genai.configure(api_key=GEMINI_API_KEY)
_model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = f"""Tu es l'assistant IA personnel d'Adama Koita, gérant de {BUSINESS['nom']}.

TU CONNAIS SON ENTREPRISE :
- Activités : {', '.join(BUSINESS['activites'])}
- Marchés : France et Afrique de l'Ouest
- Statut : micro-entreprise en démarrage
- Code NAF : 4321A (installation électrique, réseaux, systèmes techniques)
- TVA : non applicable (article 293B du CGI)

TU PEUX FAIRE :
1. Générer des devis professionnels complets
2. Gérer clients et prospects (ajouter, chercher, mettre à jour)
3. Créer et suivre des factures
4. Gérer l'agenda et les missions chantier
5. Répondre aux questions techniques BTP
6. Conseiller sur l'acquisition client et la stratégie commerciale

TARIFS DE RÉFÉRENCE :
{chr(10).join(f"- {k}: {v}" for k, v in BUSINESS['tarifs_journaliers'].items())}

STYLE :
- Direct, professionnel, efficace
- Pas de remplissage inutile
- Toujours proposer une action concrète ensuite
- Si tu génères un devis ou une facture, formate-le clairement

IMPORTANT :
- Adama est demandeur d'emploi en train de lancer son activité
- Budget serré, chaque action doit être rentable ou utile
- Double marché France / AOF = penser aux deux contextes
"""


def _ask(prompt: str) -> str:
    response = _model.generate_content(SYSTEM_PROMPT + "\n\n" + prompt)
    return response.text


def chat(messages: list, user_message: str) -> str:
    historique = []
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        historique.append({"role": role, "parts": [msg["content"]]})

    session = _model.start_chat(history=historique)
    response = session.send_message(SYSTEM_PROMPT + "\n\n" + user_message if not historique else user_message)

    messages.append({"role": "user", "content": user_message})
    messages.append({"role": "assistant", "content": response.text})
    return response.text


def generate_devis(client_nom: str, description: str, adresse: str = "") -> str:
    prompt = f"""Génère un devis professionnel complet pour AK Réseaux & Bâtiment.

Client : {client_nom}
Adresse chantier : {adresse or 'À préciser'}
Travaux demandés : {description}

Le devis doit inclure :
1. En-tête avec les coordonnées d'AK Réseaux & Bâtiment
2. Informations client
3. Description détaillée des travaux (décomposée en postes)
4. Prix unitaires et totaux HT réalistes selon les tarifs du marché BTP français
5. Conditions : acompte 30%, solde à réception, validité 30 jours
6. Mention TVA non applicable article 293B
7. Mention assurance RC Pro

Formate le devis de façon claire et professionnelle."""
    return _ask(prompt)


def analyser_situation(stats: dict) -> str:
    prompt = f"""Analyse rapide de la situation d'AK Réseaux & Bâtiment :

Données actuelles :
- Clients total : {stats['nb_clients']} ({stats['nb_prospects']} prospects)
- Devis émis : {stats['nb_devis']}
- Factures : {stats['nb_factures']}
- CA encaissé : {stats['ca_encaisse']}€
- CA en attente : {stats['ca_en_attente']}€
- Missions planifiées : {stats['nb_missions_planifiees']}

Donne un diagnostic en 3 points et une action prioritaire immédiate.
Sois direct et concret, pas de généralités."""
    return _ask(prompt)
