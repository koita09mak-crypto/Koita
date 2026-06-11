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
