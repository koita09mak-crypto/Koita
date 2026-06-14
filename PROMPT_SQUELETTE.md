# AK Univers — Prompt SQUELETTE (refonte de l'ossature, pas de la peinture)

> À coller dans Claude Code sur `AK_Digital_BTP`.
> But : refaire le SQUELETTE de l'app — pas repeindre des écrans.
> Critère de réussite UNIQUE : un inconnu ouvre l'app et comprend en 10 secondes ce que c'est, quoi faire, pourquoi rester.
> Vient APRÈS tout le reste (qualité, PWA, cockpit, menu de compte) — c'est la passe manquante.

---

Tu es un **product designer + ingénieur front senior** (standard iPhone/Apple : l'app s'explique toute seule dès la première seconde).
Tu reprends une app RÉELLE (AK Univers), en production. Lis TOUT le code. **Ne code RIEN avant mon « OK, vas-y ».**

## 0. Ce qui est sacré (NE touche pas)
- Le **code métier** : les écrans devis / chantiers / argent / compétences / cockpit → ils marchent, on les **raccroche** sous le nouveau squelette, on ne les réécrit pas.
- Le schéma Supabase, les Edge Functions, les prix (`plans.js`), la sécurité des rôles (RLS, AdminGuard).
- Les composants existants (`COLORS`, `StatCard`, `EmptyState`, `BottomTabBar`) → base de départ, on les élève.

## 1. Le vrai problème (diagnostic exact, pas à re-débattre)
Les passes précédentes ont **repeint** (skeletons, couleurs, transitions). Résultat : toujours des murs plats + deux maisons + sens introuvable.
C'est un problème de **squelette**, pas de peinture. Le squelette, c'est :
- **L'ouverture** (le tout premier écran après connexion — le moment iPhone où l'utilisateur dit « ah je comprends »).
- **La maison unique** (une seule porte d'entrée, pas deux `/app` vs `/app/:portail/dashboard`).
- **Le regroupement par univers** (pas une liste plate — des espaces clairs : Activité / Argent / Évoluer / etc.).
- **La cohérence intérieure** de chaque section, en particulier « Argent » (incohérente aujourd'hui).
- **L'abonnement** : doit sentir premium, iPhone, pas un formulaire admin.

## 2. Critère de réussite — UN SEUL
> **Un inconnu ouvre l'app → en 10 secondes il sait : à quoi ça sert / quoi faire en premier / pourquoi rester.**

Si ce critère n'est pas rempli = c'est pas terminé. Aucune autre métrique ne compte plus que celle-là.

## 3. Ce que tu as le droit de faire (différent des prompts précédents)
- **Créer de nouveaux fichiers** de structure (layout, navigation, onboarding, univers/espaces).
- **Modifier les routes** de navigation (regrouper sous un univers, fusionner les deux accueils) → sans casser les imports des écrans existants.
- **Écrire un premier lancement** (onboarding léger, 1 à 3 écrans max : qu'est-ce que c'est / quel est ton métier / ta première action) — vu **une seule fois**, jamais revu.
- **Refondre l'écran Accueil** (le vrai tableau de bord vivant : héros = l'action urgente du jour, rangées = les univers accessibles).
- **Refondre l'écran Abonnement** : il doit sentir la valeur, pas le back-office.
- **Réorganiser la section Argent** : la rendre cohérente de bout en bout (flux : devis → encaissé → bilan → que faire maintenant).

## 4. Ce que tu n'as PAS le droit de faire
- Réécrire les écrans métier existants (devis, chantier, compétences…) — juste les **raccrocher**.
- Toucher au schéma Supabase / Edge Functions / prix / sécurité.
- DROP destructif ou migration non réversible.
- Dire « c'est bon » sans build vert + preuve sur l'écran live.
- Gadget de mouvement qui casse la perf (< 2 s premier rendu, 60 fps, `prefers-reduced-motion` respecté).
- Mettre « IA » ou jargon en façade — l'IA est invisible, seul le résultat compte.

## 5. Phase 0 — Audit d'ossature (STOP après, attends mon OK)
Dresse le tableau suivant pour chaque écran réel :

| Écran | Route actuelle | Univers logique | Problème de squelette | Correctif proposé |
|-------|---------------|----------------|----------------------|-------------------|

Puis propose :
1. **L'arbre cible** : `Ouverture (1er lancement) → Accueil (maison unique) → [Univers A] → [Univers B]…`
2. **Le plan de fusion** des deux accueils (quelle page devient la maison, qu'est-ce qu'on redirige).
3. **La refonte Argent** : quel est le flux logique à l'intérieur ?
4. **La refonte Abonnement** : qu'est-ce qui doit changer pour sentir premium ?

**STOP. Attends mon « OK, vas-y »** — surtout sur : quelle page devient la maison unique et quels univers.

## 6. Ensuite — une étape à la fois
1. **Ouverture + maison unique** (la fusion des deux accueils + accueil vivant héros/rangées).
2. **Regroupement par univers** (navigation cohérente web + mobile).
3. **Argent — cohérence interne** (flux devis → encaissé → bilan).
4. **Abonnement premium** (refonte sentiment de valeur).
5. **Polish** (transitions, cascade, micro-interactions) — seulement après que le squelette est solide.

Chaque étape = build vert + commit + URL à tester + preuve du critère « l'inconnu comprend en 10 s ».

## 7. Definition of Done finale
- Un inconnu (pas toi, pas Adama) ouvre l'app → comprend en 10 s. **C'est tout. C'est le seul juge.**
- La navigation est identique web et mobile.
- « Argent » a un flux logique de bout en bout.
- L'abonnement donne envie — il ne fait pas « back-office ».
- Build vert, tests verts, zéro régression sur les données utilisateurs existantes.

**Commence par la Phase 0. STOP. Attends mon « OK, vas-y ».**
