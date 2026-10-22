---
name: outbound
description: Savoir de prospection B2B en France pour les agents de l'équipe — signaux d'achat et où les trouver, anatomie des emails et des séquences, règles LinkedIn, style et liste noire, exemples bons et mauvais, volumes et délivrabilité, plus un script qui contrôle chaque message. Utilisé par les agents de stratégie, de recherche, de prospection, de qualification et de relance, pas directement par l'utilisateur.
user-invocable: false
---

# Prospection outbound

Ce skill rassemble ce qu'il faut savoir pour trouver, analyser et contacter des prospects B2B en France sans écrire de messages génériques. Un message générique ne reçoit pas de réponse : tout ce qui suit sert à écrire un message que seul ce prospect pouvait recevoir.

## Quel fichier lire

| Tu dois… | Lis |
|---|---|
| trouver ou choisir un signal, un angle | `signaux.md` |
| écrire un email ou une séquence | `email.md`, puis `style.md` |
| écrire pour LinkedIn | `linkedin.md`, puis `style.md` |
| t'inspirer d'exemples | les gagnants de l'utilisateur d'abord, puis `exemples.md` |
| décider combien contacter, quand, et à quel rythme | `regles-volume.md` |

## L'ordre des modèles

1. **Les messages qui ont marché pour l'utilisateur** : `messages-qui-marchent/gagnants.md` dans son dossier de travail, en priorité ceux de la cible visée. Reprends leur longueur, leur structure, leur façon d'ouvrir et de poser la question, leur registre. Ne recopie jamais leurs faits : ils parlaient d'un autre prospect.
2. **`exemples.md`** de ce skill, si l'utilisateur n'a pas encore de gagnants. Dis-le dans ta réponse au chef (« pas encore de messages gagnants : je me suis appuyé sur les exemples de base »).
3. **Évite tout ce qui ressemble à `messages-qui-marchent/flops.md`** : même ouverture, même angle, même longueur.

## Le contrôle

Toute rédaction de prospection à froid (emails, LinkedIn, séquences, demande de recommandation) se termine par le script ci-dessous. Une relance après un call suit le skill `relance` et n'y passe pas.

```
python3 <dossier de ce skill>/scripts/verifier_message.py <ton fichier de messages>
```

Le script lit les messages au format suivant (un bloc par message, sans signature) :

```
### <compte> — <canal> <n°>
Objet : <objet>          (emails seulement)

<corps du message>
```

Canaux : `email`, `email-rupture`, `linkedin-invitation`, `linkedin-message`. Pour une invitation LinkedIn, le corps est exactement `(sans note)`.

S'il répond autre chose que `OK`, réécris les messages signalés et relance-le, **3 fois au plus** ; s'il reste des défauts, rends la main au chef en les listant. Si Python n'est pas installé sur l'ordinateur (la commande échoue ou ouvre une fenêtre d'installation), ne réessaie pas : vérifie chaque message à la main avec les règles ci-dessous et dis-le au chef.

Les règles du script : email ≤ 75 mots et une seule question ; rupture ≤ 40 mots ; message LinkedIn ≤ 60 mots et une seule question ; invitation `(sans note)` ; objet de 2 à 5 mots commençant par une minuscule, sans « re: » ; ni « Je », « J' » ni « Nous » en tête ; aucun lien ; aucune formule de `style.md` ; aucune donnée du registre récitée ; pas deux messages avec la même ouverture ou la même question. Le script ne voit pas tout : relis aussi chaque message avec la grille de `style.md`.
