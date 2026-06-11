# Mission MONÉTISATION — carte de travail

> **Objectif** : faire payer AK Univers **sans tuer l'acquisition**.
> **Principe (north star)** : on fait payer pour la **valeur** (le difficile/répétitif fait à ta place + la conformité + se faire payer), **pas** pour « un outil de plus ».
> Statut : **à structurer AVANT de coder.** La RLS « équipe » suit le design des paliers (décision actée : équipe = OUI, gated abonnement).

---

## 1. La logique d'ensemble (freemium → premium)

1. **On fait entrer** facilement (l'inscription sans friction qu'on a construite = « essai en 30 s »).
2. **On fait goûter** la vraie valeur (créer de vrais devis/factures conformes).
3. **On convertit** quand l'utilisateur atteint une limite ou veut une fonction premium (agents illimités, équipe…).

> Règle d'or BTP : **ne jamais dégrader le document** (pas de filigrane sur un devis/facture) — la conformité EST la valeur. On limite le **volume** ou les **fonctions**, jamais la qualité du document.

---

## 2. Les 3 paliers proposés (à valider/ajuster)

| | **Découverte (gratuit)** | **Pro (solo, payant)** | **Équipe (premium)** |
|---|---|---|---|
| Cible | Tester, se rassurer | L'artisan seul, cœur de cible | TPE/PME, plusieurs personnes |
| Devis / factures | **limités** (ex. X/mois) | **illimités** | illimités |
| PDF conformes (TVA, SIRET) | ✅ | ✅ | ✅ |
| Agents IA | **basiques** | **tous** | tous |
| Suivi paiement / relances | basique | complet | complet |
| Utilisateurs | 1 | 1 | **plusieurs (rôles, partage)** |
| Rapports / pilotage | — | simple | avancé |
| Formation / modules | aperçu | inclus | inclus |

→ **L'équipe est le déclencheur premium** (ta décision) : « tu veux bosser à plusieurs ? → offre Équipe ».

---

## 3. Le double marché (France + Afrique de l'Ouest)

Le **même produit**, mais **deux réalités de prix et de paiement** :

| | France | Afrique de l'Ouest |
|---|---|---|
| Pouvoir d'achat | standard SaaS | **plus faible** → prix adaptés |
| Concurrence repère | Tolteck/Obat (~30-50 €/mois) → AK doit être **accessible** | peu d'équivalents → **avantage** |
| Paiement | carte (Stripe) | **mobile money** (Wave, Orange Money, MTN…) + annuel |
| Conformité | RGPD + TVA FR | à cadrer par pays |

→ Prévoir une **grille de prix par zone** (pas un prix unique mondial).

---

## 4. Les décisions à prendre (les tiennes, Adama)

1. **Limites du gratuit** : combien de devis / factures / clients par mois avant de devoir passer Pro ?
2. **Prix** : Pro en France (€/mois) ? Pro en AOF (FCFA/mois) ? Équipe (par utilisateur ou forfait) ?
3. **Essai** : en plus du gratuit, un **essai Pro de X jours** (14 ?) puis retour au gratuit ?
4. **Remise annuelle** (ex. 2 mois offerts) pour fidéliser et encaisser d'avance ?
5. **Paiement** : Stripe (France) + quel(s) mobile money (AOF) en priorité ?
6. **Le déclic d'upgrade** : quel message quand on atteint la limite gratuite ?

---

## 4 bis. Grille de prix recommandée *(proposée par le consultant — à valider/ajuster par Adama)*

> Logique : **accessible** (challenger sous les concurrents FR ~29-39 €/mois) + **adaptée à l'AOF** (mobile money, pouvoir d'achat — on n'applique PAS le prix français converti). Prix simples et prévisibles.

| Palier | France 🇫🇷 | Afrique de l'Ouest 🌍 | Contenu |
|---|---|---|---|
| **Découverte** | Gratuit | Gratuit | 3 devis + 3 factures/mois · 5 clients · agents basiques · 1 user |
| **Pro** | **19 €/mois** (ou 190 €/an) | **5 000 FCFA/mois** (ou 50 000/an) | Tout illimité · tous les agents · 1 user |
| **Équipe** | **49 €/mois** (ou 490 €/an) | **12 000 FCFA/mois** (ou 120 000/an) | Jusqu'à 5 users · partage/rôles · rapports avancés |

