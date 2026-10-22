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

**Phrases** : « Trouve-moi de nouveaux clients », « trouve-moi 20 prospects », « remplis mon pipe ».

Nombre de comptes : celui demandé, sinon 10.

1. `strategie-portrait-client` → `portrait-client.md` (s'il en existe déjà un récent dans `livrables/`, réutilise-le et saute cette étape).
2. `recherche-comptes`, avec `portrait-client.md` et le nombre de comptes → `comptes.md`
3. En même temps :
   - `recherche-decideurs` → `decideurs.md`
   - `recherche-declencheurs` → `declencheurs.md`
4. `prospection-accroches` → `accroches.md`
5. En même temps :
   - `prospection-email` → `emails.md`
   - `prospection-linkedin` → `linkedin.md`
6. Toi : la liste d'envoi du jour, au format du modèle `liste-envoi.md` (skill `modeles`), avec les messages des deux fichiers → `liste-envoi.md`

**Tu rends** : le nombre de comptes trouvés (et combien ont été écartés faute de source), les 3 plus prometteurs avec leur déclencheur, et le lien vers la liste d'envoi. Rappelle que c'est l'utilisateur qui envoie.

## 3. Relancer les deals qui dorment

**Phrases** : « Relance mes deals qui dorment », « qui je dois relancer ? », « mes deals sont bloqués ».

Il faut un export CSV du CRM (ou le CRM branché sur Claude Code). Sans l'un ni l'autre, demande l'export en une phrase et attends.

1. `pipeline-rapport` → `rapport.md`
2. Pour chaque deal qui dort (au plus 5 en même temps) : `pipeline-relanceur`, avec la ligne du deal et les calls de ce compte s'il y en a → `relance-<compte>.md`

**Tu rends** : la liste des deals qui dorment (compte, étape, montant, jours sans activité) et un lien vers chaque relance.

## 4. Augmenter le taux de closing

**Phrases** : « Aide-moi à augmenter mon taux de closing », « pourquoi je ne signe pas ? », « analyse mes calls ».

Il faut des transcriptions dans `calls/`. S'il n'y en a pas, dis la phrase Weecloz une fois et attends.

1. Pour chaque call de `calls/` (5 calls au plus, les plus récents), en même temps :
   - `decouverte-temps-parole` → `temps-de-parole-<call>.md`
   - `nego-detecteur-objections` → `objections-<call>.md`
   - `qualif-grille` → `grille-<call>.md`
2. `pipeline-autopsie`, avec tous ces fichiers et les transcriptions → `autopsie.md`

**Tu rends** : les 3 raisons qui reviennent (avec combien de calls concernés), une citation pour chacune, et les 3 changements à faire au prochain call.
