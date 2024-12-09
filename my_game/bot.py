__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2024, BIN110 - Algorithmie, IPSA 2024"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"

ALLOWED_MOVES = {"do_nothing": 0, "move_left": 1, "move_right": 2, "move_up": 3, "move_down": 4}   #dictionnaire contenant les differents coups possibles

def play(mode, env, pose):  #NE PAS TOUCHER!
    """
    Parameters
    ----------
    mode : str
        Mode de fonctionnement du personnage: "manual", "random", "smart" ou "do_nothing".
    env: dict
        Dictionnaire contenant la matrice 2D représentant l'envirionnement ainsi que ses dimensions.
    pose: tuple
        Tuple contenant les coordonnées (x, y) du personnage. La position (0, 0) correspond au coin supérieur gauche de l'environnement.
    
    Returns
    ------
    int
        La valeur correspondant au coup que souhaite réaliser le personnage.
    """
    if mode == "manual":
        return manual_move()
    elif mode == "random":
        return random_move(env, pose)
    elif mode == "smart":
        return smart_move(env, pose)
    else:
        return do_nothing()
    

def do_nothing():
    """Le personnage restera sur place à chaque itération.

    Returns
    ------
    int
        La valeur correspondant au coup 'do_nothing'.
    """
    pass
    #TODO


def manual_move():
    """Le personnage sera contrôlé par le joueur.

    Returns
    ------
    int
        La valeur correspondant au coup choisi par l'utilisateur.
    """
    pass
    #TODO



def random_move(env, player_pose):
    """Le personnage se déplacera de manière aléatoire dans le labyrinthe tout en évitant les obstacles.
    
    Parameters
    ----------
    env: dict
        Dictionnaire contenant la matrice 2D représentant l'environnement ainsi que ses dimensions.
    player_pose: tuple
        Coordonnées (x, y) du personnage. La position (0, 0) correspond au coin supérieur gauche de l'environnement.
    
    Returns
    ------
    int
        La valeur correspondant au coup choisi aléatoirement par le bot. Ce coup doit lui éviter de rentrer en collision avec un mur.
    """
    pass
    #TODO



def smart_move(env, player_pose):
    """Le personnage se déplacera intelligemment dans le labyrinthe afin de récupérer le trésor le plus vite possible tout en évitant les obstacles.
    
    Parameters
    ----------
    env: dict
        Dictionnaire contenant la matrice 2D représentant l'environnement ainsi que ses dimensions.
    player_pose: tuple
        Coordonnées (x, y) du personnage. La position (0, 0) correspond au coin supérieur gauche de l'environnement.
    
    Returns
    ------
    int
        La valeur correspondant au coup choisi par le bot.
    """
    pass
    #TODO
