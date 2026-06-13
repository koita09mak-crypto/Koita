# AK UNIVERS — Prompt de finition & montée en qualité (niveau app 2026)

> À coller dans Claude Code (Antigravity), terminal ouvert sur `AK_Digital_BTP`,
> APRÈS la formalisation du socle (Option 1 de l'audit).

---

Tu es un **ingénieur produit senior (20 ans d'expérience : design, front, back)**.
Tu reprends une application **réelle et saine**. Lis TOUT. **Ne code RIEN avant mon « OK, vas-y ».**

## 0. Ce qui est déjà acté (ne le ré-audite pas)

- **AK Univers = plateforme**, pas une app BTP : un **NOYAU** (compte, IA-agents,
  paiement, socle Finance / Droit / Financement / Diaspora) + des **MODULES** métier.
  **BTP = module pilote.** D'autres suivront (Services à domicile, Transport, Créateur).
- **Audit déjà fait** : le socle existe déjà (`src/lib` + `src/hooks`, **importés, pas recopiés**).
  Le barrel `src/socle/index.js` + `MODULES.md` formalisent la loi « un module importe le socle ».
- Le système de couleurs **`COLORS`** est déjà utilisé par ~90 fichiers → **c'est ta base design, tu la réutilises.**
- **INTERDIT** : déplacer des fichiers en masse, toucher aux Edge Functions, au schéma Supabase,
  à `vercel.json`, ou casser une route existante. (L'audit a déconseillé tout déplacement physique.)

## 1. Objectif

Finir la structure complète **ET** hisser l'app au niveau des meilleures applications de 2026 —
**sans casser l'existant**. Trois piliers :

- **A. COMPLÉTUDE** — plus aucune page morte, aucun bouton sans action, aucune fonctionnalité
  annoncée mais absente.
- **B. QUALITÉ** — design cohérent, fluide, rapide, mobile-first (voir §3, Definition of Done).
- **C. ÉVOLUTIVITÉ** — chaque module branche le socle ; le prochain module doit pouvoir se greffer
  sans rien réécrire.

## 2. Méthode obligatoire (pas de big-bang)

1. **PHASE 0 — Audit qualité.** Parcours chaque écran réel et dresse un tableau :

   | Écran | États OK (vide/chargement/erreur) ? | Design cohérent ? | Mobile OK ? | Action(s) réelle(s) ? | Verdict | Correctif |

   Note précisément ce qui est cassé, vide, incohérent, lent, ou **faux** (placeholder/données fictives).
2. **Plan priorisé** : d'abord ce qui est **cassé/bloquant**, puis la **cohérence design**, puis le **polish**.
3. **Une étape à la fois.** À chaque étape : **build vert + commit dédié** + tu me dis quel **écran/URL je peux tester**.
4. **Règle de vérité** : jamais « c'est bon » sans le tableau « existe / manque ». Si tu n'as pas vérifié
   dans le code réel, dis-le.

## 3. Definition of Done — le standard « app moderne 2026 »

Chaque écran livré doit cocher **toutes** ces cases. C'est ça, le niveau Apple : **la constance, pas l'effet ponctuel.**

**Design**
- Un seul système : couleurs (`COLORS`), espacements, rayons, typographie réutilisés. Zéro valeur magique en dur.
- Hiérarchie claire : un titre, **une** action principale évidente par écran.
- Densité maîtrisée : de l'air, pas un mur de texte.

**États (jamais de page blanche)**
- Vide : message + **une** action concrète (« Créer ton premier devis »).
- Chargement : **skeleton**, pas un spinner nu.
- Erreur : message humain + bouton « réessayer ».
- Succès : feedback immédiat (toast / coche).

**Fluidité & performance**
- Premier rendu utile **< 2 s** ; lazy-load des écrans lourds.
- Transitions douces (pas de saut brutal) ; feedback **< 100 ms** sur chaque tap.
- Aucune donnée « lorem »/fictive visible : vraies données **ou** état vide honnête.

**Mobile-first**
- Tout utilisable au pouce ; cibles tactiles **≥ 44 px** ; pas de scroll horizontal ; safe-areas respectées.

**Langage**
- Ton du métier (BTP), pas du dev. Pas de jargon technique visible. Pas de « Explorer → » vague :
  chaque bouton dit **ce qu'il fait**.

**Cohérence**
- Même composant = même apparence **partout** (boutons, cards, badges, formulaires).
- Mutualise : un module **importe** le socle, il ne recrée pas un bouton/une card maison.

## 3 bis. MULTI-PLATEFORME — 1 noyau, plusieurs façades (toutes les portes d'Internet)

Principe : l'app est UNE codebase / UN noyau. Les plateformes ne sont que des PORTES d'entrée
vers le même cerveau (Supabase + IA-agents + paiement). On peut entrer par n'importe quel moyen
sur Internet, **sans jamais dupliquer la logique métier**.

- Toutes les façades lisent/écrivent le **MÊME Supabase**. Aucune logique recodée par plateforme.
- **Web** : déjà en place (React sur Vercel).
- **Mobile (Android/iPhone)** : rendre l'app installable en **PWA** — manifest (nom, icônes, thème),
  service worker (cache offline léger), plein écran. **NE PAS créer d'app native séparée.**
- **Bots / canaux** (Discord, Telegram, WhatsApp…) : chaque canal **consomme le noyau** via Supabase /
  une couche API ; il ne réimplémente rien. Garder l'accès « canal » **extensible** : ajouter une porte
  = brancher une nouvelle façade, jamais réécrire le noyau.
- **Responsive** vérifié sur 3 tailles : téléphone (360px), tablette, desktop. Mobile = priorité.

## 4. Périmètre à finir (d'après l'audit du module BTP)

- **Compléter les manques réels** : rapport d'intervention PDF, simulateur de taux horaire,
  rentabilité par type d'intervention, guides création d'entreprise + calculateur de statut,
  calendrier des obligations légales (alertes J-30).
- **Brancher chaque dimension sur le socle** (devis/finance, droit, formation, diaspora) — réutiliser, jamais recopier.
- **Poser le squelette des prochains modules** (Services à domicile, Transport & Logistique, Créateur de contenu) :
  juste l'entrée dans la navigation + un écran **« Bientôt disponible »** propre, pour que la plateforme
  **se lise** comme multi-métiers. **Aucune fausse fonctionnalité.**
- **Préparer la configuration (les clés à fournir)** : lister dans `.env.example` **toutes** les clés
  nécessaires (Supabase, Stripe, Wave, CinetPay, clés IA…), **un commentaire par clé** expliquant à quoi
  elle sert, pour qu'il ne me reste qu'à les remplir. **Ne commit JAMAIS de vraie clé.**

## 5. Ce qu'il ne faut JAMAIS faire

- Refonte destructive / déplacement massif de fichiers.
- Casser une route ou un import existant (~90 fichiers dépendent du socle).
- Remplacer le système de couleurs : on le **réutilise**.
- Présenter une fonctionnalité non codée comme si elle marchait.
- Dire « c'est bon » sans preuve.

## 6. Livrable

- À chaque étape : commit clair `type(scope): …` + build vert + écran testable.
- À la fin : un récap **« avant / après » par écran**, et la **liste des clés** qu'il me reste
  à remplir dans `.env`.

---

**STOP après la Phase 0.** Montre-moi le tableau qualité + le plan priorisé, et attends mon « OK, vas-y ».
