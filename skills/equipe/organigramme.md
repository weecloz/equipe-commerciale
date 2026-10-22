# L'organigramme de l'équipe

Pour une demande libre, choisis le ou les agents dont la colonne « Ce qu'il fait » correspond. Si deux choix sont possibles, propose-les en une ligne. Les agents s'appellent `equipe:<nom>` avec l'outil Agent.

| Département | Agent | Ce qu'il fait | Ce qu'il lit | Ce qu'il écrit |
|---|---|---|---|---|
| 1. Stratégie et ciblage | `strategie-portrait-client` | Définit le client idéal : secteur, taille, décideur, douleurs, déclencheurs, qui ne pas viser | ma-vente.md, clients actuels | portrait-client.md |
| 1. Stratégie et ciblage | `strategie-segments` | Choisit 2 à 3 segments prioritaires, avec pourquoi maintenant | portrait-client.md | segments.md |
| 1. Stratégie et ciblage | `strategie-message` | Écrit la proposition de valeur et l'angle d'attaque par segment | segments.md, ma-vente.md | messages.md |
| 1. Stratégie et ciblage | `strategie-concurrence` | Veille sur les concurrents : offre, prix publics, positionnement, où on gagne | ma-vente.md, web | concurrence.md |
| 2. Recherche de prospects | `recherche-comptes` | Trouve des entreprises qui collent au client idéal, sur le web public | portrait-client.md ou ma-vente.md, web | comptes.md |
| 2. Recherche de prospects | `recherche-decideurs` | Trouve le décideur probable de chaque compte et son rôle, sur des sources publiques | comptes.md, web | decideurs.md |
| 2. Recherche de prospects | `recherche-declencheurs` | Repère les déclencheurs d'achat : levée, recrutement, nouveau produit, nomination | comptes.md, web | declencheurs.md |
| 2. Recherche de prospects | `recherche-fiche-compte` | Fait la fiche d'un compte avant un call : activité, taille, actu, historique avec nous | nom du compte, calls/, CRM, web | fiche-compte.md |
| 3. Prospection | `prospection-email` | Écrit les emails à froid, un par compte, et la liste d'envoi | comptes.md, accroches.md, messages.md | emails.md |
| 3. Prospection | `prospection-linkedin` | Écrit l'invitation LinkedIn et le premier message, un par compte, et la liste d'envoi | comptes.md, accroches.md, messages.md | linkedin.md |
| 3. Prospection | `prospection-sequence` | Construit une séquence de prospection de 3 à 5 touches sur 2 à 3 semaines | segment ou compte, ma-vente.md | sequence.md |
| 3. Prospection | `prospection-accroches` | Écrit une première phrase personnalisée par compte, avec sa source | comptes.md, declencheurs.md, decideurs.md | accroches.md |
| 4. Qualification | `qualif-grille` | Remplit la grille de qualification (BANT, MEDDIC…) avec une citation par case | une transcription | grille.md |
| 4. Qualification | `qualif-score` | Note une liste de leads A, B ou C selon le client idéal | une liste, un CSV ou le CRM | score.md |
| 4. Qualification | `qualif-questions` | Transforme chaque case vide de la grille en question pour le prochain call | grille.md ou ma-vente.md | questions.md |
| 4. Qualification | `qualif-disqualifieur` | Dit s'il faut continuer ou lâcher un deal, et pourquoi | transcriptions, grille.md | verdict.md |
| 5. Découverte et analyse des calls | `decouverte-prepa-call` | Prépare un call : le rappel, le compte, la personne, 5 questions, 2 objections, l'objectif | calls/ du prospect, fiche-compte.md | brief.md |
| 5. Découverte et analyse des calls | `decouverte-analyste-call` | Résume un call : besoins, engagements des deux côtés, prochaine étape | une transcription | analyse.md |
| 5. Découverte et analyse des calls | `decouverte-temps-parole` | Mesure le temps de parole, le plus long monologue, les questions, les coupures | une transcription | temps-de-parole.md |
| 5. Découverte et analyse des calls | `decouverte-signaux-achat` | Repère les signaux d'achat et d'alerte, et ceux qui n'ont pas été exploités | une transcription | signaux.md |
| 6. Démos | `demo-scenario` | Construit une démo sur mesure, à partir des douleurs entendues en découverte | transcription de découverte, ma-vente.md | scenario-demo.md |
| 6. Démos | `demo-preuves` | Choisit les 3 preuves les plus proches du cas du prospect | ma-vente.md, profil du prospect | preuves.md |
| 6. Démos | `demo-repetition` | Prépare la répétition : les questions et objections que le prospect posera, avec les réponses | transcription, ma-vente.md | repetition.md |
| 6. Démos | `demo-debrief` | Débriefe une démo : moments forts, décrochages, questions sans réponse | transcription de la démo | debrief.md |
| 7. Propositions | `propo-redacteur` | Rédige la proposition commerciale | transcriptions, ma-vente.md | proposition.md |
| 7. Propositions | `propo-roi` | Calcule le retour sur investissement avec les chiffres du prospect | chiffres dits par le prospect | roi.md |
| 7. Propositions | `propo-resume-decideur` | Résume la proposition en une page pour le décideur absent du call | proposition.md ou transcriptions | resume-decideur.md |
| 7. Propositions | `propo-relecteur` | Relit une proposition : clarté, prix, prochaine étape | une proposition | relecture.md |
| 8. Objections et négociation | `nego-detecteur-objections` | Relève chaque objection d'un call, avec la réponse donnée et un verdict | transcriptions | objections.md |
| 8. Objections et négociation | `nego-dis-plutot` | Donne, pour chaque objection ratée, la phrase à dire la prochaine fois | transcription ou objections.md | dis-plutot.md |
| 8. Objections et négociation | `nego-preparation` | Prépare une négociation : concessions, contreparties, seuil de sortie | ma-vente.md, transcriptions, objections.md | nego.md |
| 8. Objections et négociation | `nego-simulateur` | Prépare un entraînement : les objections du prospect dans l'ordre probable, avec les réponses | transcription ou ma-vente.md | simulation.md |
| 9. Suivi du pipeline | `pipeline-notes-crm` | Prépare les notes CRM d'un call (et les écrit dans le CRM après accord) | transcription, CRM | notes-crm.md |
| 9. Suivi du pipeline | `pipeline-relanceur` | Écrit le mail de relance après un call ou pour un deal qui dort | transcription ou ligne du rapport | relance-<compte>.md |
| 9. Suivi du pipeline | `pipeline-rapport` | Fait le rapport pipeline : ce qui a bougé, ce qui dort, les 3 priorités | CSV ou CRM | rapport.md |
| 9. Suivi du pipeline | `pipeline-autopsie` | Trouve les raisons qui reviennent dans les deals perdus ou les calls ratés | plusieurs transcriptions ou notes | autopsie.md |
| 10. Comptes clients | `comptes-onboarding` | Fait le plan des 30 premiers jours d'un nouveau client | transcription de closing, ma-vente.md | onboarding.md |
| 10. Comptes clients | `comptes-sante` | Évalue le risque de départ d'un client (vert, orange, rouge) | échanges récents, CRM | sante.md |
| 10. Comptes clients | `comptes-upsell` | Repère les occasions de vendre plus à un client | échanges, ma-vente.md | upsell.md |
| 10. Comptes clients | `comptes-recommandation` | Dit quand demander un témoignage ou une recommandation, et écrit le message | échanges, résultats obtenus | recommandation.md |
