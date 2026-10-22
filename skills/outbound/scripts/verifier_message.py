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
SALUT_EN_TETE = re.compile(r"^(bonjour|salut|hello|bonsoir)\b[^,\n]{0,40},\s*", re.I)
URL = re.compile(r"(https?://\S+|www\.\S+)", re.I)
REGISTRE = re.compile(r"(entre\s+\S+\s+et\s+\S+\s+(salariés|personnes|employés)|code\s+naf|\bnaf\b|chiffre d'affaires de)", re.I)
ENTETE = re.compile(r"^###\s+(.+?)\s+—\s+([a-z-]+)\s*(\d*)\s*$")


def _blocs(text: str):
    blocs, cur = [], None
    for line in text.replace("’", "'").splitlines():
        m = ENTETE.match(line.strip())
        if m:
            cur = {"titre": line.strip()[4:], "canal": m.group(2), "lignes": []}
            blocs.append(cur)
        elif cur is not None:
            brut = line.strip()
            if brut.startswith("```") or re.match(r"^#{1,2}\s", brut) or re.match(r"^#{4,}\s", brut):
                cur = None  # fin du bloc : ce qui suit n'est plus le message
            else:
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
    corps = SALUT_EN_TETE.sub("", corps, count=1) if SALUT_EN_TETE.match(corps) else corps
    liens = URL.findall(corps)
    sans_liens = URL.sub(" ", corps)
    mots = len(corps.split())
    if mots > LIMITES[canal]:
        errs.append(f"{t} : {mots} mots, {LIMITES[canal]} au plus")
    q = sans_liens.count("?")
    if liens and canal in ("email", "linkedin-message"):
        errs.append(f"{t} : pas de lien dans un premier contact ({liens[0]})")
    if REGISTRE.search(corps):
        errs.append(f"{t} : donnée du registre récitée (« {REGISTRE.search(corps).group(0)} ») : dis-le comme on le dirait à voix haute")
    if canal in UNE_QUESTION and q != 1:
        errs.append(f"{t} : {q} question(s), il en faut exactement une")
    if canal == "email-rupture" and q > 1:
        errs.append(f"{t} : {q} questions, une au plus")
    bas = corps.lower()
    for w in LISTE_NOIRE:
        if w in bas:
            errs.append(f"{t} : formule interdite « {w} »")
    if re.match(r"^(je\b|j'|nous\b)", bas):
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


def _corps(b) -> str:
    lignes = [l.strip() for l in b["lignes"] if l.strip() and not l.strip().lower().startswith("objet")]
    if lignes and SALUT.match(lignes[0]):
        lignes = lignes[1:]
    return " ".join(lignes)


def _norme(t: str) -> str:
    return " ".join(re.sub(r"[^\w\s]", " ", t.lower()).split())


def _repetitions(blocs) -> list[str]:
    """Deux messages d'un même fichier ne doivent pas ouvrir ni questionner de la même façon."""
    errs, vus_ouv, vus_q = [], {}, {}
    for b in blocs:
        if b["canal"] not in LIMITES:
            continue
        corps = _corps(b)
        ouverture = " ".join(_norme(corps).split()[:6])
        phrases = re.split(r"(?<=[.?])\s+", corps)
        question = {w for w in next((_norme(p) for p in phrases if "?" in p), "").split() if len(w) > 3}
        if ouverture and ouverture in vus_ouv:
            errs.append(f"{b['titre']} : même ouverture que « {vus_ouv[ouverture]} »")
        vus_ouv.setdefault(ouverture, b["titre"])
        for autre, mots in vus_q.items():
            if question and mots and len(question & mots) / len(question | mots) >= 0.5:
                errs.append(f"{b['titre']} : même question que « {autre} » (varie la question d'un compte à l'autre)")
                break
        vus_q[b["titre"]] = question
    return errs


def check_text(text: str) -> list[str]:
    blocs = _blocs(text)
    if not blocs:
        return ["aucun message trouvé (en-tête attendu : ### <compte> — <canal> <n°>)"]
    return [e for b in blocs for e in _check(b)] + _repetitions(blocs)


def check_file(path) -> list[str]:
    return check_text(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    errs = check_file(sys.argv[1])
    n = len(_blocs(Path(sys.argv[1]).read_text(encoding="utf-8")))
    print(f"OK ({n} messages)" if not errs else "\n".join(errs))
    sys.exit(1 if errs else 0)
