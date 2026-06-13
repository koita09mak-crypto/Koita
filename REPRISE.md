# 🔄 REPRISE — Par où on reprend (snapshot 2026-06-13, nuit)

> **À lire en PRIORITÉ en début de session**, avec `KOITA_STRATEGY.md`.
> Ce repo `Koita` = mémoire/stratégie. L'app vit dans le repo **`AK_Digital_BTP`** (séparé).

---

## ✅ Où on en est (l'essentiel)
- 🏛️ **Micro-entreprise DÉPOSÉE** (13/06) — entreprise individuelle, activité **numérique** (Services d'information / hébergement de données), nom commercial **AK Univers**, forme commerciale (BIC ~21 %), versement libératoire Non. N° formalité J00250658754. → **SIRET en attente** par email.
- 📱 **App SaaS `AK_Digital_BTP` fonctionnelle** : IA réelle (clé Anthropic) + **paiement Stripe (mode test) → abonnement Pro ACTIF** (prouvé). Installable (PWA, Lighthouse 100), sécurité/cockpit OK, landing + prix (Pro 29 €/Équipe 49 €) faits.

---

## 🎯 TRAVAIL EN COURS : CLARTÉ UX du pilote BTP (objectif : compréhensible pour un débutant total / "une enfant de 8 ans")
> ⚠️ **Anti-dispersion (risque n°1)** : UN sujet à la fois, prouvé. **PAS de nouveaux domaines** (créateur/formation/contenu restent « bientôt »). On finit le **pilote BTP**.

### Audit Phase 0 fait par l'agent — findings clés :
- ✅ **Le « + Publier un article » n'est PAS un bug** : il n'apparaît que pour un compte **ADMIN** (le compte fondateur d'Adama). Un **vrai artisan voit « + Nouveau devis »**. → **L'universel marche.**
- 🔔 **Bug CSS** : panneau notifications (340px) déborde de la sidebar (260px) → coupé à gauche.
- 👤 **Manque un menu de compte** (avatar → Mon compte / Abonnement / Déconnexion).
- 🏠 **DEUX accueils** : l'onboarding mène à `/app/:portail/dashboard`, mais l'onglet « Accueil » mène à `/app` → « deux maisons » = la sensation « tout est mélangé ».

### Plan validé — à exécuter DANS L'ORDRE (un à la fois, build vert + commit + capture) :
1. **Corriger le panneau de notifications** (le « coupé »).
2. **Ajouter le menu de compte sur l'avatar** (Mon compte · Abonnement · Déconnexion).
3. **Ajouter l'interrupteur « Voir comme mon métier »** pour l'admin (pour qu'Adama teste la vraie vue BTP).
4. **PUIS : unifier les 2 accueils** — ⚠️ décision à prendre avec Adama (quelle page devient LA maison unique). C'est le cœur du « pas structuré ».

---

## ⏳ Actions terrain (Adama)
- Recevoir le **SIRET** (email, quelques jours).
- ⚠️ **Déposer l'ACRE à l'URSSAF AVANT ~28/07/2026** (via `autoentrepreneur.urssaf.fr` + attestation de demandeur d'emploi France Travail). → Claude guidera dès le SIRET reçu.
- Vérifier la validité du justificatif de **domiciliation** (< 3 mois, à son nom, bonne adresse).

---

## 🧹 Reste technique (non bloquant — plus tard)
- Nettoyer le **webhook Stripe dupliqué** (`dynamic-rhythm`, 100 % erreur) ; **durcir l'idempotence** (clé anti-rejeu après traitement réussi).
- **Wave / CinetPay** (mobile money AOF) — nécessite un **compte marchand** (donc SIRET) ; tester d'abord en **sandbox**.
- **Passage en LIVE** Stripe (clés live + webhook live) + brancher la **remise −30 % fondateurs** (coupon).
- **Légal** : CGU / CGV / RGPD à valider par un juriste. **Domaine** à acheter.
- **Traductions** (FR/EN/WO/AR) incomplètes → polish, plus tard (pas requis pour le marché FR).

---

## 🧭 Rappels stratégiques
- **UNE micro-entreprise FR multi-activités** (numérique d'abord, BTP en 2e activité plus tard via diplôme La Solive OU 3 ans d'expérience). Entité AOF différée.
- **IA invisible** (philosophie Apple), **cible universelle** (tous métiers, BTP = ancre/preuve), **un produit excellent à la fois.**
- Priorité Phase 1 **terrain** (formation, ACRE, immatriculation, réseau AOF) reste ouverte **en parallèle** du digital.
