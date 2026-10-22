#!/usr/bin/env python3
"""Contrôle les messages de prospection d'un fichier avant de les montrer à l'utilisateur.

Chaque message commence par une ligne « ### <compte> — <canal> <n°> ».
Canaux : email, email-rupture, linkedin-invitation, linkedin-message.
Usage : python3 verifier_message.py <fichier>
"""
import re
import sys
from pathlib import Path

LIMITES = {"email": 75, "email-rupture": 40, "linkedin-message": 60}
UNE_QUESTION = {"email", "linkedin-message"}
LISTE_NOIRE = ["j'espère que vous allez bien", "j'espère que tu vas bien", "je me permets",
               "n'hésitez pas", "n'hésite pas", "je reviens vers", "petite question", "booster",
               "levier", "synergie", "solution innovante", "révolutionn", "incontournable",
               "game changer", "—", "!"]
SALUT = re.compile(r"^(bonjour|salut|hello|bonsoir)\b[^\n]*,\s*$", re.I)
ENTETE = re.compile(r"^###\s+(.+?)\s+—\s+([a-z-]+)\s*(\d*)\s*$")


def _blocs(text: str):
    blocs, cur = [], None
    for line in text.replace("’", "'").splitlines():
        m = ENTETE.match(line.strip())
        if m:
            cur = {"titre": line.strip()[4:], "canal": m.group(2), "lignes": []}
            blocs.append(cur)
        elif cur is not None:
            cur["lignes"].append(line)
    return blocs


def _check(b) -> list[str]:
    t, canal, errs = b["titre"], b["canal"], []
    lignes = [l for l in b["lignes"]]
    if canal not in LIMITES and canal != "linkedin-invitation":
        return [f"{t} : canal inconnu « {canal} »"]
    objet = None
    if canal.startswith("email"):
        idx = next((i for i, l in enumerate(lignes) if l.strip().lower().startswith("objet")), None)
        if idx is None:
            errs.append(f"{t} : objet manquant")
        else:
            objet = lignes.pop(idx).split(":", 1)[1].strip() if ":" in lignes[idx] else ""
    corps_lignes = [l.strip() for l in lignes if l.strip()]
    if canal == "linkedin-invitation":
        if corps_lignes and corps_lignes != ["(sans note)"]:
            errs.append(f"{t} : une invitation LinkedIn part sans note")
        return errs
    if corps_lignes and SALUT.match(corps_lignes[0]):
        corps_lignes = corps_lignes[1:]
    corps = " ".join(corps_lignes)
    mots = len(corps.split())
    if mots > LIMITES[canal]:
        errs.append(f"{t} : {mots} mots, {LIMITES[canal]} au plus")
    q = corps.count("?")
    if canal in UNE_QUESTION and q != 1:
        errs.append(f"{t} : {q} question(s), il en faut exactement une")
    if canal == "email-rupture" and q > 1:
        errs.append(f"{t} : {q} questions, une au plus")
    bas = corps.lower()
    for w in LISTE_NOIRE:
        if w in bas:
            errs.append(f"{t} : formule interdite « {w} »")
    if re.match(r"^(je|nous)\b", bas):
        errs.append(f"{t} : le message commence par « Je » ou « Nous »")
    brut = " ".join(b["lignes"]) + " " + (objet or "")
    if "[" in brut or "]" in brut:
        errs.append(f"{t} : un [crochet] n'a pas été rempli")
    if objet is not None:
        n = len(objet.split())
        if not 2 <= n <= 5:
            errs.append(f"{t} : objet de {n} mots (2 à 5)")
        if objet[:1] != objet[:1].lower():
            errs.append(f"{t} : l'objet commence par une majuscule")
        if re.match(r"^(re|fwd|tr)\s*:", objet.lower()):
            errs.append(f"{t} : objet en faux « re: » / « fwd: »")
    return errs


def check_text(text: str) -> list[str]:
    blocs = _blocs(text)
    if not blocs:
        return ["aucun message trouvé (en-tête attendu : ### <compte> — <canal> <n°>)"]
    return [e for b in blocs for e in _check(b)]


def check_file(path) -> list[str]:
    return check_text(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    errs = check_file(sys.argv[1])
    n = len(_blocs(Path(sys.argv[1]).read_text(encoding="utf-8")))
    print(f"OK ({n} messages)" if not errs else "\n".join(errs))
    sys.exit(1 if errs else 0)
