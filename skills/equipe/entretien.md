# L'entretien

Deux temps : **le socle** au premier lancement (environ 10 minutes), puis **le reste au bon moment**, la première fois qu'une mission en a besoin. Rien n'est demandé pour rien, et rien n'est demandé deux fois : avant chaque question, vérifie que la réponse n'est pas déjà dans un fichier.

Une question à la fois. Chaque question se termine par « (Tu peux répondre "je ne sais pas".) ». Si l'utilisateur répond à plusieurs questions d'un coup, ne les repose pas. S'il dit « écris la fiche » ou « je ne sais pas pour le reste », arrête et écris les fichiers avec ce que tu as.

Commence par : « Pour que l'équipe travaille pour toi et pas pour un commercial imaginaire, j'ai besoin de te connaître : 6 questions, une à la fois. »

## Le socle

1. **Toi** : « Comment tu t'appelles, quel est ton rôle et ton entreprise ? Et dans tes transcriptions de calls, tu apparais sous quel nom ? (Dans Weecloz, c'est "Vous", ou "You" en anglais.) »
2. **Ton offre** : « Qu'est-ce que tu vends, en 2 phrases, et à quel prix ? Qu'est-ce que ça change concrètement pour ton client ? Et tes meilleures preuves : un client, un chiffre, un résultat réel. »
3. **Tes cibles** : « À qui tu vends ? Donne-moi 1 à 3 types de clients. Pour chacun : le secteur, la taille, la zone, et l'intitulé exact du poste de la personne qui décide, comme sur sa carte de visite. » Puis, cible par cible : « Qu'est-ce qui leur fait mal, et qu'est-ce qui les pousse à acheter maintenant ? Et à qui tu ne veux surtout pas écrire ? »
4. **Tes concurrents** : « Contre qui ou contre quoi tu te bats (des concurrents, Excel, ne rien faire…) ? Et pourquoi tes clients te choisissent ? »
5. **Tes outils** : d'abord, regarde les outils disponibles dans la session dont le nom évoque un CRM (HubSpot, Pipedrive, folk, Salesforce, Axonaut…), un outil d'enrichissement (FullEnrich, Dropcontact, Kaspr, Lusha…), une messagerie (Gmail, Outlook) ou un outil de séquences (lemlist, La Growth Machine…). Puis : « Je vois que [outils détectés] sont connectés. Tu en utilises d'autres pour trouver des emails, suivre tes deals, envoyer tes mails ou tes séquences ? » Pour chaque outil, dis ce que l'équipe en fera, en une ligne. Un outil utilisé mais pas connecté : explique en une phrase qu'il faut l'ajouter dans les connecteurs de Claude, et note-le « pas connecté ».
6. **Ton style** : « Tu tutoies ou tu vouvoies tes prospects ? Ton ton en deux mots ? Et ta signature de mail ? »

À la fin du socle, écris les 3 fichiers (formats ci-dessous et dans `fichiers-profil.md`), montre un résumé en 5 lignes, dis qu'il peut les modifier quand il veut, puis propose les 4 missions.

## Au bon moment

| La 1re fois que… | Demande | Range dans |
|---|---|---|
| tu prospectes (recherche de comptes, emails, LinkedIn, séquence) | « Montre-moi 3 à 5 messages ou mails de prospection qui ont eu des réponses, et dis-moi pour quelle cible. Et un qui a fait un flop, si tu en as un. Colle-les simplement ici. » Si l'utilisateur n'en a pas : « Pas de souci, l'équipe partira des exemples de base, et tu me diras ce qui marche. » | `messages-qui-marchent/gagnants.md`, `flops.md` |
| tu cherches plus de 10 comptes | l'échantillon de 5 à 10 comptes à valider (voir SKILL.md) | « ne pas viser » dans `mes-cibles.md` si refus |
| tu relances ou tu fais un rapport pipeline | si aucun CRM n'est connecté : « Exporte tes deals en CSV et colle-le ou mets-le dans ton dossier. » Et : « Quelles sont les étapes de ton pipeline ? » | le CSV à la racine ; les étapes dans la rubrique 8 de `ma-vente.md` |
| tu analyses des calls | les transcriptions, avec la phrase Weecloz si `calls/` est vide | `calls/` |
| tu rédiges une proposition | « Qu'est-ce qui est inclus ou non dans ton offre, et tes conditions (durée, paiement) ? » | rubrique 2 de `ma-vente.md` |
| tu remplis une grille de qualification | « Tu utilises une grille : BANT, MEDDIC, SPICED, la tienne ? (Sinon on prend BANT.) » | rubrique 6 de `ma-vente.md` |
| tu traites des objections | « Les 3 objections que tu entends le plus, et ce que tu réponds aujourd'hui ? » | rubrique 7 de `ma-vente.md` |

## Les fichiers du socle

### `ma-vente.md`

Les skills d'analyse des calls lisent ce fichier : garde exactement ces titres. La rubrique 3 résume la cible principale et renvoie à `mes-cibles.md`.

```
# Ma vente

## 1. Moi
- Mon prénom et mon nom :
- Mon nom tel qu'il apparaît dans mes transcriptions :
- Mon rôle :
- Mon entreprise :

## 2. Mon offre
- Ce que je vends, en 2 phrases :
- Le problème que je résous :
- Prix ou fourchette :
- Inclus :
- Pas inclus :

## 3. Mon client type
- Cible principale : [résumé en une ligne] (détail et autres cibles : voir mes-cibles.md)
- Le décideur :
- Ses 3 plus grosses douleurs :
- Ce qui déclenche l'achat :

## 4. Mes arguments
1. [argument] — preuve : [preuve]

## 5. Mes concurrents et alternatives
- Concurrents directs :
- Alternatives :
- Pourquoi on nous choisit plutôt qu'eux :

## 6. Ma grille de qualification
- Grille : à compléter

## 7. Mes objections connues
| Objection que j'entends | Ma meilleure réponse aujourd'hui |
|---|---|

## 8. Mon process de vente
- Les étapes de mon pipeline : à compléter
- Mon CRM :
- Mon cycle de vente moyen : à compléter
- Mon panier moyen : à compléter

## 9. Mon style
- Avec mes prospects, je :
- Mon ton :
- Ma signature de mail :
```

### `mes-cibles.md` et `mes-outils.md`

Au format de `fichiers-profil.md`.

## Règles

- Uniquement ce que l'utilisateur a dit, avec ses mots. Rien de déduit ni d'inventé.
- Ce qui manque : « à compléter ». Tu le demanderas au bon moment.
- Si le nom dans les transcriptions n'est pas donné, mets « You, Vous » (les libellés de Weecloz).
- Zone non précisée : « France ».
