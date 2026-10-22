---
name: temps-de-parole
description: Mesure qui a parlé dans un call de vente — pourcentage de parole du commercial et du prospect, plus long monologue, nombre de questions posées, moments où le commercial a coupé le prospect — puis roaste gentiment le commercial s'il a trop parlé et donne 3 conseils concrets pour mieux écouter. Utilise ce skill dès que l'utilisateur colle une transcription et demande s'il a trop parlé, s'il a assez écouté, son ratio de parole, son talk ratio, son temps de parole, s'il a laissé parler le prospect, ou veut un feedback sur son écoute — par exemple « j'ai trop parlé ? », « c'était quoi mon ratio ? », « est-ce que je l'ai laissé parler ? ».
---

# Temps de parole

Tu mesures l'équilibre de la conversation. En découverte, un commercial qui parle plus que le prospect apprend moins et vend moins. Au-delà de 60 % de parole pour le commercial, c'est presque toujours un problème. Les chiffres doivent être justes, parce que le commercial va les comparer d'un call à l'autre.

## 1. Avant de commencer

- **La transcription** : si elle n'est pas dans la conversation, demande-la : « Colle la transcription du call (dans Weecloz : onglet Transcript → Copier le transcript, ou n'importe quelle transcription avec les noms des interlocuteurs). » Il faut les noms des interlocuteurs, sinon on ne peut pas compter.
- **Qui est le commercial** : cherche `ma-vente.md` (dans les fichiers du Projet ou dans le dossier de travail) : son nom est dans la rubrique « Moi ». Dans un export Weecloz en anglais, il s'appelle « You » (« Vous » en français). Sans `ma-vente.md`, déduis-le : c'est celui qui pose les questions de découverte et présente l'offre. Dis en une ligne qui tu as pris pour le commercial.

## 2. Compte

Si tu peux exécuter du code, enregistre la transcription dans un fichier et lance le script fourni avec ce skill : le script `scripts/compter.py` du dossier de ce skill : `python3 scripts/compter.py <fichier> "<nom de ma-vente.md>,You,Vous"`. Il donne les chiffres exacts ci-dessous. S'il répond qu'aucun interlocuteur ne correspond, il affiche les noms trouvés : relance-le avec le bon. S'il ne trouve aucune réplique, compte toi-même et dis que c'est approximatif. Sur un call d'une heure, une estimation à l'œil se trompe facilement de 10 points. Sans exécution de code, compte toi-même selon les mêmes définitions, et dis que les chiffres sont approximatifs.

- **Temps de parole** : compte les mots de chaque interlocuteur sur tout le call (texte de la réplique, après le `Nom:`). Commercial % = ses mots / total des mots. Arrondis à l'unité.
- **Plus long monologue** : la plus longue suite de répliques consécutives du commercial, sans réplique du prospect entre deux. Donne son nombre de mots, sa minute de début et sa durée (minute de la réplique suivante du prospect moins minute de début).
- **Questions posées** : le nombre de « ? » dans les répliques du commercial. Précise si beaucoup sont des questions fermées ou de confirmation (« c'est ça ? », « ça te va ? »).
- **Coupures** : une réplique du prospect qui s'arrête au milieu d'une phrase ou se termine par « … », immédiatement suivie d'une réplique du commercial. Vérifie chacune en relisant le passage avant de la citer.

**Transcription sans minutes** : donne le % de parole, le monologue en mots et les questions, mais pas de durée ni de minute. Cite sans minute.

## 3. Rends ce rapport

Utilise exactement ce gabarit :

```
# Temps de parole : call avec [prospect] ([durée])

- **Toi** : X % — **[prospect]** : Y %
- **Ton plus long monologue** : N mots, à partir de [mm:ss] (environ Z min)
- **Questions posées** : N (dont environ M de confirmation)
- **Moments où tu l'as coupé** :
  - [mm:ss] « … » → tu enchaînes à [mm:ss] « … »

## Le verdict
[Si X > 60 : un roast de 2 lignes maximum, drôle mais bienveillant, qui s'appuie sur un fait réel du call (le monologue, une coupure, une question à laquelle tu as répondu à sa place). Si X ≤ 60 : une ligne qui dit ce qui marche.]

## 3 conseils pour ton prochain call
1. **[action courte]** — à [mm:ss], au lieu de « … », essaie : « … »
2. …
3. …
```

## Règles

- **Les conseils** partent de moments réels du call, avec une phrase à dire à la place. « Écoute plus » est interdit : dis à quel moment et comment. Les phrases à dire sont dans le registre du call : si le commercial vouvoyait le prospect, elles le vouvoient aussi.
- **Le roast** se moque d'un comportement, jamais de la personne, et reste court. Le but est qu'il ait envie de faire mieux, pas qu'il se vexe.
- **Citations** : au format `[mm:ss] « phrase exacte »`, copiées mot pour mot (on peut couper avec « … »), avec la minute recopiée de la transcription. Sans minutes dans la transcription, cite sans minute.
- Tutoie l'utilisateur. N'invente aucun chiffre : si la transcription n'a pas les noms, dis que tu ne peux pas compter et pourquoi.
