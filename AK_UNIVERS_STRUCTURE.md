# AK UNIVERS — Structure de référence

> **Dernière mise à jour : 2026-06-11**
> Document carte. C'est ICI qu'on regarde quand on se demande « on en est où, c'est quoi le plan ».
> La règle d'or : **AK Univers est le NOYAU. Les métiers sont des MODULES branchés dessus.**

---

## 1. La vision en une phrase

> ### ⭐ Promesse n°1 (north star)
> **Tout ce qui est répétitif, long ou compliqué dans ta journée, AK le simplifie ou le fait à ta place — et t'apprend ce que tu ne maîtrises pas — pour que tu puisses entreprendre et créer sans être bloqué par le manque de temps ou de connaissances.**
>
> Version courte : **« Le difficile, le répétitif, l'inconnu — AK s'en occupe, pour que toi tu avances. »**

Cette promesse **unifie tout** (et tue l'effet « dashboard générique ») :
- les **agents** font le répétitif à ta place,
- la **formation** comble le manque de connaissances,
- les **modules** (entreprise, création, IA) débloquent l'envie d'entreprendre.

Tout sert **un seul but : faciliter** (l'esprit Apple « it just works »).

AK Univers est une plateforme propulsée par l'IA qui accompagne chaque personne dans sa vraie vie
professionnelle — quel que soit son métier — en réunissant au même endroit le travail, l'argent,
la formation, le droit et la diaspora.

L'IA n'y est pas un chatbot. C'est un **moteur qui travaille à la place de l'utilisateur** : elle
génère le devis, anime la formation, trie les offres d'emploi, relance les clients.

---

## 2. Le principe fondateur : on part des VRAIES VIES, pas des modules

On ne conçoit pas en « fonctionnalités ». On conçoit autour de **personnes réelles** et de ce qu'elles vivent. Leurs besoins **se croisent** : une même personne traverse plusieurs modules.

| La personne | Sa vraie vie / son problème | Modules AK Univers utilisés |
|---|---|---|
| **Adama / l'électricien** (France) | Chantiers, habilitations, devis, se faire payer | BTP · Finance · Formation · Diaspora |
| **Fatou** (services à domicile) | Trouver des clients, facturer, être en règle | Services à domicile · Finance · Droit |
| **Karim** (créateur / jeune actif) | Monétiser son savoir, se former, trouver un job | Créateur de contenu · Formation · Emploi |
| **Le livreur** (Afrique) | Livraisons, tournées, gérer ses recettes | Transport & Logistique · Finance |
| **Le Sénégalais de la diaspora** | Se former à distance, envoyer/recevoir de l'argent | Formation · Diaspora · Finance |

> ⚠️ Personas **Fatou** et **Karim** à confirmer/affiner par Adama. Le reste est validé.

**Lecture clé :** presque tout le monde touche à **Finance** ; beaucoup touchent à **Formation** et **Diaspora**. Donc ces briques sont **communes** → elles vivent dans le NOYAU, pas dans un métier.

---

## 3. La carte complète

```
        ┌───────────────────────────────────────────────────────┐
        │                      AK  UNIVERS                        │
        │     Compte unique · IA qui TRAVAILLE · Paiement         │
        │   SOCLE : Finance · Droit · Financement · Diaspora      │ ← sert à TOUS
        └───────────────────────────────────────────────────────┘
          │         │          │          │           │         │
       ┌──┴─┐  ┌────┴───┐ ┌────┴───┐ ┌────┴────┐ ┌────┴────┐ ┌──┴──────┐
       │BTP │  │Services│ │Créateur│ │Formation│ │ Emploi  │ │Transport│
       │    │  │à domic.│ │contenu │ │         │ │         │ │ & Logist│
       └────┘  └────────┘ └────────┘ └─────────┘ └─────────┘ └─────────┘
```

---

## 4. Règle d'architecture : SOCLE vs VERTICAL

**Séparation légère, pas de sur-ingénierie** — Adama est seul à porter et maintenir le projet : on garde simple pour qu'il en **garde le contrôle** (ce n'est pas une question d'argent, mais de maîtrise).

### NOYAU / SOCLE (construit UNE fois, partagé par tous les modules)
- **Compte / identité** utilisateur
- **IA / agents** (Devis, Commercial, Chantier… réutilisables par tout métier)
- **Paiement** (Wave, CinetPay, et autres)
- **Finance / Compta** : devis, factures, TVA, URSSAF, rentabilité
- **Droit** : statuts juridiques, contrats, obligations légales
- **Financement** : CPF, ACRE, aides, subventions
- **Diaspora** : transferts d'argent, formation à distance, France ⇄ Afrique

### VERTICAUX (un par métier ; ne contiennent QUE le spécifique ; **importent** le socle)
- **BTP** : chantiers, planning, habilitations, normes NF C, bibliothèque de prix BTP
- **Services à domicile** : prestations, clients récurrents
- **Créateur de contenu** : audience, monétisation
- **Formation** : catalogue, certifications, progression *(transversal mais présenté comme module)*
- **Emploi** : offres, candidatures, matching
- **Transport & Logistique** : tournées, livraisons, recettes

> **Loi non négociable :** un vertical **IMPORTE** le socle, il ne le **recopie jamais**.
> Quand on ajoutera « Services à domicile », il doit réutiliser Finance/Droit/Diaspora **sans les réécrire**.

---

## 4 bis. Les façades — toutes les portes d'Internet

On ne fait **PAS** trois applications séparées. **Un seul noyau, plusieurs façades** : on peut entrer
par n'importe quelle porte d'Internet, et tout pointe vers le même cerveau (Supabase + IA + paiement).
Une donnée saisie sur le téléphone apparaît sur le web et dans le bot — **un seul endroit à maintenir.**

```
              NOYAU  (Supabase · IA-agents · paiement · socle)
                    ▲             ▲              ▲
                 ┌──┴──┐     ┌────┴────┐    ┌────┴────┐
                 │ WEB │     │ MOBILE  │    │  BOTS   │
                 │navig│     │PWA/Andr.│    │ canaux  │
                 └─────┘     └─────────┘    └─────────┘
```

- **Web** : déjà en place (React sur Vercel).
- **Mobile (Android / iPhone)** : l'app web rendue **installable en PWA** — une seule codebase,
  pas d'app native séparée.
- **Bots / canaux** (Discord, Telegram, WhatsApp…) : chaque canal **consomme le noyau** via Supabase /
  une couche API. Le `replit_bot.py` est la première façade-bot.
- **Loi** : ajouter une nouvelle porte d'entrée ne doit **jamais** obliger à toucher la logique métier du noyau.

---

## 5. Ordre de lancement (focalisé : un module à la fois)

Comme Amazon a démarré **aux livres uniquement** avant de tout vendre, et l'iPhone avec une poignée de fonctions :

1. **Bâtir le NOYAU proprement** (compte, IA, paiement, socle Finance/Droit/Financement/Diaspora).
2. **Lancer UN seul module : le BTP** — parce que c'est le métier qu'Adama connaît et peut rendre crédible. C'est le « rayon livres » d'AK Univers.
3. **Brancher les modules suivants** (Services, Transport, Créateur…) sur le noyau, sans tout refaire.

Vision = large. Lancement = focalisé.

---

## 6. Règle de vérité (anti « c'est bon »)

Historique : les outils répondaient « c'est bon / c'est fait » sans vérifier → des failles cachées sortaient plus tard.

**Désormais, jamais de « c'est bon » sans preuve.** Toute affirmation d'avancement doit s'accompagner d'un tableau :

| Élément | Existe déjà ? | À créer | À compléter | Ne pas toucher |

Si ça n'a pas été vérifié dans le code réel, on le dit. Pas de réassurance à vide.

---

## 7. Décisions actées

- **Promesse n°1 (north star)** : AK **facilite** — il fait le répétitif/difficile à ta place et comble le manque de connaissances. L'accueil et la navigation se construisent autour de ça. *(2026-06-11)*
- **Promesse agents = « AK REPÈRE pour toi », pas « AK travaille pendant que tu dors »** *(2026-06-11)*
  - Vérité technique : les 5 agents = **moteur de règles côté client** qui scanne les vraies données **à chaque ouverture de l'accueil**. Pas de cron serveur, pas de table `agent_logs` persistante → **aucune autonomie nocturne réelle.**
  - Wording validé pour le héros : **« CE QU'AK A REPÉRÉ POUR TOI »** (exact, défendable). On ne dit ni « a fait », ni « cette nuit ».
  - Règle : ne jamais promettre une autonomie qui n'existe pas. Un utilisateur trahi une fois ne revient pas.
- **État vide du héros (jour 1)** : jamais de héros vide ni de faux « tout va bien ». Si compte vierge → carte unique qui vend : « Tes agents sont prêts à travailler pour toi » + 1 bouton (« Créer mon 1er devis → »). *(2026-06-11)*
- **Audit du cœur DEVIS → FACTURE → PAIEMENT (2026-06-11)** : la boucle est **structurellement complète et persiste bien** (schéma sain, RLS OK, statuts/retard/relances câblés, PDF généré, build vert + 29 tests). MAIS elle **n'a jamais tourné sur du réel** (0 client / 0 devis / 0 facture en base). 3 faiblesses + plan de réparation (ordre de levier) :
  1. ✅ **FAIT (2026-06-11)** — **Capter l'entreprise tôt** (SIRET, raison sociale, **régime TVA**). 4e étape onboarding + gate (pas de PDF sans SIRET/raison sociale). PDF conforme prouvé : micro → « TVA non applicable, art. 293 B du CGI » ; réel → TVA au taux. **Vérifié de visu sur PDF.**
  2. ✅ **FAIT (2026-06-11)** — **Vraies lignes de devis** (désignation/qté/PU/unité/total) + **TVA multi-taux par ligne** (20/10/5,5 + taux par défaut réglable) + mode forfait rapide en 1 ligne. Récap TVA par taux + Total HT/TVA/TTC. **Vérifié de visu** sur 2 PDF (micro 1 ligne + réel multi-taux, totaux justes : HT 6320 / TVA 832 / TTC 7152).
  3. **Verrouiller le lien devis↔facture** (marquer « facturé » à la conversion, pas de double facturation). ← **SUIVANT**
  4. ✅ **FAIT (2026-06-11) — Grand test bout-en-bout sur du RÉEL** (compte test en prod). PDF devis + facture **validés de visu** : accents OK, totaux justes (devis 4 937 €), facture conforme (émetteur / facturé à / référence devis / conditions légales). Le test a révélé des bugs réels que l'audit code avait ratés → **preuve que tester sur du réel est indispensable** :
     - 🔴 ✅ **CORRIGÉ (2026-06-11)** — création de client cassée (dérive de schéma). Table `clients` migrée au bon schéma + Clients.jsx aligné. **Prouvé via l'UI** (création/recherche/édition d'un vrai client, is_demo=false).
     - 🟠 ✅ **CORRIGÉ (2026-06-11)** — TTC faux à l'écran. CA/KPI/liste factures calculent maintenant le TTC par ligne comme le PDF (4 surfaces = 4 937 € sur le cas multi-taux). Compte de test purgé après vérif (prod propre).
     - 🟠 ✅ **CORRIGÉ (2026-06-11)** — Friction inscription : accès immédiat (<30 s, sans cliquer de mail) + confirmation différée (bandeau « confirme ton adresse » non-bloquant, vérif conservée). **Prouvé** (parcours Sara Test). Activations optionnelles côté Adama : `RESEND_API_KEY` (envoi réel des emails) + Supabase Auth « Confirm email » OFF.
     - 🔵 Mineur : téléphone non capté à l'onboarding, seed clients démo inexploitable.
  5. **Structurer la base Supabase** (le test a prouvé qu'il y a de la dérive de schéma → audit DB complet). ← après les 2 fixes
- AK Univers = **noyau/plateforme** ; les métiers = **modules**. *(2026-06-11)*
- Le **BTP** est le **module pilote** de lancement. *(2026-06-11)*
- **Finance, Droit, Financement, Diaspora** sont dans le **SOCLE** (partagés). *(2026-06-11)*
- L'IA est un **moteur qui agit**, pas un chatbot. *(2026-06-11)*
- Multi-plateforme = **1 noyau, plusieurs façades** (Web · Mobile/PWA · Bots). Aucune logique dupliquée par plateforme. *(2026-06-11)*
- Méthode obligatoire : **audit d'abord** (Phase 0) avant toute création. *(2026-06-11)*

## 8. Questions ouvertes

- Définition précise des personas **Fatou** et **Karim**.
- Le noyau (compte + IA + paiement + socle) existe-t-il déjà dans l'app `AK_Digital_BTP`, ou est-il dupliqué dans les pages ? → audit à lancer.
- **Roadmap — vraie autonomie des agents** : faire tourner les agents en arrière-plan côté serveur (cron) + table `agent_logs` persistante. C'est ce qui débloquera la promesse « AK travaille pendant que tu dors » (« CE QU'AK A FAIT POUR TOI CETTE NUIT »). Différenciateur fort, mais nécessite du back. *(noté 2026-06-11)*
