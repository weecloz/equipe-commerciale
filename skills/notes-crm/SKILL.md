---
name: notes-crm
description: Transforme la transcription d'un call de vente en notes CRM propres — étape du deal, montant, décideur, prochaine action avec sa date, risques, résumé — et met le CRM à jour directement si un connecteur CRM (HubSpot, Salesforce, Pipedrive…) est branché sur Claude, après validation de l'utilisateur. Utilise ce skill dès que l'utilisateur parle de mettre à jour son CRM, de remplir la fiche d'un deal, de logger un call, de prendre des notes après un rendez-vous, ou demande « mets à jour HubSpot », « fais mes notes CRM », « résume ce call pour le CRM », « c'est quoi la prochaine étape avec lui ? ».
---

> **Dans l'équipe commerciale** (lancé par le chef `/equipe`) : n'écris jamais dans le CRM toi-même, même si tu y as accès. Mets chaque changement dans `actions-a-valider.md` ; le chef le fait valider par l'utilisateur, puis l'exécute.

# Notes CRM

Tu transformes un call en notes CRM que le commercial (ou son manager) comprend en 10 secondes, dans 3 mois. Des notes vagues (« bon call, à relancer ») ne servent à rien. Des notes précises (le montant, la date, qui décide) font avancer le pipeline.

## 1. Avant de commencer

- **La transcription** : si elle n'est pas dans la conversation, demande-la : « Colle la transcription du call (dans Weecloz : onglet Transcript → Copier le transcript, ou n'importe quelle transcription avec les noms des interlocuteurs). »
- **Le contexte** : cherche `ma-vente.md` (dans les fichiers du Projet ou dans le dossier de travail) : il donne le nom du commercial dans les transcriptions, son offre, son process et son style. S'il n'existe pas, ne bloque pas : demande en une question le nom de l'utilisateur, ce qu'il vend et son client type, ou continue en déduisant qui est qui à partir du contenu, et préviens que la réponse sera plus générique. Utilise tels quels les noms d'étapes de sa rubrique « Mon process », pour que la note colle au CRM.
- **Le connecteur CRM** : regarde si un connecteur CRM est disponible dans tes outils.

## 2. Extrais du call

1. **L'étape** du deal à la fin du call (un nom du pipeline de `ma-vente.md`, sinon un nom simple : découverte, démo, proposition, négociation, signé, perdu).
2. **Le montant** dont on a parlé (avec ce qu'il comprend : honoraires, abonnement, durée).
3. **Le décideur**, et les autres personnes impliquées.
4. **La prochaine action** : qui fait quoi, et quand (date et heure exactes si elles ont été dites).
5. **Les risques** : ce qui peut faire capoter le deal, avec une citation du prospect.
6. **Le résumé** en 3 lignes.

## 3. Rends les notes

```
# Notes CRM : [prospect], [entreprise] — call du [date]

- **Étape** : …
- **Montant** : …
- **Décideur** : …
- **Prochaine action** : … — [date, heure]
- **Risques** :
  - [mm:ss] « … » : en quoi c'est un risque, en une ligne.
- **Résumé** :
  1. …
  2. …
  3. …
```

## 4. Mets à jour le CRM

- **Avec un connecteur CRM branché** : retrouve le contact et le deal dans le CRM. Montre à l'utilisateur, champ par champ, ce que tu vas changer (ancienne valeur → nouvelle valeur), et la note que tu vas ajouter. Attends son accord explicite avant d'écrire quoi que ce soit : une mise à jour du CRM est vue par toute l'équipe. Après l'écriture, confirme ce qui a été fait.
- **Sans connecteur** : rends les notes ci-dessus comme un bloc prêt à coller dans le CRM, et dis en une ligne que, si l'utilisateur branche le connecteur de son CRM sur Claude, tu pourras faire la mise à jour toi-même.

## Règles

- **Citations** : au format `[mm:ss] « phrase exacte »`, copiées mot pour mot (on peut couper avec « … »), avec la minute recopiée de la transcription. Sans minutes, cite sans minute.
- **Qui parle** : le commercial pilote et propose la suite ; le prospect dit ses besoins, ses freins et ses engagements. Si un label semble faux, fie-toi au contenu.
- **Aucune invention** : un champ sans info dans le call s'écrit « non abordé ».
- Tutoie l'utilisateur.
