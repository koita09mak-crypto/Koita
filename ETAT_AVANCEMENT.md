# AK Univers — État d'avancement

> **Mis à jour : 2026-06-11**
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

## 4. Après le pilote — ⬜ DERNIÈRE LIGNE DROITE
- [ ] Passe de finition qualité 2026 (le gros prompt) : états, perf, cohérence sur toute l'app
- [ ] PWA / mobile : manifest + service worker → app installable Android/iPhone
- [ ] Squelettes des autres modules (Services à domicile, Transport, Créateur) : entrée + « Bientôt disponible »
- [ ] Config des clés : `.env.example` documenté (Supabase, Stripe, Wave, CinetPay, IA)
- [ ] Bots / canaux (Discord/Telegram/WhatsApp) — `replit_bot.py` comme base

---

## 🎯 Où on en est
- Fondations + noyau = **✅ faits**
- Pilote BTP = **✅ 5/5 COMPLET**
- Prochaine étape : finition qualité 2026 + mobile (PWA) → pour rendre l'app « payable »

## Décisions métier actées (rappel)
- KPI fiscal = **ENCAISSÉ** (base URSSAF / plafond micro), pas le facturé. *(2026-06-11)*
- Décennale / RC Pro stockées sur `profils` (pas de table assurances dédiée). *(2026-06-11)*
- Financement = brique du **socle**, consommée par les modules, jamais enfermée dans le BTP. *(2026-06-11)*