- **Essai** : 14 jours Pro complet à l'inscription → retour au gratuit si pas d'abonnement.
- **Annuel** : 2 mois offerts (encaisse d'avance + fidélise).
- **Lancement** : « Membres fondateurs » — prix réduit garanti pour les 100 premiers (amorce + bouche-à-oreille).
- **Paiement** : France → Stripe (carte/SEPA) · AOF → mobile money (Wave + Orange Money via agrégateur PayDunya/CinetPay) — **commission, pas d'abonnement** (compatible budget 200 €).

**À confirmer par Adama** : (1) limites exactes du gratuit (3 ou 5 devis ?) · (2) prix Pro (19 / 24 / 15 ?) · (3) mobile money prioritaire (Wave ?).

---

## 4 ter. Contrôle des coûts IA — protéger la marge ⚠️

**Risque identifié (Adama, 2026-06-11)** : si l'IA coûte plus cher que le prix payé, on perd de l'argent — critique avec un budget de 200 €.

**Réalité** : une action IA avec un petit modèle = fraction de centime à ~2 cts. Un user actif ≈ **1-3 €/mois** de coût IA → marge confortable sous un Pro à 19 €.

**Les 4 protections (par design) :**
1. **Petit modèle économique** (type Haiku) pour le routinier ; gros modèle réservé au critique.
2. **Agents "repère" = règles côté client (sans LLM) → coût ZÉRO** → peuvent rester sur le gratuit.
3. **IA générative (coûteuse) = derrière le paywall (Pro+)** → le coût suit le revenu.
4. **Limites fair-use par palier + plafond serré sur le GRATUIT** (les users gratuits = pure dépense).

**Règle** : le coût IA d'un user doit toujours rester **sous son prix**. À prouver avant de coder (chiffrage par palier).

### ✅ Marge PROUVÉE (audit agent, 2026-06-11, sur vrais chiffres)
- Prix API Claude réels + plans existants de l'app (Free / Pro 29 € / Business 79 € / Enterprise 299 €) + quotas (Free 5k / Pro 50k / Business 200k / Enterprise ~1M tokens/mois).
- **Pire cas (quota 100 % consommé sur Opus, le + cher)** : Pro coûte **0,55 €** d'IA pour 29 € → **marge 98 %** (96 % en FCFA). Business 2,21 € → 97 %. **Le coût IA est ~50× sous le prix.**
- Protections **déjà en place** : quota + plafond serveur (bloque avant l'appel) + `max_tokens=1024` + agents « repère » en règles (0 LLM).
- **⚠️ Seul vrai risque** : comptage de tokens « best-effort » → si l'incrément échoue, un user peut dépasser sans être décompté. **À blinder en priorité** (fiabiliser le comptage).
- **🔧 Levier** : défaut = Opus (cher) partout → router le routinier vers **Haiku** (5× moins cher).
- **💡 Opportunité** : quotas trop chiches (~21 actions/mois sur Pro) → quadruplables en restant à 92 % de marge → meilleure UX/rétention. Le frein n'est pas le coût.
- *Décision prix ouverte* : garder 29 €/79 €/299 € (codé) ou adopter 19 €/49 € (plus agressif). Les deux ultra-rentables.

---

## 5. Ordre de construction (structurer d'abord)

1. **Décider** les paliers + prix + limites (section 4) — *toi*.
2. **Modéliser** : la table `subscriptions` existe déjà → définir les plans (free/pro/équipe) proprement.
3. **Câbler les limites** (gating) côté app : bloquer/inviter à upgrader selon le plan.
4. **Brancher le paiement** (Stripe d'abord, mobile money ensuite).
5. **RLS Équipe** : implémenter le partage org **selon le design des paliers** (pas avant).

> Chaque étape : plan d'abord → prouvé → un chantier à la fois. Comme tout le reste.

---

## 6. Budget de départ (rappel)

Démarrage à **200 €** → privilégier des outils **gratuits/peu chers** (Stripe = commission, pas d'abonnement ; mobile money = commissions). Pas d'outil payant superflu avant d'avoir des revenus.
