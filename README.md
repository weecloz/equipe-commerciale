# Ton équipe commerciale dans Claude Code

40 agents. 10 départements. 1 chef. Tu lui donnes une mission, il répartit le travail, et chaque agent te rend un fichier prêt à utiliser.

## Installation (2 minutes)

Il te faut un abonnement Claude qui donne accès à Claude Code.

1. Ouvre l'app Claude, onglet **Code**, et démarre une session dans un dossier dédié (ex. `Ma vente`).
2. Tape ces deux commandes, l'une après l'autre :
   ```
   /plugin marketplace add weecloz/equipe-commerciale
   /plugin install equipe@weecloz
   ```
3. Tape `/equipe` (ou `/equipe:equipe` si la première forme ne répond pas).

## Premier lancement

Le chef te pose 9 questions rapides sur ta vente (ton offre, ton client type, tes objections…), une à la fois, et écrit ta fiche `ma-vente.md`. Toute l'équipe la lit avant de travailler. Tu peux la modifier quand tu veux : c'est un simple fichier.

Il crée aussi deux dossiers :
- `calls/` : tes transcriptions de calls, une par fichier ;
- `livrables/` : tout ce que l'équipe produit, rangé par mission et par date.

## Les 4 missions pour commencer

| Tu tapes | L'équipe te rend |
|---|---|
| « Prépare mon call avec Sarah » | un brief : le rappel de vos échanges, 5 questions, 2 objections probables avec la réponse, l'objectif du call |
| « Trouve-moi de nouveaux clients » | des comptes réels (chacun avec sa source), leur décideur, leur actualité, les messages prêts et ta liste d'envoi du jour |
| « Relance mes deals qui dorment » | les deals qui dorment (depuis ton export CRM) et une relance écrite pour chacun |
| « Aide-moi à augmenter mon taux de closing » | sur tes calls : ton temps de parole, tes objections ratées, ta qualif, et les 3 raisons qui reviennent |

Pour tout le reste, parle normalement (« écris une proposition pour Nova », « prépare ma négo », « fais-moi répéter ma démo ») : le chef choisit les bons agents.

## L'organigramme

| Département | Agents |
|---|---|
| 1. Stratégie et ciblage | `strategie-portrait-client` · `strategie-segments` · `strategie-message` · `strategie-concurrence` |
| 2. Recherche de prospects | `recherche-comptes` · `recherche-decideurs` · `recherche-declencheurs` · `recherche-fiche-compte` |
| 3. Prospection | `prospection-email` · `prospection-linkedin` · `prospection-sequence` · `prospection-accroches` |
| 4. Qualification | `qualif-grille` · `qualif-score` · `qualif-questions` · `qualif-disqualifieur` |
| 5. Découverte et analyse des calls | `decouverte-prepa-call` · `decouverte-analyste-call` · `decouverte-temps-parole` · `decouverte-signaux-achat` |
| 6. Démos | `demo-scenario` · `demo-preuves` · `demo-repetition` · `demo-debrief` |
| 7. Propositions | `propo-redacteur` · `propo-roi` · `propo-resume-decideur` · `propo-relecteur` |
| 8. Objections et négociation | `nego-detecteur-objections` · `nego-dis-plutot` · `nego-preparation` · `nego-simulateur` |
| 9. Suivi du pipeline | `pipeline-notes-crm` · `pipeline-relanceur` · `pipeline-rapport` · `pipeline-autopsie` |
| 10. Comptes clients | `comptes-onboarding` · `comptes-sante` · `comptes-upsell` · `comptes-recommandation` |

Les règles de toute l'équipe : rien d'inventé (chaque info a sa source), des citations mot pour mot, et rien n'est envoyé à ta place : l'équipe prépare, tu envoies. Si ton CRM est connecté à Claude Code, les agents le lisent, et n'y écrivent qu'après ton accord.

## Tes calls

La moitié de l'équipe travaille sur ce qui s'est vraiment dit pendant tes calls. Mets tes transcriptions dans `calls/`, avec les noms des interlocuteurs.

Le plus simple : l'extension Chrome **Weecloz**. Elle enregistre tes calls sur Google Meet, Zoom et Teams, sans bot. Après le call : onglet Transcript → Copier le transcript, et tu colles dans un fichier de `calls/`. → https://www.weecloz.io

## Licence

MIT. Utilise-la, modifie-la, partage-la.
