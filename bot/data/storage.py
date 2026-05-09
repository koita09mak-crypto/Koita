import json
import os
import uuid
from datetime import datetime
from config import DATA_FILE


def _load():
    if not os.path.exists(DATA_FILE):
        return {"clients": [], "devis": [], "factures": [], "planning": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _id():
    return str(uuid.uuid4())[:8].upper()


# --- CLIENTS ---

def add_client(nom, telephone="", email="", adresse="", type_client="particulier", marche="France", notes=""):
    data = _load()
    client = {
        "id": _id(),
        "nom": nom,
        "telephone": telephone,
        "email": email,
        "adresse": adresse,
        "type": type_client,
        "marche": marche,
        "notes": notes,
        "statut": "prospect",
        "date_ajout": datetime.now().isoformat(),
        "historique": [],
    }
    data["clients"].append(client)
    _save(data)
    return client


def get_clients(statut=None, marche=None):
    data = _load()
    clients = data["clients"]
    if statut:
        clients = [c for c in clients if c.get("statut") == statut]
    if marche:
        clients = [c for c in clients if c.get("marche") == marche]
    return clients


def find_client(query):
    data = _load()
    query = query.lower()
    return [
        c for c in data["clients"]
        if query in c["nom"].lower()
        or query in c.get("telephone", "")
        or query in c.get("email", "").lower()
    ]


def update_client_statut(client_id, statut):
    data = _load()
    for c in data["clients"]:
        if c["id"] == client_id:
            c["statut"] = statut
            c["historique"].append({"date": datetime.now().isoformat(), "action": f"Statut → {statut}"})
            break
    _save(data)


# --- DEVIS ---

def save_devis(client_id, client_nom, description_travaux, postes, total_ht, validite_jours=30, notes=""):
    data = _load()
    num = f"DEV-{datetime.now().strftime('%Y%m')}-{len(data['devis']) + 1:03d}"
    devis = {
        "id": _id(),
        "numero": num,
        "client_id": client_id,
        "client_nom": client_nom,
        "description": description_travaux,
        "postes": postes,
        "total_ht": total_ht,
        "validite_jours": validite_jours,
        "date_creation": datetime.now().isoformat(),
        "statut": "envoyé",
        "notes": notes,
    }
    data["devis"].append(devis)
    _save(data)
    return devis


def get_devis(statut=None):
    data = _load()
    devis = data["devis"]
    if statut:
        devis = [d for d in devis if d.get("statut") == statut]
    return devis


# --- FACTURES ---

def save_facture(devis_id, client_nom, montant_ht, echeance_jours=30, notes=""):
    data = _load()
    num = f"FAC-{datetime.now().strftime('%Y%m')}-{len(data['factures']) + 1:03d}"
    facture = {
        "id": _id(),
        "numero": num,
        "devis_id": devis_id,
        "client_nom": client_nom,
        "montant_ht": montant_ht,
        "echeance_jours": echeance_jours,
        "date_emission": datetime.now().isoformat(),
        "statut": "en attente",
        "notes": notes,
    }
    data["factures"].append(facture)
    _save(data)
    return facture


def get_factures(statut=None):
    data = _load()
    factures = data["factures"]
    if statut:
        factures = [f for f in factures if f.get("statut") == statut]
    return factures


def marquer_facture_payee(facture_id):
    data = _load()
    for f in data["factures"]:
        if f["id"] == facture_id:
            f["statut"] = "payée"
            f["date_paiement"] = datetime.now().isoformat()
            break
    _save(data)


# --- PLANNING ---

def add_planning(date, mission, client_nom="", type_mission="chantier", notes=""):
    data = _load()
    event = {
        "id": _id(),
        "date": date,
        "mission": mission,
        "client_nom": client_nom,
        "type": type_mission,
        "notes": notes,
        "statut": "planifié",
        "date_ajout": datetime.now().isoformat(),
    }
    data["planning"].append(event)
    _save(data)
    return event


def get_planning(jours=7):
    from datetime import timedelta
    data = _load()
    maintenant = datetime.now()
    limite = maintenant + timedelta(days=jours)
    events = []
    for e in data["planning"]:
        try:
            date_event = datetime.fromisoformat(e["date"])
            if maintenant <= date_event <= limite:
                events.append(e)
        except (ValueError, KeyError):
            pass
    return sorted(events, key=lambda x: x["date"])


def get_stats():
    data = _load()
    factures = data["factures"]
    ca_total = sum(f["montant_ht"] for f in factures if f["statut"] == "payée")
    ca_en_attente = sum(f["montant_ht"] for f in factures if f["statut"] == "en attente")
    return {
        "nb_clients": len(data["clients"]),
        "nb_prospects": len([c for c in data["clients"] if c["statut"] == "prospect"]),
        "nb_devis": len(data["devis"]),
        "nb_factures": len(factures),
        "ca_encaisse": ca_total,
        "ca_en_attente": ca_en_attente,
        "nb_missions_planifiees": len([e for e in data["planning"] if e["statut"] == "planifié"]),
    }
