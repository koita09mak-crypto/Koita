import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OWNER_TELEGRAM_ID = os.getenv("OWNER_TELEGRAM_ID")  # Ton ID Telegram perso

BUSINESS = {
    "nom": "AK Réseaux & Bâtiment",
    "proprietaire": "Adama Koita",
    "siret": os.getenv("SIRET", "En cours d'immatriculation"),
    "email": os.getenv("BUSINESS_EMAIL", "contact@ak-reseaux-batiment.fr"),
    "telephone": os.getenv("BUSINESS_PHONE", ""),
    "adresse": os.getenv("BUSINESS_ADDRESS", ""),
    "assurance_rc": os.getenv("ASSURANCE_RC", "RC Pro — en cours de souscription"),
    "tva": "TVA non applicable — Article 293B du CGI",
    "marches": ["France", "Afrique de l'Ouest"],
    "activites": [
        "Câblage réseaux et télécoms",
        "Installation systèmes d'alarme et contrôle d'accès",
        "Installation électrique courant faible",
        "Assistance technique BTP",
        "Services numériques pour artisans BTP",
    ],
    "tarifs_journaliers": {
        "cablage_reseaux": "200-280€/jour",
        "alarme_securite": "250-350€/jour",
        "assistance_technique": "180-250€/jour",
        "electricite_courant_fort": "250-400€/jour",
        "service_numerique": "50-150€/prestation",
    },
}

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "business_data.json")
