import anthropic
from config import ANTHROPIC_API_KEY, BUSINESS

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

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


def chat(messages: list, user_message: str) -> str:
    messages.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    assistant_reply = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply


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

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


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

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text
