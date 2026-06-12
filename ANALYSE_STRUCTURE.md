# AK UNIVERS — Analyse de structure (atouts / inconvénients)

> **Date : 2026-06-12** · Vue du consultant après lecture des docs de fond (`PROMPT_FINITION_AK_UNIVERS.md`,
> `KOITA_STRATEGY.md`, `ETAT_AVANCEMENT.md`) + tout l'historique de build (cœur métier, base, monétisation).
> **Grille de lecture** : la vision = **moteur universel des tâches répétitives / routines de CHAQUE métier** (le BTP = 1er métier prouvé).
> ⚠️ Le code de l'app n'est pas lisible depuis ce repo (il vit dans `AK_Digital_BTP`/Antigravity) → certains points sont **à confirmer par un mini-audit de l'agent** (voir fin).

---

## ✅ ATOUTS (la structure sert déjà la vision)

1. **C'est déjà une PLATEFORME, pas une app BTP** : vrai socle (`src/socle`, `MODULES.md`, « un module importe le socle »). Noyau (compte, IA-agents, paiement, Finance/Droit/Financement/Diaspora) **séparé** du BTP → ajouter un métier = greffer un module.
2. **BTP pilote riche (5/5)** : Terrain · Compétences · Argent · Entreprise · Avenir. Ce sont des **routines** (alertes J-30, certifs 90j, relances, obligations) → le moteur de tâches répétitives **tourne déjà**, habillé BTP.
3. **Multi-plateforme dès le départ** : 1 noyau, façades Web / PWA / Bots, même Supabase → « toutes les portes d'Internet ».
4. **« Pas passif » déjà planifié** : squelettes des autres modules (Services à domicile, Transport, Créateur) + « Bientôt » → se lit multi-métiers.
5. **Double marché intégré** : mobile money (Wave/CinetPay) + Stripe + fuseaux FR/AOF.
6. **Noyau prouvé** (session 11-12/06) : sécurité RGPD, intégrité, monétisation, **marge IA 96-98 %**.

---

## 🔴 INCONVÉNIENTS / risques (vs la vision universelle)

1. **🎯 Le « moteur de routines » universel n'est pas encore un concept GÉNÉRIQUE et central** : routines/alertes câblées **par métier** (BTP). Pas encore (à confirmer) de système générique « mes tâches récurrentes » configurable par tout métier sans code. **C'est l'âme de la vision, encore incarnée dans le BTP, pas abstraite.**
2. **Universalité prête en archi mais NON prouvée** : tout repose sur 1 métier. Le vrai test = brancher un 2e métier.
3. **IA non activée** (pas de clé) → « moteur qui agit » en règles seulement ; « AK comprend ton métier » attend la clé.
4. **Risque de DISPERSION** = risque n°1 de la propre stratégie d'Adama (contre-mesure : « 1 focus par trimestre »). Beaucoup de surface.
5. **Pas encore lançable** : finition qualité 2026 + PWA mobile à faire, clés (paiement/IA) à poser.
6. **Personas non précisés** (Fatou/Karim) → qui est le 2e métier cible ?

---

## 🧭 Le crux stratégique

> L'app est **déjà une plateforme universelle bien née** ; le BTP la prouve richement. **Mais le « moteur de routines universel » vit DANS le BTP — il n'est pas encore EXTRAIT en système générique réutilisable par tout métier.**
>
> Deux chantiers de fond : **(1)** rendre le moteur de routines **générique et central** (le héros du produit) ; **(2)** le **prouver sur un 2e métier**. Mais — discipline anti-dispersion — **d'abord finir + lancer le BTP** (revenus + retours réels qui guideront le moteur universel).

---

## ❓ À confirmer par l'agent (mini-audit code, zéro code écrit)
1. Notion **générique** de routine/tâche récurrente/échéance réutilisable par tout métier, ou recodée dans le BTP ?
2. L'onboarding (`type_profil`/`sous_profil`) propose-t-il **plusieurs métiers** ? Que voit un user **non-BTP** ?
3. Le socle (`src/socle`) : qu'expose-t-il, est-il **métier-agnostique** ?
4. Les agents (`agentsBilan`) : règles BTP en dur ou **configurables par métier** ?

