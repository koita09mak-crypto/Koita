# Guide de déploiement — Assistant IA AK Réseaux & Bâtiment
> Telegram Bot + Claude AI + iPhone

---

## Ce que tu vas avoir sur ton iPhone

Une application Telegram avec un assistant IA qui tourne 24h/24 pour ton entreprise :

- 📋 **Devis** — tu décris le chantier, le bot génère un devis complet
- 👥 **Clients** — ajouter, chercher, suivre tes prospects et clients
- 💰 **Factures** — créer, suivre, marquer comme payées
- 📅 **Planning** — missions chantier, rappels, agenda
- 🤖 **Assistant IA** — questions libres sur ton activité, stratégie, BTP, AOF

---

## ÉTAPE 1 — Créer ton bot Telegram (5 minutes, gratuit)

1. Ouvre Telegram sur ton iPhone
2. Cherche **@BotFather**
3. Tape `/newbot`
4. Donne un nom : `AK Réseaux & Bâtiment`
5. Donne un username : `AKReseauxBot` (doit se terminer par "bot")
6. BotFather te donne un **token** — copie-le, c'est précieux

**Récupère ton ID Telegram :**
1. Cherche **@userinfobot** sur Telegram
2. Tape `/start`
3. Il t'affiche ton ID — note-le

---

## ÉTAPE 2 — Compte Anthropic Claude (clé API)

1. Va sur **console.anthropic.com**
2. Crée un compte gratuit
3. Va dans "API Keys" → "Create Key"
4. Copie la clé (commence par `sk-ant-...`)

**Coût réel :** ~$0.01 à $0.05 par conversation.
Pour un usage quotidien normal : moins de $5/mois.

---

## ÉTAPE 3 — Hébergement gratuit sur Railway

**Railway** héberge ton bot gratuitement (500h/mois offerts).

1. Va sur **railway.app**
2. Crée un compte (gratuit, avec GitHub si tu en as un)
3. "New Project" → "Deploy from GitHub repo"
   (si pas de GitHub : "Deploy" → "Empty project")

---

## ÉTAPE 4 — Préparer le code

Sur ton ordinateur (ou demande de l'aide pour cette étape) :

```bash
# Cloner le repo
git clone [ton repo]
cd Koita/bot

# Créer le fichier .env
cp .env.example .env
```

Ouvre le fichier `.env` et remplis :

```
TELEGRAM_TOKEN=le_token_de_botfather
ANTHROPIC_API_KEY=ta_cle_anthropic
OWNER_TELEGRAM_ID=ton_id_telegram
BUSINESS_EMAIL=ton@email.fr
BUSINESS_PHONE=ton_numero
```

---

## ÉTAPE 5 — Déployer sur Railway

```bash
# Dans le dossier bot/
railway login
railway init
railway up
```

Ou via l'interface Railway :
1. Upload le dossier `bot/`
2. Ajoute les variables d'environnement (les mêmes que ton .env)
3. Deploy

Railway détecte automatiquement Python et installe les dépendances depuis `requirements.txt`.

---

## ÉTAPE 6 — Tester sur ton iPhone

1. Ouvre Telegram
2. Cherche ton bot : `@AKReseauxBot`
3. Tape `/start`
4. Le menu principal apparaît

---

## Structure des fichiers

```
bot/
├── main.py                  # Point d'entrée — gestion du bot
├── config.py                # Configuration et données entreprise
├── requirements.txt         # Dépendances Python
├── .env.example             # Variables d'environnement (modèle)
├── agents/
│   └── assistant.py         # Cerveau IA (Claude API)
├── handlers/
│   ├── menus.py             # Menus Telegram (boutons)
│   └── conversations.py     # Toute la logique des conversations
└── data/
    ├── storage.py           # Base de données locale (JSON)
    └── business_data.json   # Tes données (auto-créé au premier lancement)
```

---

## Utilisation quotidienne

### Générer un devis
1. Ouvre Telegram → ton bot
2. Appuie sur 📋 Devis → Nouveau devis
3. Tape le nom du client
4. Décris les travaux (ex: "Câblage réseau data 8 prises RJ45 bureau 120m², passage gaines, baie de brassage 12U")
5. Adresse du chantier (ou "passer")
6. **Le bot génère un devis professionnel complet en 10 secondes**

### Ajouter un client
1. 👥 Clients → Ajouter client
2. Remplis les infos au fur et à mesure
3. Choisis France ou Afrique de l'Ouest

### Poser une question à l'IA
1. 🤖 Assistant IA
2. Écris directement : "Comment trouver des clients en sous-traitance électricité à Paris ?"
3. Réponse personnalisée en quelques secondes

### Commandes rapides
- `/start` — revenir au menu principal
- `/stop` — interrompre une conversation en cours

---

## Évolutions prévues (Phase 2)

- Connexion Notion pour synchroniser les données sur tous tes appareils
- Rappels automatiques pour les factures en retard
- Envoi de devis par email directement depuis le bot
- Statistiques mensuelles automatiques
- Agent spécialisé marché AOF

---

## Coûts mensuels

| Service | Coût |
|---------|------|
| Telegram bot | Gratuit |
| Railway (hébergement) | Gratuit (500h/mois) |
| Claude API (usage normal) | ~$3-8/mois |
| **Total** | **~3-8€/mois** |

---

## En cas de problème

**Le bot ne répond pas** → Vérifie que Railway est bien déployé et actif

**Erreur "Invalid token"** → Vérifie le TELEGRAM_TOKEN dans les variables Railway

**Erreur "Authentication"** → Vérifie l'ANTHROPIC_API_KEY

**Besoin d'aide** → Ouvre une session avec Claude et colle le message d'erreur exact
