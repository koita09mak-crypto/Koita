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
