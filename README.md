<p align="center">
  <img src="assets/banner.svg" alt="Ton équipe commerciale dans Claude Code : 1 chef, 40 agents, 10 départements" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="Licence MIT" src="https://img.shields.io/badge/licence-MIT-2F6BFF?style=flat-square"></a>
  <img alt="Plugin Claude Code" src="https://img.shields.io/badge/plugin-Claude%20Code-D97757?style=flat-square">
  <img alt="40 agents" src="https://img.shields.io/badge/agents-40-151923?style=flat-square">
  <img alt="En français" src="https://img.shields.io/badge/langue-fran%C3%A7ais-151923?style=flat-square">
</p>

<p align="center">
  <b>Une équipe commerciale complète, installée en 2 minutes.</b><br>
  Tu donnes une mission au chef. Il répartit le travail entre 40 agents spécialisés.<br>
  Chacun te rend un fichier prêt à utiliser : un brief, une liste de prospects, une relance, une proposition…
</p>

<p align="center">
  <a href="#installation">Installation</a> ·
  <a href="#avant-tout--tes-calls">Tes calls</a> ·
  <a href="#les-4-missions">Les 4 missions</a> ·
  <a href="#lorganigramme">L'organigramme</a> ·
  <a href="#comment-ça-marche">Comment ça marche</a> ·
  <a href="exemples/">Exemples</a>
</p>

---

## Installation

Il te faut un abonnement Claude qui donne accès à **Claude Code**, et l'app Claude sur ton ordinateur. Pas besoin de terminal.

1. Crée un dossier `Ma vente` sur ton ordinateur.
2. Ouvre l'app Claude, onglet **Code**, et démarre une session dans ce dossier.
3. Tape ces deux commandes, l'une après l'autre :

   ```
   /plugin marketplace add weecloz/equipe-commerciale
   /plugin install equipe@weecloz
   ```

4. Tape `/equipe` (ou `/equipe:equipe` si la première forme ne répond pas).

Au premier lancement, le chef te pose **9 questions rapides** (ton offre, ton prix, ton client idéal, tes arguments, tes objections…), une à la fois, et écrit ta fiche `ma-vente.md`. Toute l'équipe la lit avant de travailler. C'est un simple fichier : tu peux le modifier quand tu veux.

## Avant tout : tes calls

Trouver les bons prospects, leur écrire, préparer un call, répondre à une objection, relancer : tout repose sur **ce que tes clients disent vraiment pendant tes appels**. Leurs vraies douleurs, leurs vrais besoins, leurs vrais mots.

Sans transcriptions, l'équipe travaille sur des suppositions. Avec, elle travaille sur des faits.

Le plus simple : l'extension Chrome **[Weecloz](https://www.weecloz.io)**. Elle enregistre tes calls sur Google Meet, Zoom et Teams, **sans bot dans ta réunion**. Après le call : onglet Transcript → Copier le transcript, et tu le colles dans la conversation. Le chef le range dans `calls/`.

> N'importe quelle transcription marche aussi, du moment qu'elle contient les noms des interlocuteurs. Pense à prévenir ton prospect que tu enregistres.

## Les 4 missions

| Tu tapes | Le chef lance | Tu reçois |
|---|---|---|
| « Prépare mon call avec Sarah » | fiche compte + objections passées → prépa de call | un brief de 2 minutes : le rappel de vos échanges, 5 questions, 2 objections probables avec la réponse, l'objectif du call · [exemple](exemples/1-prepa-call.md) |
| « Trouve-moi de nouveaux clients » | portrait client → comptes → décideurs + déclencheurs → accroches → emails + LinkedIn | des comptes réels, chacun avec sa source, et ta liste d'envoi du jour · [exemple](exemples/2-nouveaux-clients.md) |
| « Relance mes deals qui dorment » | rapport pipeline → une relance par deal | les deals qui dorment (depuis ton export CSV) et leur relance écrite · [exemple](exemples/3-deals-qui-dorment.md) |
| « Aide-moi à augmenter mon taux de closing » | temps de parole + objections + qualif sur chaque call → autopsie | les 3 freins qui reviennent, avec citations, et quoi changer · [exemple](exemples/4-taux-de-closing.md) |

Pour tout le reste, parle normalement : « écris une proposition pour Nova », « prépare ma négo de vendredi », « fais-moi répéter ma démo », « mon client risque-t-il de partir ? ». Le chef choisit les bons agents et te dit lesquels.

