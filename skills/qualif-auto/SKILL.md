---
name: qualif-auto
description: Remplit automatiquement la grille de qualification d'un prospect (BANT par défaut, ou MEDDIC, SPICED, CHAMP, ou la grille perso du commercial) à partir de la transcription d'un call de vente, avec une citation comme preuve pour chaque case, et transforme chaque case vide en question à poser au prochain call. Utilise ce skill dès que l'utilisateur parle de qualifier un prospect, de BANT, MEDDIC, SPICED, CHAMP, de savoir si un lead est qualifié, si le prospect a le budget, qui décide, ou ce qu'il lui manque comme infos — par exemple « remplis ma grille », « il est qualifié ou pas ? », « qu'est-ce que je ne sais pas encore sur lui ? ».
---

# Qualif auto

Tu remplis la grille de qualification à partir de ce que le prospect a vraiment dit. Une case cochée « à l'impression » fausse les prévisions du commercial et lui fait perdre son temps sur des deals qui ne signeront pas. Une case n'est remplie que si une citation le prouve.

## 1. Avant de commencer

- **La transcription** : si elle n'est pas dans la conversation, demande-la : « Colle la transcription du call (dans Weecloz : onglet Transcript → Copier le transcript, ou n'importe quelle transcription avec les noms des interlocuteurs). » Tu peux recevoir plusieurs calls avec le même prospect : utilise-les tous.
- **Le contexte** : cherche `ma-vente.md` (dans les fichiers du Projet ou dans le dossier de travail) : il donne le nom du commercial dans les transcriptions, son offre, son process et son style. S'il n'existe pas, ne bloque pas : demande en une question le nom de l'utilisateur, ce qu'il vend et son client type, ou continue en déduisant qui est qui à partir du contenu, et préviens que la réponse sera plus générique.
- **La grille** : prends celle de `ma-vente.md` (rubrique « Ma grille de qualification »). S'il n'y en a pas, prends BANT, et dis-le en une ligne.
- **La référence** : lis `grilles.md` (dans le dossier de ce skill). Il donne, pour chaque critère, ce qui compte comme rempli et la question à poser s'il manque.

## 2. Remplis chaque critère

Pour chaque critère de la grille, choisis :
- **✅ Rempli** : une citation du prospect le prouve clairement (un montant, un nom, une date, un problème chiffré) ;
- **🟡 Partiel** : il en parle, mais sans engagement clair, ou avec une contradiction dans le call ;
- **⬜ Vide** : rien dans le call.

Attention aux pièges classiques : le commercial qui répond à la place du prospect (« donc tu as le budget, c'est ça ? » suivi d'un « ouais » ne vaut pas un budget confirmé), ou un chiffre donné par le commercial et pas par le prospect.

## 3. Rends ce rapport

Utilise exactement ce gabarit :

```
# Qualif [grille] : [prospect]

| Critère | Statut | Preuve | Question pour le prochain call |
|---|---|---|---|
| [critère] | ✅ / 🟡 / ⬜ | [mm:ss] « … » (ou —) | « … » (seulement si 🟡 ou ⬜) |

**Verdict** : une ligne. Qualifié, à creuser ou pas qualifié, avec la raison principale.

**Ce qui bloque le plus** : le critère le plus faible, et pourquoi il compte pour ce deal.
```

## Règles

- **Citations** : au format `[mm:ss] « phrase exacte »`, copiées mot pour mot depuis une réplique du prospect (on peut couper avec « … »), avec la minute recopiée telle qu'elle apparaît. Sans minutes dans la transcription, cite sans minute.
- **Qui parle** : le commercial pilote et pose les questions ; le prospect répond, parle de ses besoins et de ses freins. Si un label semble faux, fie-toi au contenu.
- **Les questions** se disent telles quelles, dans le registre du call (tu ou vous), avec le contexte de ce prospect.
- Tutoie l'utilisateur. N'invente rien : une case sans preuve reste vide.
