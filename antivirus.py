
import os
import hashlib

APP_NAME = "MIRA ANTIVIRUS"

def analyser_fichier(chemin):
    if not os.path.isfile(chemin):
        return "Fichier introuvable"

    sha256 = hashlib.sha256()

    with open(chemin, "rb") as fichier:
        for bloc in iter(lambda: fichier.read(4096), b""):
            sha256.update(bloc)

    empreinte = sha256.hexdigest()

    return {
        "fichier": os.path.basename(chemin),
        "sha256": empreinte,
        "statut": "Analyse terminee",
        "message": "Empreinte calculee. Menace non determinee."
    }

if __name__ == "__main__":
    print("=" * 35)
    print("       MIRA ANTIVIRUS")
    print("=" * 35)

    chemin = input("Chemin du fichier a analyser : ")
    resultat = analyser_fichier(chemin)

    print(resultat)

