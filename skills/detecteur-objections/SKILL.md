---
name: detecteur-objections
description: Analyse la transcription d'un call de vente et relève chaque objection du prospect — prix, timing, validation interne, besoin pas clair, concurrence, confiance, y compris les objections cachées dites à demi-mot — avec la citation exacte, la minute, la réponse du commercial et un verdict (bien traitée, mal traitée, ignorée). Utilise ce skill dès que l'utilisateur colle ou évoque la transcription d'un call et parle d'objections, de freins, de ce qui a bloqué, de pourquoi le prospect hésite, ou demande « analyse ce call », « qu'est-ce qui a coincé ? », « liste les objections », même sans dire le mot « objection ».
---

# Détecteur d'objections

Tu relèves tout ce qui freine la vente dans un call, et tu dis honnêtement si le commercial l'a bien traité. Ce rapport ne sert que s'il est fidèle : une citation reformulée ou mal attribuée fait travailler le commercial sur un problème qui n'existe pas.

## 1. Avant de commencer

- **La transcription** : si elle n'est pas dans la conversation, demande-la : « Colle la transcription du call (dans Weecloz : onglet Transcript → Copier le transcript, ou n'importe quelle transcription avec les noms des interlocuteurs). »
  Format Weecloz : un en-tête (le call, la date et la durée, les participants), puis une ligne par réplique `[mm:ss] Nom: texte`. Les minutes peuvent dépasser 59 (`[78:08]`). Dans un export en anglais, le commercial s'appelle « You ».
- **Le contexte** : cherche `ma-vente.md` (dans les fichiers du Projet ou dans le dossier de travail) : il donne le nom du commercial dans les transcriptions, son offre, son process et son style. S'il n'existe pas, ne bloque pas : demande en une question le nom de l'utilisateur, ce qu'il vend et son client type, ou continue en déduisant qui est qui à partir du contenu, et préviens que la réponse sera plus générique.

## 2. Trouve les objections

Une objection, c'est un moment où le **prospect** exprime un frein, un doute, une réticence ou un refus qui ralentit la vente. Les questions du commercial n'en sont jamais.

- **Objections explicites** : « c'est trop cher », « on a déjà un outil pour ça », « je dois en parler à mon associé ».
- **Objections cachées** : un frein dit sans en avoir l'air. Par exemple « on verra après l'été », « intéressant, envoyez-moi une doc », « c'est beaucoup de changement pour l'équipe », une note de 5 sur 10, ou une question de méfiance sur le prix total.

Pour chacune :
1. Copie la phrase du prospect mot pour mot, avec la minute du tour de parole où elle commence.
2. Cherche la réponse du commercial qui suit et qui porte sur CETTE objection. Si elle n'existe pas, l'objection est ignorée.
3. Juge la réponse :
   - ✅ **bien traitée** : la réponse adresse directement le frein, et le prospect est rassuré ou ne le relance pas ;
   - ⚠️ **mal traitée** : la réponse est vague, à côté, ou le prospect relance le même frein ensuite ;
   - ❌ **ignorée** : aucune réponse.

Fusionne les citations qui portent sur le même frein (garde la plus nette), et garde 12 objections au plus.

**Qui parle** : le commercial pilote l'appel, pose les questions de découverte, présente l'offre, répond et propose la suite ; le prospect exprime un besoin, une contrainte, un doute ou un intérêt. Si un label contredit le contenu, fie-toi au contenu. Si tu ne sais vraiment pas qui parle, n'utilise pas ce passage.

## 3. Rends ce rapport

Utilise exactement ce gabarit :

```
# Objections du call avec [prospect]

| # | Objection | Ce qu'il a dit | Ta réponse | Verdict | Pourquoi |
|---|---|---|---|---|---|
| 1 | [famille : prix, timing, validation interne, besoin, concurrence, confiance] | [mm:ss] « … » | « … » ou — | ✅ / ⚠️ / ❌ | une ligne |

## Les objections cachées
- [mm:ss] « … » : ce qu'elle veut vraiment dire, en une ligne.

## La plus coûteuse
Une ligne : l'objection qui a le plus pesé sur l'issue du call, et pourquoi.

👉 Pour savoir quoi répondre la prochaine fois, demande-moi « dis plutôt ».
```

Classe le tableau par ordre d'apparition dans le call. Les objections cachées apparaissent aussi dans le tableau ; la section dédiée explique ce qu'elles veulent dire.

## Règles

- **Citations** : au format `[mm:ss] « phrase exacte »`. On copie mot pour mot, on peut couper avec « … », on ne reformule jamais. La minute est recopiée de la transcription, jamais calculée. Sans minutes dans la transcription, cite sans minute.
- **« Ta réponse »** : les vrais mots du commercial (copiés ou à peine raccourcis), jamais une catégorie du genre « argument de valeur ».
- **« Pourquoi »** : un fait, pas une morale. Par exemple « il propose une remise avant de savoir ce que "trop cher" veut dire pour elle ».
- Tutoie l'utilisateur. N'invente rien : si le call n'a aucune objection, dis-le.
