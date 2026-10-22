# Les 4 missions prêtes

Pour chaque mission : les agents dans l'ordre, ce que chaque étape passe à la suivante, et ce que tu rends à la fin. « En même temps » = lance-les en parallèle. Tous les fichiers vont dans le dossier de la mission (`livrables/<aaaa-mm-jj>-<mission>/`).

## 1. Préparer un call

**Phrases** : « Prépare mon call avec Sarah », « je vois Nova demain », « j'ai un rdv à 14 h avec le DG de X ».

1. Cherche dans `calls/` les transcriptions de ce prospect (son nom ou son entreprise dans le nom du fichier ou dans l'en-tête).
2. En même temps :
   - `recherche-fiche-compte` → `fiche-compte.md`
   - `nego-detecteur-objections` sur ses calls passés → `objections.md` (seulement s'il y a des calls passés)
3. `decouverte-prepa-call`, avec `fiche-compte.md`, `objections.md` et ses calls passés → `brief.md`

**Tu rends** : le rappel du brief en 4 lignes, les 2 objections probables, l'objectif du call, et les liens vers les fichiers.

## 2. Trouver de nouveaux clients

**Phrases** : « Trouve-moi de nouveaux clients », « trouve-moi 20 cabinets comptables à Lyon », « remplis mon pipe ».

**Avant** (questions au bon moment, voir `entretien.md`) : la cible visée (si l'utilisateur en a plusieurs et ne précise pas, demande laquelle) ; ses messages qui ont marché, si `gagnants.md` est vide. Nombre de comptes : celui demandé, sinon 10.

1. `strategie-portrait-client`, avec la cible de `mes-cibles.md` → `portrait-client.md` (s'il en existe déjà un récent pour cette cible dans `livrables/`, réutilise-le).
2. `recherche-comptes` → `comptes.md`. Plus de 10 comptes demandés : d'abord un **échantillon** de 5 à 10 comptes, que tu fais valider (voir SKILL.md), puis le reste en excluant les comptes refusés. 10 comptes ou moins : montre la liste complète et fais-la valider de la même façon avant de chercher les décideurs.
3. En même temps :
   - `recherche-decideurs` (avec l'outil d'enrichissement de `mes-outils.md`) → `decideurs.md`
   - `recherche-declencheurs` → `declencheurs.md`
4. `prospection-accroches` → `faits.md` (le bloc de faits de chaque compte).
5. En même temps, avec `faits.md` et `messages-qui-marchent/` :
   - `prospection-email` → `emails.md`
   - `prospection-linkedin` → `linkedin.md`
   Dis-leur que tu fais la liste d'envoi toi-même.
6. Toi :
   - relance `python3 <plugin>/skills/outbound/scripts/verifier_message.py` sur `emails.md` et `linkedin.md` ; si ce n'est pas `OK`, renvoie le fichier à son agent ;
   - une seule liste d'envoi du jour, au format de `<plugin>/skills/modeles/liste-envoi.md` → `liste-envoi.md` (pour LinkedIn : invitation sans note, puis message 1 à J1-J2 après acceptation) ;
   - si des outils sont connectés : `actions-a-valider.md` (créer les contacts dans le CRM, charger la séquence en pause dans l'outil de séquences, créer des brouillons), puis fais-les valider.

**Tu rends** : le nombre de comptes retenus et écartés, les 3 plus prometteurs avec leur signal, le statut des emails (vérifiés, à chercher), le lien vers la liste d'envoi, et les actions faites après validation. Rappelle que c'est l'utilisateur qui envoie, et demande-lui de te dire quels messages obtiennent des réponses.

## 3. Relancer les deals qui dorment

**Phrases** : « Relance mes deals qui dorment », « qui je dois relancer ? », « mes deals sont bloqués ».

Il faut le CRM connecté (dans `mes-outils.md`) ou un export CSV (dans le dossier de travail, ou collé dans la conversation : enregistre-le). Sans l'un ni l'autre, demande l'export en une phrase et attends.

1. `pipeline-rapport` (il lit le CRM connecté lui-même, ou le CSV) → `rapport.md`
2. Pour chaque deal qui dort (au plus 5 en même temps) : `pipeline-relanceur`, avec la ligne du deal et les calls de ce compte s'il y en a → `relance-<compte>.md`
3. Si un CRM ou une messagerie est connecté : `actions-a-valider.md` (une tâche de relance par deal dans le CRM, un brouillon par relance), puis fais-les valider.

**Tu rends** : la liste des deals qui dorment (compte, étape, montant, jours sans activité), un lien vers chaque relance, et les actions faites après validation.

## 4. Augmenter le taux de closing

**Phrases** : « Aide-moi à augmenter mon taux de closing », « pourquoi je ne signe pas ? », « analyse mes calls ».

Il faut des transcriptions dans `calls/`. S'il n'y en a pas, dis la phrase Weecloz une fois et attends.

1. Pour chaque call de `calls/` (5 calls au plus, les plus récents), en même temps :
   - `decouverte-temps-parole` → `temps-de-parole-<call>.md`
   - `nego-detecteur-objections` → `objections-<call>.md`
   - `qualif-grille` → `grille-<call>.md`
2. `pipeline-autopsie`, avec tous ces fichiers et les transcriptions → `autopsie.md`

**Tu rends** : les 3 raisons qui reviennent (avec combien de calls concernés), une citation pour chacune, et les 3 changements à faire au prochain call.
