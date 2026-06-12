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

---

## 5. Domaine DROIT — couche A (valeur user) — scénarios WOW *(défini 12/06)*

Rôle : **AK veille, l'utilisateur n'a pas à connaître le droit.** Tout part de sa **situation réelle**.

| # | Scénario WOW | Connecté à | État |
|---|---|---|---|
| 1 | **Documents toujours conformes** (devis/facture : mentions, TVA, statut) | Devis | ✅ commencé |
| 2 | **Alertes d'obligations AVANT la faute** : plafond micro, URSSAF, RC Pro/décennale à renouveler, habilitation qui expire | Entreprise + Financement | détecteurs (moteur unifié) |
| 3 | **Clauses intelligentes selon le chantier** : acompte, retard, réserve, garantie | Devis / Contrat | à construire |
| 4 | **Tes DROITS, pas que tes devoirs** : aides, **recours en cas d'impayé**, médiation | Finances / Financement | à construire |
| 5 | **Premier réflexe juridique** : question en langage simple → réponse selon statut *(info, pas conseil d'avocat)* | IA | à construire |

**Le fil du Droit** : un devis / un montant / une échéance / un impayé → AK relie le droit aux autres
domaines **automatiquement**. Plus une rubrique isolée → une **vigilance permanente** portée par le moteur.

*(Rappel : ceci = couche A. Les couches B/plateforme et C/paiement = devoirs d'AK, checklist de lancement, à valider par un juriste — cf. §2 bis.)*

---

## 6. Domaine FINANCEMENT — scénarios WOW *(défini 12/06 — « commencer par le commencement »)*

Rôle : **AK ne te laisse jamais passer à côté d'argent auquel tu as droit** (domaine où les gens perdent de l'argent par ignorance : aides non réclamées, CPF jamais utilisé).

| # | Scénario WOW | Connecté à |
|---|---|---|
| 1 | **Aides au démarrage, au bon moment** : « active l'**ACRE AVANT** immatriculation », maintien ARE, microcrédit | Entreprise + Droit |
| 2 | **Formation financée** : « cette formation = 100% **CPF** / AIF Pôle Emploi » | Formation |
| 3 | **Financer matériel/projet** : prêt d'honneur, leasing, microcrédit pro | Entreprise + Tangible |
| 4 | **Anticipation trésorerie** : « trou de cash dans 3 sem. → relance / avance sur facture » | Finances + Droit (impayés) |
| 5 | **Diaspora** : financer un projet au pays, microfinance locale, transferts | Diaspora |

**WOW central** : *« AK trouve l'argent que tu ne savais pas pouvoir avoir. »* Le **timing** est le wow (ACRE après immatriculation = perdue → AK prévient avant). Brique `lib/financement.js` (CPF/ACRE/aides) existe déjà dans le socle.

**Caveat** : AK oriente/informe, l'**éligibilité finale se confirme auprès de l'organisme** (Pôle Emploi/URSSAF). On détecte et on guide, on ne promet pas.

**Le fil** : se déclenche depuis la situation — création d'entreprise → ACRE · manque de compétence → CPF · impayé → avance · projet → prêt.

---

## 7. Domaine CRÉATEUR DE CONTENU — scénarios WOW *(défini 12/06)*

Rôle : **rendre créateur quelqu'un qui n'y connaît rien** (ne sait ni quoi poster, ni comment, ni les procédures).

| # | WOW | Connecté à |
|---|---|---|
| 1 | **Ton travail réel → du contenu** (chantier fini/produit → post, vidéo avant-après) | le métier |
| 2 | **Il te dit QUOI poster** (idées par métier, jamais la page blanche) | IA |
| 3 | **Il t'apprend COMMENT** (filmer, accroche, modèles) | Formation |
| 4 | **Un effort → partout** (Insta/TikTok/LinkedIn/Facebook) | — |
| 5 | **Le contenu ramène des clients** | Emploi / Marketplace |

**WOW** : *« Tu bosses, AK fait ta com'. »*

## 8. Domaine FORMATION — scénarios WOW *(défini 12/06)*

Rôle : **trouver, financer et réussir** sa formation — **pour TOUS les métiers** — même sans savoir comment s'y prendre.

| # | WOW | Connecté à |
|---|---|---|
| 1 | **La bonne formation au bon moment** (suggérée quand un manque bloque, pas un catalogue) | moteur (détecte le manque) |
| 2 | **Financée** (100% CPF / Pôle Emploi) | Financement |
| 3 | **Procédures gérées** (inscription, dossier, organisme) | Droit |
| 4 | **Suivi jusqu'au bout** (progression, certif, habilitation) | Compétences / Droit |
| 5 | **Tous les métiers** (BTP, transport, commerce, créateur…) | universel |

**WOW** : *« AK sait de quoi tu as besoin avant toi, et te porte jusqu'à la certif. »*

---

## 9. 🔄 LA BOUCLE VERTUEUSE (le cœur du « ça s'interagit dedans » — Adama)

> **Tu bosses** → AK détecte un **manque** → **Formation** (financée **CPF**) → **nouvelle compétence** (+ certif = **Droit**) → **meilleur travail** → **Contenu** (créateur) → **visibilité** → **nouveaux clients** (Emploi) → **plus de travail…**

**AK fait tourner la vie pro en boucle vertueuse** : chaque domaine nourrit le suivant, porté par le moteur de routines. **C'est le wow ultime, et il est universel (tous métiers).** ← LE différenciateur d'AK Univers.

---

## 10. Domaines restants — scénarios WOW *(définis 12/06)*

### ENTREPRISE (le cockpit)
Rôle : piloter sa boîte sans voler à l'aveugle. Santé (CA/encaissé/plafond/rentabilité) · alertes statut/obligations · guide création/passage au réel · rentabilité par type de presta.
**WOW** : *« AK surveille la santé de ta boîte à ta place. »* → Droit + Financement + Finances.

### EMPLOI / MARKETPLACE
Rôle : ne pas attendre le travail. Chantiers/missions adaptés (métier+zone) · le contenu ramène des clients · sous-traitance · missions France↔AOF.
**WOW** : *« AK te ramène le travail, tu ne le cherches plus. »* → Créateur + Diaspora + profil.

### DIASPORA (angle UNIQUE)
Rôle : pont France ↔ Afrique de l'Ouest. Gérer 2 marchés d'un endroit (devises, fuseaux) · projets au pays à distance · transferts/financement (mobile money) · normes FR appliquées en AOF.
**WOW** : *« Le seul outil pour celui qui vit et travaille entre deux continents. »* ← personne d'autre.

### TANGIBLE (QR / scan / colis / logistique)
Rôle : l'opérationnel concret = preuve de sérieux. QR sur devis/facture/chantier · suivi matériaux/colis/livraisons · transport.
**WOW** : *« Du palpable — AK n'est pas un jouet, c'est un vrai outil de terrain. »*

---

## ✅ CARTE COMPLÈTE — 8 domaines définis
Entreprise · Droit · Financement · Formation · Créateur · Emploi/Marketplace · Diaspora · Tangible — tous reliés par **la boucle vertueuse** (§9) et le **moteur de routines unifié**. Persona n°1 = **Adama** (test sur son cas réel d'abord). → Prochaine étape : **audit dans le projet** (ce qui existe vs ces scénarios wow) avant de construire.

---

## 11. AUDIT PROJET + PLAN DE CÂBLAGE DE LA BOUCLE (agent, 12/06)

**Constat décisif** : chaque domaine est **riche à l'intérieur** (tout existe), MAIS les **connexions inter-domaines manquent** (le fil/la boucle). Un `event_bus` était prévu pour ça → **dormant** (jamais émis). Le seul véhicule vivant = le **moteur unifié** (moteurEcheances/detecteurs). → **Le wow = relier, pas reconstruire.**

**Gaps de connexion par domaine** : Activité ne nourrit ni CV ni Contenu ni Formation · Droit sans escalade réelle · Financement pas déclenché au bon moment · Formation : maillon « manque→formation » absent · Créateur : rien depuis l'Activité · Emploi : CV ne lit pas devis/chantiers.

**Plan de câblage (chacun = 1 détecteur, 0 migration, réutilise l'existant) :**
- **Étape 1** — **chantier fini → « raconte-le en vidéo » → générateur de script pré-rempli.** L'étincelle la plus spectaculaire ; relie les **2 identités d'Adama** (technicien BTP ↔ Koïta Mak créateur) = dogfooding parfait. ✅ **FAIT (12/06)** : détecteur « chantier terminé + rien publié depuis 14j → 🎬 Raconte ton chantier X → GenerateurScript pré-rempli (TikTok) ». Marche **sans clé IA** (pré-remplissage OK, fallback playbook). Garde-fous : pas de harcèlement, pas de bruit, priorité 55.
- **Étape 2** — **compétence/certif qui expire → formation financée (CPF) → certif** (réutilise `certifs` + `financement.js`, dédoublonne les catalogues).
- **Étape 3** — **travail → CV auto-rempli (chantiers/devis) → missions** (la boucle revient à l'Emploi).

→ Construit pas à pas, prouvé, s'affiche sur le QG/accueil. **C'est le passage de « app de devis » à « assistant qui relie tout ».**
