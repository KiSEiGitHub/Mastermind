from random import randint

"""
Programme Mastermind
Divisé en trois fonctions
    - newCode() : qui génère le code à trouver
    - Game() : La fonction qui nous fait jouer
    - Main() : qui appel Game()
"""


def newCode():
    """
    Étape 1 :
        D'abord on définit notre Code en tant que chaîne de caractère vide.
        Car on va devoir remplir cette variable.
        Avec une variable qui génère un nombre aléatoire entre 1 - 6.
    Étape 2 :
        - On utilise une boucle tant qui va tourner sous la condition
        len(Code) < 5.
        On définit ensuite notre variable qui nous génère le nombre aléatoire entre 1 - 6
        - On utilise une condition pour contrôler si le nombre généré est déjà présent dans
        la chaîne de caractère que contient la variable Code.
        Si oui, alors on ne fait rien. Si non alors Code += nb, vue que c'est du string quand on fait
        une addition de variable de type str, alors elle se "colle entre elle".
        Donc le code, c'est techniquement pas 1 str mais 5 str collé
        - la boucle va touner tant que le code n'a pas une longueur de 5 ET de 5 chiffres différent
        - Ensuite une fois que c'est bon, alors on peut return Code
    """
    Code = ""
    while len(Code) < 5:
        nb = str((randint(1, 6)))
        if nb in Code:
            continue
        else:
            Code += nb
    return Code


def Game():
    code = newCode()  # on récupère notre return qu'on stocke dans une autre variable
    Tentative = 2  # on définit les tentatives sur 12
    choix = ""  # on définit notre choix en tant que chaine vide pour pouvoir controler chaque index d'str

    """
    - Notre jeu et le fait qu'on puisse recommencer, tourne sous une boucle while 
    tant que notre choix est différent de code

    - On définit nos variables de gestion directement après la boucle. 
    Pourquoi dans la boucle et pas avant la boucle ?
    Tout simplement parce qu'à la fin on nous dit combien sont bien placé, mal placé ou pas dans le code
    c'est var de gestion sont des variables compteuse, mais elle doivent se reset au prochain tour c'est important 
    dans le jeu. Au cas ou si l'utilisateur test un nouveau code, pour pouvoir lui redire combien sont mal ou bien placé 
    voir pas dans le code.

    - if len(choix) > 5 or len(choix) < 5
    C'est pour controler si l'utilisateur rentre un code valide
    Tout se passe dans le else

    - else 
    Vue qu'on au final deux string, il faut faire de la comparaison d'index de string
    par exemple MaVariable[0] = lettre de MaVariable à l'indice ou index 0

    - Du coup il faut à chaque fois comparé choix[0] et code[0]
    a chaque fois le 0 change et +1 donc il faut faire une boucle for

    - Quelle condition pour la boucle for ? parce que oui, une boucle for tourne sous une 
    condition elle aussi

    La condition est simple tant que i < 5. Pourquoi 5 ? car le code à 5 chiffres 
    """
    print(code)
    while choix != code:
        nb_bien_place = 0
        nb_mal_place = 0
        pas_dans_le_code = 0
        # Le code commence ici
        choix = input('>> ')  # pour entrer notre choix
        if len(choix) > 5 or len(choix) < 5:
            print('Vous devez rentrer un code à 5 chiffres')
        else:
            for i in range(5):
                if choix[i] == code[i]:
                    nb_bien_place += 1
                elif choix[i] != code[i]:
                    if choix[i] not in code:
                        pas_dans_le_code += 1
                    else:
                        nb_mal_place += 1

        # à chaque fin de tour on controle s'il nous reste des essais
        Tentative -= 1
        if Tentative < 1:
            print('Vous avez perdu')
            break
        elif code == choix:
            print('Vous avez gagner')
            break
        else:
            print('-' * 20)
            print(f"Bien placé(s) : {nb_bien_place} ")
            print(f"mal placé(s): {nb_mal_place} ")
            print(f"pas dans le code : {pas_dans_le_code} ")
            print(f"Nombre de tentatives restante : {Tentative}")


def Main():
    # appel juste Game
    Game()


if __name__ == '__main__':
    Main()
