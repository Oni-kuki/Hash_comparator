import hashlib
hashtos = input("Give the Hash in Md5 : ")
path_dictionnary = input("give the link to the dictionnary : ")
def hash_text(text):
    #fonction pour hasher
    hasher = hashlib.md5()
    hasher.update(text.encode())
    return hasher.hexdigest()
with open(path_dictionnary, "r",encoding="latin-1") as file:
    # lire le fichier
    for line in file:
        new_line = line.replace("\n", "") # enlever tous les espace de fin de ligne
        # hasher chacune des lignes 
        hashed_line = hash_text(new_line)
        if hashed_line == hashtos:
            # si on trouve le hash on print la ligne de résultat
            print(new_line)
