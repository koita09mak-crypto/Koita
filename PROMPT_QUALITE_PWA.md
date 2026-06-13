# AK Univers — Prompt QUALITÉ 2026 + PWA (app installable, zéro casse)

> À coller dans Claude Code (Antigravity), session sur `AK_Digital_BTP`.
> But : hisser chaque écran au niveau d'une app moderne 2026 ET rendre l'app installable sur téléphone (PWA),
> sans rien casser. Format : audit écran par écran → STOP.
> Vient APRÈS : simplification ✅, mode démo ✅, landing + prix ✅, cockpit/sécurité des rôles ✅.

---

Tu es un ingénieur produit senior (design + front + perf, école Apple : « it just works », la constance plutôt que l'effet ponctuel).
Tu reprends une app RÉELLE et SAINE (AK Univers), en production. Lis TOUT. **Ne code RIEN avant mon « OK, vas-y ».**

## 0. Ce qui est acté (ne ré-audite pas, ne casse pas)
- AK = plateforme multi-métiers ; BTP = module pilote complet. IA INVISIBLE (on montre le résultat, pas la techno).
- Déjà fait et prouvé : simplification (menu universel), mode démo, landing + prix (lus depuis `plans.js`), sécurité des rôles/cockpit (RLS, AdminGuard, is_admin).
- Le système de couleurs `COLORS` + les composants existants (StatCard, EmptyState…) sont TA base design → tu les RÉUTILISES.
- INTERDIT : refonte destructive, déplacement massif de fichiers, casser une route/un import, toucher au schéma Supabase / aux Edge Functions / aux prix / à la sécurité des rôles.

## 1. Objectif — deux livrables
A. QUALITÉ 2026 : hisser chaque écran au niveau d'une app moderne, SANS rien casser.
B. PWA : rendre l'app INSTALLABLE sur téléphone (Android/iPhone), même codebase, même Supabase — PAS d'app native séparée.

## 2. Méthode obligatoire (pas de big-bang)
- PHASE 0 — AUDIT, puis STOP. Parcours chaque écran réel et dresse un tableau :
  | Écran | États (vide / chargement / erreur) OK ? | Design cohérent ? | Mobile OK (pouce, ≥44px, pas de scroll horizontal) ? | Perf (<2s) ? | Données réelles (zéro « lorem ») ? | Verdict | Correctif |
- Puis un PLAN PRIORISÉ : d'abord le cassé/bloquant, puis la cohérence, puis le polish.
- UNE étape à la fois : build vert + commit dédié + tu me dis quel écran/URL je peux tester.
- Règle de vérité : jamais « c'est bon » sans le tableau « existe / manque » prouvé dans le code réel.

## 3. Definition of Done — standard « app 2026 » (chaque écran livré coche TOUT)
États (jamais de page blanche) :
- Vide : message + UNE action concrète (« Créer ton premier devis »).
- Chargement : SKELETON, pas un spinner nu.
- Erreur : message humain + bouton « réessayer ».
- Succès : feedback immédiat (toast / coche).
Design : un seul système (COLORS, espacements, rayons, typo) ; une SEULE action principale par écran ; de l'air, pas un mur de texte.
Fluidité : premier rendu utile < 2s ; lazy-load des écrans lourds ; feedback < 100ms au tap.
Mobile-first : tout au pouce, cibles ≥ 44px, pas de scroll horizontal, safe-areas.
Langage : ton du métier, zéro jargon technique ; chaque bouton dit ce qu'il fait.
Cohérence : même composant = même apparence PARTOUT.

## 4. PWA (livrable B)
- Manifest : nom (« AK Univers »), icônes (toutes tailles), couleur de thème, affichage plein écran, écran de démarrage.
- Service worker : cache léger pour un chargement rapide et un offline minimal (l'app s'ouvre même réseau faible) — sans casser les données live (tout lit le MÊME Supabase).
- Résultat : l'utilisateur peut « Ajouter à l'écran d'accueil » sur Android ET iPhone, et lancer AK comme une app.
- INTERDIT : créer une app native séparée, dupliquer la logique métier.
- Vérifie : installable sur les 3 tailles (téléphone 360px / tablette / desktop), responsive, l'icône et le nom corrects.

## 5. Ce qu'il ne faut JAMAIS faire
- Casser une route, un import, une donnée d'un utilisateur existant.
- Remplacer le système de couleurs (on le réutilise).
- Présenter une fonctionnalité non codée comme si elle marchait.
- Réintroduire l'IA en façade, ou un prix en dur (les prix viennent de `plans.js`).
- Dire « c'est bon » sans build vert + écran testable.

## 6. Livrable
- Phase 0 : le tableau d'audit qualité + le plan priorisé → montre-le-moi, puis ATTENDS mon OK.
- Ensuite, une étape à la fois : build vert + commit + écran/URL à tester.
- À la fin : récap « avant/après » par écran + confirmation « PWA installable » (capture de l'app sur l'écran d'accueil d'un téléphone).

**Commence par la PHASE 0 (le tableau d'audit). STOP après. Attends mon « OK, vas-y ».**