---

## ✅ RÉSULTAT DU MINI-AUDIT (2026-06-12) — la vision universelle est à ~80%

**Verdict : DEUX moteurs de routines coexistent (un générique, un BTP) — il faut les fusionner.**

| Question | Réponse |
|---|---|
| 1. Moteur générique de routines ? | 🟠 **Partiel** : `lib/recommandations.js` (Sprint 16) est **déjà générique/cross-portail** ; mais `lib/agentsBilan.js` est **BTP en dur** + aucune table « tâche récurrente » (chaque alerte recodée ad-hoc). `certifs.js` générique mais sous-utilisé. |
| 2. Onboarding multi-métiers ? | ✅ **OUI, déjà universel** : `lib/portails.js` = 6 portails × 5 profils, plein de non-BTP (commerce, transport, ménage, salarié, diaspora, URSSAF…). **BTP = 1 profil sur 5.** L'entrée est générique, **l'atterrissage non** (cf. Q4). |
| 3. Socle métier-agnostique ? | 🟠 **Majoritairement**, mais bundle des défauts BTP (seeds catalogue Élec/Réseau/CCTV + exporte `agentsBilan` comme s'il était transverse). |
| 4. Agents (`agentsBilan`) configurables ? | ❌ **BTP EN DUR** (devis/chantiers/habilitations). Un non-BTP voit quand même « Agent Chantier ». C'est ce moteur qui alimente **le héros de l'accueil**. |

**Le levier (effort Moyen, AUCUNE migration BDD)** : **fusionner `agentsBilan` dans le modèle déjà-générique de `recommandations.js`** (scopé portail) + généraliser `certifs.js` aux échéances → **UN seul moteur de routines paramétrable par métier**. Bonus : le **héros d'accueil devient universel** automatiquement (montre les bons agents selon le métier).

**Timing** : ne bloque PAS le lancement BTP (1ers users = BTP). Mais c'est **l'âme de la vision + enlève une dette (doublon)** → bon candidat comme **fondation de la Gen 2**. *(Plan d'unification détaillé à demander à l'agent.)*

---

## 🔧 PLAN D'UNIFICATION (agent, 2026-06-12) — « un seul moteur d'échéances, deux vues »

**Idée** : remplacer le code impératif (80 lignes/alerte) par une **liste de DÉTECTEURS déclaratifs** (1 fiche de config par routine : `id, portail, agentKey, table+colonnes, secteurs?, detecte(), message(), route/cta/priorite, seuilJours?`). → **Ajouter une routine pour un nouveau métier = 1 ligne de config**, pas un nouveau moteur. `certifs.js` = primitive d'échéance unique.
- **Architecture** : `moteurEcheances.js` (1 scan batché) → `signaux[]` → 2 vues (`vueAgents` pour AgentsNuit / `vueRecos` pour PourToi).
- **Sans risque** : lecture seule, **aucune migration BDD**, **Phase 0 = test de non-régression** (fige la sortie actuelle). Effort **~1-1,5 j**.
- **Phases** : P0 test filet → P1 extraire moteur+détecteurs (transcription fidèle, dédup) → P2 brancher les 2 vues + supprimer le doublon.

**Décisions tranchées (Adama, 2026-06-12)** :
1. **Garder les 2 surfaces** (Agents + Pour toi) **avec anti-redondance** (un signal = 1 fois). *(voir mockup ASCII avant de figer)*
2. **OUI, filtrer par métier** : un non-BTP ne voit plus les agents Chantier/Juridique. ← cœur de la vision universelle.
3. **Suppression franche** des vieux moteurs (grep = 0 import externe + test P0 en filet).

→ **C'est le geste qui rend l'app fidèle à son nom : AK Univers, pas AK BTP.**
