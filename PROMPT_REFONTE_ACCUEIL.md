# AK Univers — Refonte ACCUEIL & navigation (clarté + différenciation)

> À coller dans Claude Code (Antigravity), session fraîche sur `AK_Digital_BTP`.
> But : faire RESSORTIR la promesse d'AK et désencombrer — sans rien casser.

---

Tu es un designer produit senior (style Apple : focus, hiérarchie, « it just works »).
Lis TOUT. **Ne code RIEN avant mon « OK, vas-y ».**

## 0. Le problème à résoudre
L'accueil actuel montre TOUT en même temps (héros, 5 agents, 8 cartes « Que veux-tu faire »,
Formation, Emploi, parrainage, citation… + ~15 items de barre latérale). Résultat : ça ressemble
à un **dashboard générique**, la différence d'AK ne ressort pas, et l'utilisateur **CHERCHE au lieu
d'AGIR**.

Objectif : refondre l'**ACCUEIL** et la **NAVIGATION** pour incarner la promesse, **sans supprimer
aucune fonctionnalité**. On ne retire pas de modules : on **réorganise la hiérarchie** et on **enlève
le bruit**.

## 1. La promesse à incarner (north star)
« Tout ce qui est répétitif, long ou compliqué, AK le fait à ta place — et t'apprend ce que tu ne
maîtrises pas — pour que tu avances. » → **faciliter.**
L'accueil doit faire **ressentir ça en 5 secondes.**

## 2. Principes (Apple)
- **UNE** chose principale par écran, une action évidente.
- Montrer peu, **révéler le reste au besoin**. De l'air.
- Chaque tap mène quelque part de **précis** (jamais « Explorer → » vague).
- On **enlève**, on ne rajoute pas.

## 3. PHASE 0 — Audit (puis STOP)
Liste ce que l'accueil affiche aujourd'hui (chaque bloc) + les items de navigation, et propose :

| Bloc / item actuel | Héros · Reléguer · Regrouper · Masquer | Pourquoi |

Puis montre-moi la **maquette texte** du nouvel accueil + de la nouvelle navigation. **Attends mon OK.**

## 4. Cible — Nouvel ACCUEIL (3 zones max)
1. **HÉROS = « Ce qu'AK a fait pour toi »** : les AGENTS (Devis / Commercial / Chantier / Juridique /
   Support) et ce qu'ils ont traité pendant que tu bossais. C'est LA différence → **en premier, en grand.**
2. **« À faire aujourd'hui »** : 2-3 actions qui comptent vraiment (ex : SIRET manquant, devis à
   relancer). Pas une liste infinie.
3. **« Apprendre / avancer »** : 1 entrée formation + 1 vers les autres modules. Discret.

Le reste (parrainage, citation Foi & Travail, sélecteur de langues) : **gardé mais secondaire**,
pas dans la figure.

## 5. Cible — Navigation dégraissée
~15 items = trop. **Regroupe** en quelques sections claires (ex : *Mon activité* · *Mes finances* ·
*Apprendre* · *AK Univers*). Montre l'essentiel, le reste en sous-niveau. **Garde toutes les
destinations**, réduis seulement la charge visuelle.

## 6. Règles
- Réutilise `COLORS` + les composants existants (StatCard, EmptyState…). Cohérence totale.
- **Ne casse aucune route ni fonctionnalité** : tu changes la PRÉSENTATION et la HIÉRARCHIE, pas la logique.
- Mobile-first. États vides propres. Aucune donnée fictive.
- Build vert + commit dédié. Jamais « c'est bon » sans preuve.

---

**Commence par la Phase 0** (tableau + maquette texte de l'accueil et de la nav), puis attends mon « OK, vas-y ».