## L'organigramme

| Département | Agents |
|---|---|
| **1. Stratégie et ciblage** | `strategie-portrait-client` · `strategie-segments` · `strategie-message` · `strategie-concurrence` |
| **2. Recherche de prospects** | `recherche-comptes` · `recherche-decideurs` · `recherche-declencheurs` · `recherche-fiche-compte` |
| **3. Prospection** | `prospection-email` · `prospection-linkedin` · `prospection-sequence` · `prospection-accroches` |
| **4. Qualification** | `qualif-grille` · `qualif-score` · `qualif-questions` · `qualif-disqualifieur` |
| **5. Découverte et analyse des calls** | `decouverte-prepa-call` · `decouverte-analyste-call` · `decouverte-temps-parole` · `decouverte-signaux-achat` |
| **6. Démos** | `demo-scenario` · `demo-preuves` · `demo-repetition` · `demo-debrief` |
| **7. Propositions** | `propo-redacteur` · `propo-roi` · `propo-resume-decideur` · `propo-relecteur` |
| **8. Objections et négociation** | `nego-detecteur-objections` · `nego-dis-plutot` · `nego-preparation` · `nego-simulateur` |
| **9. Suivi du pipeline** | `pipeline-notes-crm` · `pipeline-relanceur` · `pipeline-rapport` · `pipeline-autopsie` |
| **10. Comptes clients** | `comptes-onboarding` · `comptes-sante` · `comptes-upsell` · `comptes-recommandation` |

Le détail de chaque agent (ce qu'il fait, ce qu'il lit, ce qu'il écrit) est dans [`skills/equipe/organigramme.md`](skills/equipe/organigramme.md).

## Comment ça marche

```mermaid
flowchart LR
    U([Toi : une mission]) --> C{{/equipe<br>le chef}}
    C -->|en parallèle| A1[agent]
    C -->|en parallèle| A2[agent]
    A1 --> A3[agent suivant]
    A2 --> A3
    A3 --> L[(livrables/<br>un dossier daté par mission)]
    C --> S([Toi : la synthèse<br>et les liens])
    M[ma-vente.md] -.-> A1 & A2 & A3
    K[calls/] -.-> A1 & A2 & A3
```

- **Le chef** (`skills/equipe/`) lit ta demande, choisit les agents dans l'organigramme, annonce son plan en une ligne, lance les agents (jusqu'à 5 en même temps) et te rend une synthèse courte.
- **Chaque agent** (`agents/`) a un seul job, les outils strictement nécessaires (le web seulement pour la stratégie et la recherche) et un format de sortie fixe. Plusieurs s'appuient sur des skills de vente (`skills/`) : prépa de call, détecteur d'objections, temps de parole (compté par un script, pas estimé), relance…
- **Ton dossier de travail** contient tout : `ma-vente.md`, `calls/` et `livrables/`. Rien ne part ailleurs.

## Les règles de toute l'équipe

- **Rien d'inventé.** Chaque info porte sa source : ta fiche, un call (avec la minute), une page web (avec l'adresse) ou ton CRM. Sinon, c'est écrit « à vérifier ».
- **Des citations mot pour mot**, au format `[mm:ss] « phrase exacte »`.
- **Rien n'est envoyé à ta place.** L'équipe prépare les messages, tu les envoies.
- **Ton CRM** : s'il est connecté à Claude Code, le chef le lit et le transmet aux agents. Il n'y écrit qu'après ton accord.

> **LinkedIn** : Claude Code peut piloter un navigateur, mais LinkedIn interdit l'automatisation et restreint les comptes qu'il repère. Envoie toi-même avec ta liste d'envoi du jour. Si tu automatises quand même, c'est sous ta responsabilité.

## Structure du dépôt

```
.claude-plugin/     manifeste du plugin et marketplace « weecloz »
skills/equipe/      le chef : SKILL.md, organigramme, missions, entretien
skills/…            les 10 skills de vente et les modèles (proposition, séquence, onboarding, liste d'envoi)
agents/             les 40 agents, un fichier par agent
exemples/           une réponse réelle (anonymisée) pour chaque mission
```

## Licence

[MIT](LICENSE). Utilise-la, modifie-la, partage-la.

<p align="center"><sub>Fait par <a href="https://www.weecloz.io">Weecloz</a> · l'extension qui enregistre et analyse tes calls de vente, sans bot.</sub></p>
