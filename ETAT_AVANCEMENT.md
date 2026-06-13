# AK Univers — État d'avancement

> **Mis à jour : 2026-06-13**
> Check-list vivante. Vert = fait/en prod · 🔄 = en cours · ⬜ = à faire.
> On coche à chaque session. (Carte de la vision : `AK_UNIVERS_STRUCTURE.md`.)

---

## 1. Fondations (structure) — ✅ POSÉES
- [x] AK Univers = noyau/plateforme, métiers = modules
- [x] Socle commun défini : Finance · Droit · Financement · Diaspora
- [x] Multi-plateforme : 1 noyau, plusieurs façades (Web · Mobile/PWA · Bots)
- [x] IA = moteur qui agit, pas un chatbot
- [x] Méthode : audit d'abord · anti « c'est bon » (preuves) · 1 dimension = 1 session
- [x] Docs de référence : `AK_UNIVERS_STRUCTURE.md`, `PROMPT_FINITION`, `MODULES.md`
- [ ] Personas Fatou et Karim à préciser

## 2. Noyau / socle (code) — ✅ PROPRE
- [x] Socle formalisé (barrel `src/socle`, `MODULES.md`)
- [x] Duplications éliminées (stats + TVA)
- [x] Helper partagé `etatExpiration()`
- [x] **Brique Financement** (`lib/financement.js` : CPF/ACRE/aides) — créée dans le socle (phase Entreprise)

## 3. Module BTP (pilote) — ✅ 5/5 COMPLET
- [x] **Terrain** (planning, chantiers, rapport, matériaux, bilan)
- [x] **Compétences** (certifs badges 90j, alertes, catalogue, objectifs, normes)
- [x] **Argent** (KPIs Facturé/Encaissé/En attente/Rentabilité, devis lié, dépenses, rentabilité par type, simulateur)
- [x] **Entreprise** (statut + alertes plafond/décennale/RC Pro, guide création + calculateur, fournisseurs, sous-traitants, obligations J-30, simulateur, **+ brique Financement**)
- [x] **Avenir** (IA/automatisation, créer du contenu, former, diaspora, progression)
- [x] Placeholder `BtpBientot.jsx` supprimé (nettoyage)

🎉 **PILOTE BTP COMPLET — 5 dimensions en prod, socle propre, zéro dette.**

## 4. Vers la v1 lançable — 🔄 EN COURS
> Ordre détaillé dans `PLAN_DE_CONCLUSION.md`. On finit le **wow**, puis on **polit**, puis on **branche les clés**, puis on **lance**.

