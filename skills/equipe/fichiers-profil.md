# Les fichiers de profil

Le format exact de chaque fichier que tu écris dans le dossier de travail de l'utilisateur. Les agents les lisent tels quels : garde les titres.

## `mes-cibles.md`

```
# Mes cibles

## Cible 1 : [nom court, ex. Cabinets comptables AURA]
- Secteur : …
- Taille : … (effectif, chiffre d'affaires)
- Zone : … (régions, départements, villes ; France par défaut)
- Intitulés exacts des décideurs : …, …, …
- Ceux qui influencent : …
- Douleurs : …
- Déclencheurs d'achat : …
- Ne pas viser : …

## Cible 2 : …
```

Les intitulés sont écrits comme sur une carte de visite (« DAF », « Expert-comptable associé »), jamais comme une étiquette (« les décideurs finance »).

## `mes-outils.md`

```
# Mes outils

| Type | Outil | Connecteur dans Claude Code | Ce que l'équipe en fait |
|---|---|---|---|
| Enrichissement | FullEnrich | [nom du connecteur] | trouver l'email et le téléphone des décideurs validés |
| CRM | HubSpot | [nom du connecteur] | lire contacts et deals ; créer contacts, notes et tâches après accord |
| Mail | Gmail | [nom du connecteur] | créer des brouillons après accord ; jamais d'envoi |
| Séquences | lemlist | [nom du connecteur] | lire les statistiques ; charger une séquence en pause après accord |
```

Un outil que l'utilisateur possède mais qui n'est pas connecté : écris « pas connecté » dans la colonne Connecteur. L'équipe ne l'utilise pas, mais peut préparer un fichier à importer à la main (CSV).

## `messages-qui-marchent/gagnants.md` et `flops.md`

```
# Messages qui marchent

### [cible] — [canal : email / linkedin-message / séquence] — [jj/mm/aaaa]
[le texte exact du message, objet compris pour un email]

Résultat : [ex. réponse positive, rendez-vous pris, 4 réponses sur 30]
Pourquoi ça a marché : [si l'utilisateur le sait]
```

`flops.md` a le même format, avec « Pourquoi ça a échoué ».

## `actions-a-valider.md` (dans le dossier de la mission)

```
# Actions à valider

| # | Outil | Action | Contenu | Pourquoi |
|---|---|---|---|---|
| 1 | HubSpot | créer un contact | Claire Morel, Cabinet Morel, DAF, claire.morel@… | nouveau compte validé |
| 2 | lemlist | charger une séquence en pause | campagne « Cabinets AURA — oct. », 8 contacts | séquence de sequence.md |

Réponds « oui », « oui sauf 3, 5 » ou « non ».

## Résultat
| # | Fait ? | Détail |
|---|---|---|
```
