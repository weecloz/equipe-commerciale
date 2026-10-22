---
name: prepa-call
description: Prépare un call de vente (découverte, démo, closing, relance téléphonique) avec un brief prêt à lire en 2 minutes — rappel de l'historique et de l'étape du deal, contexte du compte, rôle du prospect, besoins probables, 5 questions à poser, objections probables avec leurs réponses, et objectif du call. Utilise ce skill dès que l'utilisateur parle d'un rendez-vous ou d'un call à venir avec un prospect ou un client, même s'il ne dit pas « brief » — par exemple « prépare mon call avec Sarah », « je vois Nova demain », « j'ai un rdv à 14h avec le DG de X », « aide-moi à préparer ma démo », « je rappelle Julie mardi ».
---

# Prépa de call

Tu prépares le commercial à un call précis. Le but : qu'il arrive en sachant à qui il parle, ce qu'il veut obtenir, et quoi répondre aux objections les plus probables. Un brief trop long ne sera pas lu avant le call, alors va à l'essentiel.

## 1. Rassemble ce que tu sais, dans cet ordre

1. **Le contexte du commercial** : cherche `ma-vente.md` (dans les fichiers du Projet ou dans le dossier de travail). Il te donne son offre, son client type, ses arguments, ses objections connues et sa grille de qualif. S'il n'existe pas, demande en une question : ton nom, ce que tu vends, ton client type. Puis continue, en prévenant que le brief sera plus générique.
2. **Le CRM, si un connecteur CRM est branché sur Claude** (HubSpot, Salesforce, Pipedrive…) : va chercher la fiche du contact et de son entreprise, l'historique du deal (étape, montant, dates), les notes et les derniers échanges (mails, calls). C'est la source la plus fiable sur la relation.
3. **Le web, si tu as la recherche web** : le site de l'entreprise, son actualité récente (levée de fonds, recrutements, nouveau produit), le profil public du prospect.
4. **Le call précédent, s'il y en a un** : demande à l'utilisateur de coller la transcription (dans Weecloz : onglet Transcript → Copier le transcript, ou n'importe quelle transcription avec les noms des interlocuteurs). C'est là que se trouvent les vrais mots du prospect, ses freins et ce qui a été promis.

Si une source n'est pas disponible, passe à la suivante sans t'arrêter. N'invente jamais une info pour combler un trou : écris plutôt « à vérifier pendant le call », et transforme le trou en question.

## 2. Écris le brief

Utilise exactement ce gabarit. Chaque info factuelle est suivie de sa source entre parenthèses : (CRM), (web), (call du jj/mm) ou (ma-vente). Comme ça, le commercial sait ce qui est sûr et ce qui est une hypothèse.

```
# Brief : [Prénom Nom], [Entreprise] — [type de call], [date si connue]

## Le rappel
- **Historique** : combien d'échanges, la date du dernier, et de quoi vous avez parlé (2 à 3 sujets clés). Si c'est un premier call : « Premier échange » et d'où vient le contact.
- **Étape du deal** : l'étape actuelle, et le montant s'il est connu.
- **Ce qui a été convenu** : ce que tu as promis, ce que le prospect a promis, ce qui a été envoyé.
- **Ce qui reste en suspens** : la question pas tranchée, le doute pas levé, la personne pas encore vue.

## Le compte
- 2 à 4 puces : activité, taille, situation actuelle, actualité utile.

## La personne
- Son rôle, ce qui compte pour elle, ce qu'elle a déjà dit (citations du call précédent au format [mm:ss] « … »).

## Ses besoins probables
- 2 à 3 hypothèses, reliées à l'offre de ma-vente.md.

## 5 questions à poser
★ 1. … (les 3 prioritaires, marquées ★, d'abord)
★ 2. …
★ 3. …
4. …
5. …

## 2 objections probables
- « [objection, formulée comme le prospect la dirait] » → Réponds : « [phrase à dire telle quelle] »
- « [une 2e objection, différente de la 1re] » → Réponds : « … »

## Objectif du call
Une phrase : ce que le commercial doit obtenir avant de raccrocher (ex. une date de démo avec le DAF présent).
```

## Règles

- **Le rappel vient en premier**, parce que c'est ce que le commercial lit 30 secondes avant de décrocher. Il doit pouvoir reprendre la conversation là où elle s'est arrêtée (« la dernière fois, on avait parlé de… ») sans relire ses notes. Remplis les 4 puces, même courtes ; si une info manque, écris « à vérifier pendant le call ».
- **Les questions** sont ouvertes, tirées de ce que tu sais du compte, et servent l'objectif du call. Elles partent de ce qui reste en suspens dans le rappel. Les 3 questions ★ comblent ce qui manque le plus pour avancer (souvent : le budget, le décideur, le timing).
- **L'objectif du call** dépend de l'étape du deal : on ne vise pas une signature à un premier échange.
- **Les objections probables** : toujours 2, différentes l'une de l'autre, chacune avec sa réponse. Elles viennent d'abord du call précédent et des objections connues de `ma-vente.md`, sinon du profil du prospect. La réponse est une phrase qu'on peut dire telle quelle, avec le contexte de ce prospect, pas un conseil général.
- **Les citations** sont copiées mot pour mot depuis la transcription, avec la minute telle qu'elle apparaît : `[mm:ss] « phrase exacte »`. On peut couper avec « … », jamais reformuler. Si la transcription n'a pas de minutes, cite sans minute.
- **Qui parle** : le commercial pilote, pose les questions et présente l'offre ; le prospect parle de ses besoins, de ses freins et de son intérêt. Si un label semble faux, fie-toi au contenu.
- Tutoie l'utilisateur. Reste court : le brief doit se lire en 2 minutes.
