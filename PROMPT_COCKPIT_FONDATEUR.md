# AK Univers — Prompt COCKPIT FONDATEUR & RÔLES (sécurité, zéro cassure)

> À coller dans Claude Code (Antigravity), session sur `AK_Digital_BTP`.
> But : rendre les rôles/sécurité corrects et **prêts au lancement**, avec **ZÉRO cassure** pour l'utilisateur,
> le client payant, le fondateur (Adama) et les clients d'activité. Format : audit/filet d'abord → STOP.
> Vient APRÈS : simplification ✅, mode démo ✅, refonte landing + prix ✅, code promo fondateurs.

---

Tu es un ingénieur back-end + sécurité senior (Postgres/RLS, Supabase, 20 ans d'expérience).
Tu reprends une app RÉELLE en production (AK Univers). Lis TOUT. **Ne code RIEN avant mon « OK, vas-y ».**

## 0. Contexte acté (ne ré-audite pas)
- Base saine, RLS solide, future-ready : flag `profils.is_admin`, fonction `is_ak_admin()`, orgs + rôles équipe déjà prêts.
- Plans/abonnements alignés sur `plans.js` (Gratuit/Pro/Équipe), paiements câblés.
- 3 fragilités connues à corriger ICI :
  1. email codé EN DUR (front `isAdmin()` + 1 RLS `user_analytics`).
  2. route `/app/admin` juste CACHÉE côté client (navigate), pas verrouillée serveur.
  3. Cockpit fondateur FAUX : la RLS ne laisse lire que SA ligne → « 1 inscrit, MRR 0 ». Pas de vue agrégée admin.

## 1. Objectif — corriger les rôles/sécurité avec ZÉRO cassure pour PERSONNE
- L'UTILISATEUR normal voit SES données (devis/chantiers/clients) exactement comme avant — ni plus, ni moins.
- Il ne voit JAMAIS les données d'un autre, ni rien d'AGRÉGÉ (aucune fuite).
- L'ABONNÉ garde son plan/abonnement intact.
- Les MEMBRES D'ÉQUIPE (orgs) gardent leur partage, avec des rôles VALIDES.
- TOI, le FONDATEUR, tu vois enfin le VRAI cockpit (inscrits, MRR, activité) — réservé aux admins.
- Les DONNÉES MÉTIER (les clients que l'artisan gère) restent ISOLÉES par compte, intactes.

## 2. Le plan en 5 points (chacun = 1 étape prouvée, build + tests verts)
1. Le front lit `profils.is_admin` (fin de l'email codé en dur) → 1 source de vérité, multi-admin.
2. RLS `user_analytics` : `is_ak_admin()` au lieu de l'email en dur.
3. `RequireAdmin` sur `/app/admin*` : VERROU SERVEUR (pas un simple redirect client).
4. Cockpit : vue agrégée `SECURITY DEFINER` réservée à `is_ak_admin()` (inscrits, MRR, abonnements, activité).
   ⚠️ PROUVER qu'un user normal ne voit RIEN d'agrégé.
5. CHECK sur `membres_organisation.role` (valeurs valides uniquement).

## 3. Méthode obligatoire — ZÉRO cassure (le plus important)
- PHASE 0 — FILET DE NON-RÉGRESSION AVANT toute modif : écris des tests qui figent le comportement ACTUEL
  pour CHAQUE acteur (user normal, abonné, membre d'équipe, admin). On ne touche à rien tant que le filet n'est pas vert.
- Additif et réversible : migrations VERSIONNÉES, chaque changement RLS/policy/vue est AJOUTÉ proprement,
  jamais un DROP destructif. Retour arrière possible.
- Cette passe A LE DROIT de toucher RLS / policies / une vue SECURITY DEFINER / un CHECK (c'est l'objet).
  Mais RIEN d'autre : pas de refonte, pas de déplacement de fichiers, pas de changement du cœur métier/prix/landing.
- TEST DE FUITE obligatoire : prouver qu'un compte user normal ne voit AUCUNE donnée agrégée ni celle d'un autre compte (avant ET après).
- Une étape à la fois : build vert + tests verts + commit dédié + tu me dis quel écran/URL tester
  (cockpit en admin = vrais chiffres ; cockpit en user normal = rien).

## 4. Definition of Done (norme de lancement)
- Un user normal : exactement ses données, zéro fuite, zéro régression.
- Un admin (moi) : cockpit avec VRAIS chiffres (inscrits, MRR).
- `/app/admin` inaccessible à un non-admin MÊME en tapant l'URL (verrou serveur).
- Rôles d'équipe contraints (CHECK), partage org intact.
- Plus AUCUN email codé en dur ; tout passe par `is_admin` / `is_ak_admin()`.
- Migrations versionnées, tests verts, parité prouvée sur comptes existants.

## 5. Ce qu'il ne faut JAMAIS faire
- DROP destructif / migration non réversible.
- Casser l'accès d'un user existant à SES données.
- Ouvrir la moindre fuite (un user qui verrait l'agrégé ou un autre compte).
- Toucher au cœur métier, aux prix, à la landing.
- Dire « c'est bon » sans le test de non-régression ET le test de fuite verts.

## 6. Livrable
- Phase 0 : le filet de non-régression (tests qui figent l'existant par acteur) → montre-le-moi vert, puis ATTENDS mon OK.
- Ensuite les 5 points un par un : chacun build + tests verts + commit + écran testable.
- À la fin : récap « avant/après » par acteur + confirmation ZÉRO fuite / ZÉRO régression.

**Commence par la PHASE 0 (le filet de non-régression). STOP après. Attends mon « OK, vas-y ».**
