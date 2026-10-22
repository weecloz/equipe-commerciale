---
name: rapport-pipeline
description: Prépare le rapport pipeline du lundi à partir d'un export CSV du CRM, d'une liste de deals ou d'un connecteur CRM branché sur Claude — les deals qui ont bougé, ceux qui dorment depuis 7 jours ou plus, et les 3 priorités de la semaine avec leur pourquoi. Utilise ce skill dès que l'utilisateur parle de son pipeline, de sa revue de la semaine, de son point du lundi, de ses deals en cours, de prévisions, ou demande « fais mon rapport du lundi », « où en est mon pipe ? », « sur quels deals je dois me concentrer cette semaine ? », « quels deals je dois relancer ? ».
---

# Rapport pipeline du lundi

Tu donnes au commercial une vue claire de son pipeline en 1 minute de lecture, et surtout où mettre son énergie cette semaine. Un deal qui dort depuis plus de 7 jours refroidit : il faut le voir avant qu'il soit trop tard.

## 1. Avant de commencer

- **L'entrée**, dans cet ordre :
  1. un connecteur CRM branché sur Claude : lis les deals ouverts, avec leur étape, leur montant, leur dernière activité et leur prochaine action ;
  2. sinon, un export CSV du CRM, ou une liste collée par l'utilisateur ;
  3. sinon, demande l'un des deux.
- **La date du jour** : prends-la dans le contexte. Si tu ne la connais pas, demande-la : tout le calcul des « 7 jours » en dépend.
- **Le contexte** : cherche `ma-vente.md` (dans les fichiers du Projet ou dans le dossier de travail) : il donne le nom du commercial dans les transcriptions, son offre, son process et son style. S'il n'existe pas, ne bloque pas : demande en une question le nom de l'utilisateur, ce qu'il vend et son client type, ou continue en déduisant qui est qui à partir du contenu, et préviens que la réponse sera plus générique.
- Si une colonne manque (par exemple la date de dernière activité), dis-le et fais le rapport avec ce qui existe.

Si tu peux exécuter du code et que tu as un CSV, calcule les jours depuis la dernière activité avec un script plutôt qu'à l'œil.

## 2. Classe les deals

- **Ont bougé** : une activité dans les 7 derniers jours (une étape franchie, un call, un mail, une proposition envoyée).
- **Dorment** : aucune activité depuis 7 jours ou plus. Indique depuis combien de jours.
- **Priorités** : choisis 3 deals, pas plus. On donne la priorité à ce qui est proche de la signature, à ce qui a un gros montant, et à ce qui dort alors qu'il était chaud. Pour chacun, l'action précise à faire cette semaine.

## 3. Rends ce rapport

```
# Pipeline — semaine du [date]

**En cours** : [n] deals, [montant total]

## Ont bougé ([n])
- [Deal] — [étape] — [montant] — [ce qui s'est passé]

## Dorment ([n]) ⚠️
- [Deal] — [étape] — [montant] — sans activité depuis [n] jours — [prochaine action prévue, ou « aucune »]

## Tes 3 priorités de la semaine
1. **[Deal]** — [action concrète à faire, avec qui et quand] — pourquoi : [une ligne]
2. …
3. …
```

## Règles

- **Aucune invention** : pas de montant, de date ou d'étape qui ne soient dans les données. Une info absente s'écrit « non renseigné ».
- Les noms des étapes sont ceux du CRM ou de `ma-vente.md`.
- Avec un connecteur CRM, ce skill ne fait que lire. Pour mettre le CRM à jour, l'utilisateur passe par le skill `notes-crm`.
- Tutoie l'utilisateur. Le rapport doit tenir sur un écran.
