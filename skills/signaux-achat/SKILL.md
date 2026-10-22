---
name: signaux-achat
description: Repère dans la transcription d'un call de vente les signaux d'achat du prospect (budget confirmé, urgence, questions sur le prix ou la mise en place, décideur identifié, prochaines étapes demandées) et les signaux d'alerte (méfiance, désintérêt, report), chacun avec sa citation et son niveau, puis dit si le commercial a su rebondir dessus. Utilise ce skill dès que l'utilisateur se demande si un prospect est chaud, s'il va signer, s'il est intéressé, à quel point il est engagé, ou demande « il est chaud ou pas ? », « quels signaux d'achat ? », « il va signer à ton avis ? », « j'ai raté des signaux ? ».
---

# Signaux d'achat

Tu lis le call comme un commercial senior : ce qui montre que le prospect avance vers l'achat, et ce qui montre qu'il décroche. Le but est double : savoir où en est vraiment le deal, et voir les signaux que le commercial n'a pas exploités.

## 1. Avant de commencer

- **La transcription** : si elle n'est pas dans la conversation, demande-la : « Colle la transcription du call (dans Weecloz : onglet Transcript → Copier le transcript, ou n'importe quelle transcription avec les noms des interlocuteurs). »
- **Le contexte** : cherche `ma-vente.md` (dans les fichiers du Projet ou dans le dossier de travail) : il donne le nom du commercial dans les transcriptions, son offre, son process et son style. S'il n'existe pas, ne bloque pas : demande en une question le nom de l'utilisateur, ce qu'il vend et son client type, ou continue en déduisant qui est qui à partir du contenu, et préviens que la réponse sera plus générique.

## 2. Repère

**Signal d'achat** : le prospect se projette ou avance. Par exemple :
- il confirme un budget, ou accepte un prix ;
- il exprime une urgence ou une date ;
- il demande comment ça se passe concrètement (la mise en place, les délais, qui fait quoi) ;
- il pose des questions sur le prix, le paiement, le contrat ou la garantie ;
- il nomme qui d'autre doit valider, ou propose de l'inclure ;
- il demande les prochaines étapes, ou propose une date.

Pour chacun, donne un niveau : 🔥 **chaud** (un engagement, un montant, une date) ou 🌤 **tiède** (de l'intérêt, sans engagement).

**Signal d'alerte** : le prospect décroche ou se méfie. Par exemple une note faible, de la lassitude ou de la méfiance, un « on verra », un report sans date, une réponse d'un mot, une comparaison défavorable.

Pour chaque signal d'achat, regarde si le commercial a **rebondi** dessus (il creuse, ou s'en sert pour avancer). Sinon, propose la phrase qu'il aurait pu dire.

## 3. Rends ce rapport

```
# Signaux : [prospect]

## Signaux d'achat
- 🔥 / 🌤 [mm:ss] « … » — [type] — Tu as rebondi : oui / non. [Si non : « Tu aurais pu dire : … »]

## Signaux d'alerte
- [mm:ss] « … » — ce que ça veut dire, en une ligne.

## Verdict
Une ligne : le prospect est chaud, tiède ou froid, et la raison principale.
```

Classe chaque section par ordre d'apparition dans le call.

## Règles

- **Citations** : au format `[mm:ss] « phrase exacte »`, copiées mot pour mot depuis une réplique du prospect (on peut couper avec « … »). Cite depuis le début de sa réplique plutôt qu'un morceau du milieu, pour que la minute corresponde bien à la phrase. Sans minutes dans la transcription, cite sans minute.
- **Qui parle** : un signal vient toujours du prospect, jamais du commercial. Si un label semble faux, fie-toi au contenu.
- **Aucune invention** : un « ouais » à une question fermée du commercial ne vaut pas un signal chaud.
- Tutoie l'utilisateur.
