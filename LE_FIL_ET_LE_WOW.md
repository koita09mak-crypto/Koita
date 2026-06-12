# AK UNIVERS — Le FIL & le WOW (définition des domaines + leurs connexions)

> **Le problème (Adama, 12/06)** : la base/moteur existe, mais les **domaines** (droit, financement,
> formation, créateur…) sont **dispersés et mal définis** → pas de fil, pas de WOW. Or « faire des devis »,
> toutes les apps le font. Ce doc met les **angles morts à plat** et définit le **fil** qui relie tout.

---

## 1. Le principe du WOW (à graver)

> **Le WOW n'est PAS dans les domaines pris séparément. Il est dans la CONNEXION entre eux, autour de la situation réelle de l'utilisateur.**

Une app normale = des outils séparés. **AK = le cerveau qui relie tout.** Le moteur d'échéances/routines
(unifié le 12/06) est le **mécanisme** de cette connexion : il surveille tous les domaines et fait remonter
le bon signal au bon moment. → Le fil = **l'utilisateur et sa situation** ; AK connecte les points.

**Scénario WOW (BTP)** — tu signes un chantier de 15 000 € :
- 💰 plafond micro approché → options (droit + financement)
- 📋 clause de retard à ajouter au devis (droit)
- 🎓 habilitation utile, finançable CPF (formation + financement)
- 📸 photos avant/après → post pour se faire connaître (créateur)

→ **Aucune app de devis ne fait ça.** C'est le différenciateur.

---

## 2. Définition des domaines *(v1 — à affiner avec Adama)*

| Domaine | Ce qu'il fait (le rôle) | Le WOW (la connexion) |
|---|---|---|
| **Entreprise** | Piloter sa boîte : statut, obligations, rentabilité, plafonds | Cockpit qui **surveille la santé** de l'entreprise et **prévient avant** le problème |
| **Droit / Juridique** | Obligations légales, contrats, clauses, mentions, RGPD, statut | AK **veille à ta place** : tu n'as pas besoin de connaître le droit, il t'alerte au bon moment (→ devis, entreprise) || **Financement** | Aides (ACRE, CPF), financer un projet, trésorerie | « Tu as droit à **cette aide** » / « voici comment financer **ce chantier** » au bon moment (→ formation, entreprise) |
| **Formation** | Monter en compétence (métier, entreprenariat, IA) | Pas un catalogue : **la bonne formation pile quand un manque te bloque** (→ chantier, financement) |
| **Créateur de contenu** | Se faire connaître (posts, vidéos, avant/après) | Transforme ton **travail réel** (chantier fini) en **contenu marketing** automatiquement (→ chantier, emploi) |
| **Emploi / Marketplace** | Trouver chantiers / clients / sous-traitance | Te **connecte aux opportunités** pertinentes pour ton métier (→ profil, contenu) |
| **Diaspora** | Pont France ↔ Afrique de l'Ouest | Gérer une activité sur **2 marchés** depuis un seul endroit (transferts, projets au pays) |
| **Tangible (QR / scan / colis / logistique)** | Suivi matériaux, livraisons, chantier via QR | **Preuve de sérieux** : « c'est un vrai outil d'entreprise », pas un jouet (→ chantier, transport) |

---

## 2 bis. ⚠️ « Droit » = 3 couches à NE PAS confondre (angle mort relevé par Adama, 12/06)

« Le droit » n'est pas une chose unique. Trois couches distinctes :

| Couche | C'est quoi | Appartient à | Quand |
|---|---|---|---|
| **A. Droit de l'UTILISATEUR** | aider l'user avec SA vie juridique (obligations, contrats/devis conformes, droits ET devoirs) | une **FONCTIONNALITÉ** (le module Droit, dans le wow) | produit |
| **B. Droit de la PLATEFORME AK** | conformité d'AK : CGU, CGV, confidentialité, **RGPD** (AK = responsable de traitement), mentions, responsabilité, rétractation | un **DEVOIR d'AK** | **avant lancement** |
| **C. Droit du PAIEMENT** | agrément, KYC, anti-blanchiment, DSP2, TVA, facturation | surtout les **PSP** (Stripe/Wave/CinetPay) + devoirs d'AK | au lancement |

- **A = valeur user** (le « domaine Droit » du wow). **B + C = devoirs d'AK** (pas une feature, juste être en règle).
- **Déjà entamé** : la couche B via le RGPD d'hier (suppression compte/conservation). La couche C est **déléguée aux PSP** (AK n'est pas une banque → bonne archi).
- ⚠️ **Caveat** : le consultant n'est PAS juriste. B + C (CGU/CGV/RGPD) → **à valider par un vrai juriste avant lancement** (trame préparée, juriste confirme). Vont dans la **checklist de lancement**.

---

## 3. Le FIL (ce qui relie tout)

Chaque domaine n'est pas une île : il **déclenche** des signaux dans les autres. Le moteur de routines
les fait dialoguer autour de l'utilisateur. → **La cohérence vient de là, pas d'un menu bien rangé.**

**À définir (les angles morts à combler)** : pour chaque domaine, les **connexions précises** (quel
événement dans le domaine A déclenche quoi dans le domaine B). C'est ce qui transforme « 8 modules
dispersés » en « 1 assistant qui pense à ta place ».

---

## 4. Prochaine étape
Creuser **domaine par domaine** : pour chacun, écrire les 2-3 **scénarios WOW concrets** (les connexions
réelles). Commencer par celui qu'Adama sent le plus. → puis le moteur les exécute (lignes de config).
