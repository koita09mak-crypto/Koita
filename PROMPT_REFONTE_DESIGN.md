# AK Univers — Prompt REFONTE DESIGN & STRUCTURE (ressenti « vraie app » Apple/Netflix, zéro casse)

> À coller dans Claude Code (Antigravity), session sur `AK_Digital_BTP`.
> But : faire passer AK Univers de « un menu + des tableaux » à une **VRAIE app** — claire, structurée par univers, vivante et dynamique
> (le niveau Apple / Netflix / Amazon), **sans rien casser**. Format : audit d'architecture → STOP.
> Vient APRÈS : simplification ✅, mode démo ✅, landing + prix ✅, cockpit/sécurité ✅, qualité 2026 + PWA ✅, **menu de compte (Mon compte · Abonnement · Déconnexion) ✅**.

---

Tu es un **directeur artistique produit + ingénieur front senior** (école Apple : « it just works », la constance plutôt que l'effet ponctuel ; sens de la hiérarchie de Netflix ; clarté d'Amazon).
Tu reprends une app RÉELLE et SAINE (AK Univers), en production. Lis TOUT. **Ne code RIEN avant mon « OK, vas-y ».**

## 0. Ce qui est acté (NE ré-audite pas, NE casse pas)
- AK = plateforme multi-métiers ; **BTP = module pilote complet**. **IA INVISIBLE** (on montre le résultat/produit, jamais la techno — vaut PARTOUT, façade comprise).
- Déjà fait, prouvé, intouchable : menu universel par métier, mode démo, landing + prix (lus depuis `plans.js`), sécurité des rôles/cockpit (RLS, AdminGuard, `is_admin`), qualité 2026 + PWA installable, **menu de compte sur l'avatar (Mon compte · Abonnement · Déconnexion)**.
- Le système de couleurs `COLORS` + les composants existants (StatCard, EmptyState, BottomTabBar…) sont **TA base design → tu les RÉUTILISES et tu les élèves**, tu ne les remplaces pas.
- **INTERDIT** : refonte destructive, déplacement massif de fichiers, casser une route / un import / l'auth / une donnée utilisateur, toucher au schéma Supabase / aux Edge Functions / aux prix / à la sécurité des rôles. **AUCUN nouveau domaine métier** (créateur/formation/contenu restent « bientôt » — anti-dispersion = risque n°1).

## 1. Le problème à résoudre (mots d'Adama)
« Ça ressemble encore à **un simple menu + des tableaux**. Je veux une **VRAIE app** : Apple / Netflix / Amazon. »
Traduction produit — 3 manques concrets :
1. **Structure plate** : tout est au même niveau, rien n'est *regroupé par univers cohérent* (ex. une zone « Activité » qui réunit ce qui va ensemble). → manque une **architecture d'information** lisible.
2. **Deux maisons** : l'onboarding mène à `/app/:portail/dashboard`, l'onglet « Accueil » mène à `/app` → sensation « tout est mélangé, où est la maison ? ». ⚠️ **C'est LE cœur du « pas structuré ».**
3. **Statique** : aucune **vie** (pas de hiérarchie visuelle forte, pas de mouvement, pas de mise en avant). Une app moderne *respire et réagit*.
4. **Ça ne s'explique pas** : un nouvel utilisateur n'a aucun moment où il comprend **à quoi sert l'app, quoi faire en premier, ce que ça lui apporte**. Il arrive et il est perdu. → manque la **clarté du sens** (l'app doit s'expliquer ET se vendre toute seule, pas que la landing).

