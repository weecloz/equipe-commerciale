# Les emails de prospection

## Avant d'écrire

Tu écris **uniquement à partir du bloc de faits du compte** (`faits.md`) : le décideur, son poste, les faits sourcés, le signal retenu et l'angle. Si un fait n'y est pas, tu ne le connais pas. Pas de « j'ai vu votre post », pas de chiffre, pas de client commun, pas de levée qui n'y figure pas.

Puis tu relis les **gagnants** de l'utilisateur pour cette cible (`messages-qui-marchent/gagnants.md`) : ce sont tes premiers modèles.

## L'email 1

- **Moins de 75 mots**, sans compter la salutation. Les dirigeants : vise 50.
- **Une observation précise sur ce compte-là**, tirée des faits, puis **une seule question**. Pas deux, pas zéro. Une généralité sur son secteur (« dans les cabinets comptables, la saison des bilans est chargée ») n'est pas une observation : n'importe qui la recevrait.
- **Pas de pitch, pas le nom du produit, pas de lien, pas de pièce jointe.** Le premier email sert à ouvrir une conversation, pas à vendre.
- **Il parle de lui, pas de toi** : il ne commence jamais par « Je » ni « Nous ». La première phrase porte sur sa situation.
- **D'égal à égal** : écris comme un pair qui connaît son métier, pas comme un fournisseur qui demande un rendez-vous.

### Les 4 déclencheurs de réponse

Construis l'email autour d'un seul :

1. **La reconnaissance** : un détail vrai et précis sur sa situation, qui lui fait penser « il sait ce que je vis ».
2. **La curiosité** : tu sais quelque chose d'utile pour lui (un constat sur son secteur, un écart sur son site). Ne l'utilise que si tu peux vraiment le lui donner ensuite.
3. **Le oui facile** : une proposition qui ne coûte rien à accepter (« je vous envoie l'analyse ? »). Ça marche mieux qu'une demande de rendez-vous.
4. **La preuve d'un pair** : un client réel de l'utilisateur, proche de lui, avec un résultat concret. Seulement s'il est dans `ma-vente.md`.

### La question

- Une question à laquelle il peut répondre en une ligne.
- Mieux vaut « C'est un sujet chez vous en ce moment ? » ou « Je vous envoie l'analyse ? » que « Seriez-vous disponible jeudi à 14 h pour un échange de 30 minutes ? ».

## La signature et la sortie

Pas de signature dans les blocs : elle est ajoutée à l'envoi. Sous la signature, chaque email de prospection porte une ligne de sortie simple (« Si ce n'est pas un sujet pour vous, dites-le-moi et je ne vous écrirai plus. »). Elle ne compte pas dans les 75 mots.

## L'objet

- **2 à 5 mots**, qui commencent par une minuscule, comme un mail entre collègues.
- Il commence par une minuscule : s'il doit commencer par un nom propre, reformule (« la paie à Lyon » plutôt que « Lyon et la paie »).
- Il parle de son sujet, pas de ton offre : « la saison fiscale », « vos 3 recrutements », « collecte des pièces ».
- Jamais son prénom, jamais de faux « Re: » ou « Fwd: », jamais de « Petite question », jamais de point d'exclamation.

## La séquence

| Jour | Message | Règle |
|---|---|---|
| J0 | email 1 | observation + une question, moins de 75 mots |
| J3 | email 2 | **un nouvel angle** (un autre signal ou une autre douleur) et **une preuve concrète** tirée de `ma-vente.md` ; nouvel objet ; ne fait jamais référence au premier email (« je reviens vers vous » est interdit) ; moins de 75 mots |
| J7 | email-rupture 3 | moins de 40 mots, sans pitch ni culpabilisation ; laisse la porte ouverte |

Sur LinkedIn, la séquence vit à part (voir `linkedin.md`). Une réponse, même un « non », arrête tout de suite la séquence sur tous les canaux.

## Exemples au bon format

```
### Cabinet Morel — email 1
Objet : la saison fiscale

Bonjour Claire,

Trois offres de collaborateur comptable sur votre page carrières depuis septembre, en pleine préparation des bilans. En attendant les recrues, comment l'équipe absorbe les dossiers en plus ?
```

```
### Cabinet Morel — email 2
Objet : 4 heures par dossier

Bonjour Claire,

Un cabinet de 15 personnes à Clermont-Ferrand a gagné 4 heures de révision par dossier en automatisant la collecte des pièces. C'est le genre de marge qui aide pendant un recrutement. Je vous montre comment ils s'y sont pris ?
```

```
### Cabinet Morel — email-rupture 3
Objet : je clos le sujet

Bonjour Claire,

Sans nouvelles de votre part, j'en déduis que ce n'est pas le moment et je ne vous relance plus. Si la collecte des pièces redevient un sujet, un mot suffit.
```

*(Le cabinet et le chiffre de l'email 2 sont des exemples : dans un vrai message, la preuve vient de `ma-vente.md`.)*

## La relecture

Avant de rendre, relis chaque email :
1. Le prospect pourrait-il penser qu'un robot l'a écrit ? Si oui, réécris.
2. Chaque affirmation sur lui vient-elle de `faits.md` ?
3. Une seule idée, une seule question ?
4. Aucune formule de `style.md` ?
5. Est-ce que **toi**, tu répondrais ?

Puis lance `verifier_message.py`.
