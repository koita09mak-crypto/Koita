# AK UNIVERS — PLAN DE CONCLUSION (vers la v1 lançable)

> **But** : avoir une **v1 lançable** = un produit qui (a) fait le **WOW** (la boucle qui relie les domaines),
> (b) est **propre/moderne**, (c) est **configuré et légal**, (d) est **en ligne**.
> Méthode inchangée : **un pas à la fois, prouvé, build vert.**

---

## ✅ DÉJÀ FAIT (socle solide, 11-12/06)
- **Accueil** refondu (3 zones, héros agents, honnête).
- **Cœur métier** : devis/factures multi-taux conformes, clients, paiement — **prouvé sur du réel**.
- **Base Supabase** auditée + assainie (V0 sécurité · V1 intégrité/FK · V2 nettoyage · V3 RGPD/suppression compte · V3b fuseaux).
- **Monétisation** complète (M0 marge IA blindée 96-98% · M1 factures plafonnées · M2 routage Haiku · M3 flux paiement prouvé · M4 cleanup).
- **Moteur universel unifié** (1 moteur de routines, filtre par métier) → **AK est universel**.
- **Vision** : 8 domaines définis + **la boucle vertueuse** + persona n°1 (Adama).
- **Boucle — Étape 1 FAITE** : chantier fini → contenu (1er maillon).

---

## ⬜ CE QUI RESTE POUR CONCLURE (dans l'ordre)

### Bloc 1 — Finir LA BOUCLE (le WOW) 🎯 *priorité produit*
- [ ] **Étape 2** : compétence/certif qui expire → **formation financée (CPF)** → certif.
- [ ] **Étape 3** : travail → **CV auto-rempli** (chantiers/devis) → missions.
- [ ] (plus tard) autres connexions des 8 domaines, au fil de l'usage.
→ *Chacune = 1 détecteur, 0 migration, prouvée, s'affiche sur l'accueil.*

### Bloc 2 — Finition qualité + mobile 📱
- [ ] **Passe qualité 2026** (états vides/chargement/erreur, perf, cohérence) — cf. `PROMPT_FINITION_AK_UNIVERS.md`.
- [ ] **PWA** : manifest + service worker → app **installable** Android/iPhone.

### Bloc 3 — Config & légal (côté Adama, peu/pas de code) ⚙️
- [ ] **Clés API** : Stripe/Wave/CinetPay (paiements réels) + `ANTHROPIC_API_KEY` (IA réelle). Voir `docs/PAIEMENT_ACTIVATION.md`.
- [ ] **Légal (couches B+C du droit)** : CGU, CGV, confidentialité, RGPD → **valider par un juriste**.
- [ ] **Activations** : `RESEND_API_KEY`, Supabase « Confirm email » OFF, toggle leaked-password.
- [ ] **Nettoyage final** : `supabase functions delete tmp-diagnostics` + domaine (LANCEMENT.md).
- [ ] **Décisions prix** : limites du gratuit · prix Pro (19 € vs 29 € codé) · mobile money prioritaire.

### Bloc 4 — LANCER 🚀
- [ ] Mise en ligne (domaine) + premiers utilisateurs (toi d'abord = test, puis BTP).

---

## L'ordre conseillé
**Bloc 1 (la boucle = le wow)** → **Bloc 2 (qualité + mobile)** → **Bloc 3 (config + légal)** → **Bloc 4 (lancer)**.
> On finit le **wow** d'abord (ce qui rend l'app unique), puis on **polit**, puis on **branche les clés**, puis on **ouvre les portes**.

---

## 🔭 PÉRENNITÉ — angles morts FUTURS à anticiper *(réflexion fondateur Adama, 2026-06-13)*
> Principe : **anticiper (noter + architecturer proprement), ne pas tout construire maintenant.** Bâtir pour aujourd'hui, laisser des accroches propres pour demain.

| Angle mort futur | État | Action |
|---|---|---|
| **Rôles & permissions** (fondateur/admin vs user vs membre d'équipe) | à vérifier | mini-audit rôles (admin en dur ? /app/admin bloqué pour un user ? rôle équipe prêt ?) ← **le plus immédiat** |
| **Sécurité/RGPD à l'échelle** | RLS solide ✅ | valider le légal (CGU/RGPD, couches B/C) par un juriste **avant de scaler** |
| **Mises à jour sans casser les users** | discipline migrations ✅ | garder : migrations versionnées, tests, prouver avant push |
| **Le wow à l'échelle** (nouveau user comprend en 3 s) | en cours (simplif + démo) | mode démo + onboarding par métier |
| **Paiement réel à l'échelle** (échecs, remboursements, relances) | rails posés ✅ | gérer les cas limites au lancement |

> ✅ Bonne nouvelle : la base est **architecturée pour grandir** (base propre, RLS, moteur universel, migrations disciplinées).