## 2. Les 3 références, traduites en principes CODABLES (pas du copier-coller)
- **Apple** → *clarté & retenue* : une hiérarchie nette (1 titre, 1 action principale), beaucoup d'air, mouvement **discret et constant** (transitions douces, feedback < 100 ms), jamais de gadget. « Ça marche, c'est calme, c'est beau. »
- **Netflix** → *hiérarchie par rangées* : un **héros** en haut (ce qui compte MAINTENANT pour cet utilisateur), puis des **sections/rangées thématiques** (« Reprendre », « À faire aujourd'hui », « Ton argent »…). On *scanne* la page, on n'est pas noyé.
- **Amazon** → *« next best action »* : la page pousse l'action la plus utile au bon moment (créer un devis, relancer un impayé), avec des **cartes** claires et des entrées rapides.

## 3. Objectif — UNE app, structurée par univers, vivante
A. **UNE maison unique** (résoudre les 2 accueils) : un **Accueil** = tableau de bord vivant et personnalisé (héros + rangées), point de départ unique.
B. **Architecture d'information regroupée** : les écrans existants rangés sous **quelques univers cohérents** (« espaces »), pas une liste plate. (Ex. de regroupement à valider en Phase 0 : **Activité** = terrain/chantiers/planning · **Argent** = devis/factures/dépenses/rentabilité · **Évoluer** = compétences/avenir/CV · **Tout AK** = le reste.) ⚠️ **Les regroupements exacts = à valider avec moi.**
C. **Vie & dynamisme** (sobre, perf) : transitions de page douces, apparition en cascade des cartes au montage, micro-interactions au tap (≤ 150 ms), états animés (skeleton → contenu), header qui réagit au scroll. **Jamais au prix de la perf** (premier rendu utile < 2 s, 60 fps, `prefers-reduced-motion` respecté).
D. **Cohérence totale** : même composant = même apparence PARTOUT ; un seul système (COLORS, espacements, rayons, typo, ombres) ; navigation identique web & mobile (BottomTabBar mobile, sidebar desktop).
E. **GUICHET UNIQUE** (exigence n°1 d'Adama — la rigueur) : AK Univers = **UNE seule porte d'entrée stricte et cohérente** d'où **tout** part. Les autres métiers/domaines sont **accessibles depuis ce guichet unique** (cohérent avec « une seule entité multi-activités »), **montrés** (visibles) mais **jamais vendus comme finis** : BTP = pilote réel, les autres = « bientôt ». Pas deux portes, pas deux logiques — une seule, stricte.
F. **L'APP S'EXPLIQUE ET SE VEND TOUTE SEULE** : en quelques secondes, un nouvel utilisateur comprend **à quoi ça sert, quoi faire en premier (1 action évidente), ce que ça lui apporte**. Le sens/la valeur est **lisible partout dans l'app**, pas seulement sur la landing (premier lancement guidé, états vides qui pointent le but, libellés qui parlent bénéfice). Niveau Apple/Amazon : l'utilisateur n'a **pas besoin qu'on lui explique** — c'est évident.

## 4. Méthode obligatoire (pas de big-bang)
- **PHASE 0 — AUDIT D'ARCHITECTURE, puis STOP.** Deux livrables :
  1. **Carte actuelle** : tableau de TOUS les écrans réels → `Écran | Route | Univers logique proposé | Niveau hiérarchie (héros/section/détail) | Dynamisme actuel (statique/animé) | Problème | Correctif`.
  2. **Proposition d'architecture cible** : l'arbre « 1 Accueil → N univers → écrans », + le plan pour **fusionner les 2 accueils** (quelle page devient LA maison, ce qu'on garde/redirige sans casser les liens existants).
- Puis un **PLAN PRIORISÉ** : d'abord l'**ossature** (maison unique + regroupement + nav cohérente), ensuite la **hiérarchie visuelle** (héros + rangées), enfin le **mouvement/polish**.
- **UNE étape à la fois** : build vert + commit dédié + tu me dis quel écran/URL je peux tester. Jamais « c'est bon » sans le tableau « existe / manque » prouvé dans le code réel.

## 5. Definition of Done — standard « vraie app 2026 » (chaque étape coche TOUT)
- **Structure** : une seule maison / **un guichet unique** ; chaque écran rangé sous un univers clair ; navigation identique partout ; zéro lien mort après le regroupement.
- **Compréhension immédiate** : un nouvel utilisateur comprend en < 10 s le but + sa 1re action ; la valeur est lisible dans l'app (pas que la landing) ; les autres domaines sont visibles mais marqués « bientôt » (pas vendus comme finis).
- **Hiérarchie** : sur chaque page, 1 chose dominante (héros / action principale), le reste en sections scannables ; pas de mur plat.
- **Vie** : transitions de page + cascade au montage + feedback tap < 100 ms ; `prefers-reduced-motion` honoré ; **0 régression de perf** (< 2 s, pas de saccade).
- **Mobile-first** : tout au pouce, cibles ≥ 44 px, pas de scroll horizontal, safe-areas, BottomTabBar cohérente.
- **États** (jamais de page blanche) : vide (+ 1 action concrète) · chargement (skeleton) · erreur (message humain + « réessayer ») · succès (toast/coche).
- **Langage** : ton du métier, zéro jargon, **zéro mot « IA »** en façade (l'effet se vit, ne s'annonce pas).
- **Cohérence** : COLORS et composants réutilisés et élevés, pas remplacés.

## 6. Ce qu'il ne faut JAMAIS faire
- Casser une route, un import, l'auth, une donnée d'un utilisateur existant, le menu de compte déjà livré.
- Remplacer le système de couleurs ou refondre les composants from scratch (on **réutilise et on élève**).
- Ajouter un domaine/métier non prévu, ou présenter une fonctionnalité non codée comme si elle marchait.
- Réintroduire l'IA en façade, ou un prix en dur (prix = `plans.js`).
- Du mouvement gadget qui tue la perf ou ignore `prefers-reduced-motion`.
- Dire « c'est bon » sans build vert + écran testable.

## 7. Livrable
- **Phase 0** : la carte des écrans + l'architecture cible + le plan de fusion des 2 accueils → montre-le-moi, puis **ATTENDS mon OK** (surtout pour : quelle page devient LA maison, et les regroupements d'univers).
- Ensuite, une étape à la fois : build vert + commit + écran/URL à tester.
- À la fin : récap **« avant/après »** (capture de l'Accueil unique + d'un univers regroupé + une transition), preuve que rien n'est cassé (build + tests verts) et que la perf tient.

**Commence par la PHASE 0 (la carte des écrans + l'architecture cible + le plan de fusion des 2 accueils). STOP après. Attends mon « OK, vas-y ».**