- [x] **SIMPLIFICATION (UX universelle)** ✅ **FAIT (2026-06-13)** — accueil 1 focus + **vocabulaire par métier**
  (artisan → « Nouveau devis » / « Devis · Chantiers · Équipe » ; ménage → « Nouvelle prestation » / « Prestations · Ménages · Équipe »),
  menu 5 entrées + « Tout AK » universel, **fin de la fuite BTP** (un profil non-BTP ne voit plus devis/chantier),
  mobile (BottomTabBar). Tests verts. *(PR #2 sur l'app `AK_Digital_BTP` — déploiement Vercel.)*
- [ ] **Mode démo populé** — sentir l'app + amener le « aha » (cf. `RETENTION_ET_PRIX.md`)
- [ ] **Refonte landing** — vendre le RÉSULTAT, pas l'IA
- [ ] **Rôles / cockpit fondateur** — plan 5-points (cf. `PLAN_DE_CONCLUSION.md`, audit rôles)
- [ ] **La boucle (le wow)** — étape 2 : certif qui expire → formation financée (CPF) → certif ; étape 3 : travail → CV auto-rempli
- [ ] **Passe de finition qualité 2026** (le gros prompt) : états, perf, cohérence sur toute l'app (cf. `PROMPT_FINITION_AK_UNIVERS.md`)
- [ ] **PWA / mobile** : manifest + service worker → app installable Android/iPhone
- [ ] **Squelettes des autres modules** (Services à domicile, Transport, Créateur) : entrée + « Bientôt disponible »
- [ ] **Config des clés** : `.env.example` documenté (Supabase, Stripe, Wave, CinetPay, IA)
- [ ] **Légal** : CGU / CGV / confidentialité / RGPD → valider par un juriste
- [ ] **Bots / canaux** (Discord/Telegram/WhatsApp) — `replit_bot.py` comme base

---

## 🎯 Où on en est
- Fondations + noyau = **✅ faits**
- Pilote BTP = **✅ 5/5 COMPLET**
- v1 lançable = **🔄 en cours** : **SIMPLIFICATION bouclée (13/06)** → prochaine étape : mode démo populé, puis finir la boucle (wow) + qualité/PWA → rendre l'app « payable ».

## Décisions métier actées (rappel)
- KPI fiscal = **ENCAISSÉ** (base URSSAF / plafond micro), pas le facturé. *(2026-06-11)*
- Décennale / RC Pro stockées sur `profils` (pas de table assurances dédiée). *(2026-06-11)*
- Financement = brique du **socle**, consommée par les modules, jamais enfermée dans le BTP. *(2026-06-11)*
- UX universelle : 1 accueil / 1 menu, **vocabulaire adapté par métier** (anti-fuite BTP). *(2026-06-13)*
- **Philosophie « Apple » — l'IA est le moteur invisible, le PRODUIT est ce qu'on voit** *(principe fondateur, vaut PARTOUT : landing ET toute l'app)* :
  - L'IA n'est **jamais** l'objet qu'on manipule ni un argument de vente. C'est seulement **comment** ça marche, sous le capot.
  - L'utilisateur voit et utilise un **PRODUIT réel qui respecte le réel** (son vrai métier, son vrai flux : devis, chantier, paiement, être en règle) — pas « une IA ».
  - Comme l'iPhone : bourré d'IA, mais les gens utilisent juste *un outil qui marche*. Ils ne pensent pas « j'utilise une IA », ils pensent « ça marche / ça m'a fait gagner du temps ».
  - Conséquence façade : bannir « IA », « intelligence », « plateforme universelle », « agents » → toujours le **bénéfice métier concret**. L'« effet IA » se **vit** à l'usage, il ne s'**annonce** pas.
  - (Le « certains ont peur de l'IA » n'est qu'une conséquence parmi d'autres — la vraie raison est la philosophie produit : respecter le réel, l'IA reste invisible.) *(2026-06-13)*
- **Cible = TOUS les métiers / indépendants, pas le BTP seul** *(positionnement, vaut PARTOUT)* :
  - L'app vise **tous ceux qui bossent à leur compte** : bâtiment, **transport, logistique**, ménage, commerce, créateur, diaspora… (tous les portails du projet).
  - **BTP = module pilote + preuve + ancre d'Adama** (sa force, la porte d'entrée) — **JAMAIS la cible exclusive.** ⛔ Interdit en façade : « l'appli des artisans du bâtiment » ou toute formule qui réduit au bâtiment.
  - La promesse est **universelle mais formulée concret/inclusif** : « ton activité », « ton métier », « quel que soit ton métier » — **PAS** le mot « plateforme universelle » (abstraction bannie).
  - Méthode : la promesse parle à tous · le BTP apparaît comme **exemple/preuve concrète** · les autres métiers sont **montrés** (visibles, pas vendus comme finis). *(2026-06-13)*
- **AK n'est PAS « une app mobile » — multi-façade à assumer en façade** *(positionnement)* :
  - On entre par **plusieurs portes** (même noyau / même Supabase) : 🌐 **Web** = porte principale, **déjà live sur Vercel**, rien à installer · 📱 **Mobile** = la même app **installable en PWA** (pas de native séparée) · 🤖 **Bots/canaux** (Discord/Telegram/WhatsApp).
  - Dedans = de **vrais produits**, pas juste des écrans. Ex. à montrer : le **CV en ligne auto-rempli** (chantiers/devis → CV partageable → missions), maillon de la boucle (Emploi).
  - ⛔ La landing ne doit **jamais** réduire AK à « une appli mobile ». Dire : « sur le web, rien à installer · aussi sur ton téléphone ». *(2026-06-13)*
- **Grille de prix actée — 3 paliers, ancrée sur la valeur** *(2026-06-13)* :
  - **Gratuit** : 3 devis + 3 factures/mois · 5 clients · alertes (coût zéro) · 1 user → l'habitude.
  - **Pro** : **29 €/mois** (290 €/an) · **5 000 FCFA/mois** (AOF) → illimité, tous les agents, la boucle, 1 user.
  - **Équipe** : **49 €/mois** (490 €/an) · **12 000 FCFA/mois** (AOF) → jusqu'à 5 users, rôles/partage, rapports avancés.
  - **Leviers** : **100 membres fondateurs = −30 % à vie** · **annuel = 2 mois offerts** · **essai 14 j Pro**.
  - **AOF = prix LOCAL** (mobile money **Wave** + Orange Money), pas une conversion du prix FR.
  - **Raison** : marge IA 96-98 % → le coût n'est pas le frein ; on price sur la **valeur/ROI** (AK fait plus que des concurrents à 30-50 €). L'accessibilité passe par **fondateurs + gratuit généreux**, jamais par un prix cassé (19 € = sous-vendre + signal « moins bien »).
  - **Conséquence code** : fondre les **4 paliers codés** (Free/Pro/Business/Enterprise) **→ 3** (Gratuit/Pro/Équipe). Garder Pro = 29 € (produit Stripe inchangé) ; collapse Business/Enterprise → Équipe. **Aligner `lib/plans.js` + Stripe AVANT la mise en ligne** (prix affiché = prix facturé). *(2026-06-13)*
