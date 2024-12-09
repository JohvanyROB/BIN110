__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2024, BIN110 - Algorithmie, IPSA 2024"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"


from my_game.game import Game
from my_game.gui import GUI
from my_game.bot import play

from time import sleep
from threading import Thread

import argparse, os


def thread_function():
    """ 
        Function that runs in background when step 1 of the project has been validated by the teacher.
        In this function, the game handler gets the player move and update its state and pose accordingly.
        Then, the game window is updated.
        Once the game is over (wall hit or treasure found), a final display appears on the game window.
        3 seconds later, the game is completely stopped.
    """
    global game, gui, player_info
    while game.player_state == game.victory_rule["continue"]:
        game.process(play(args.mode, environment, player_info["pose"]))
        player_info = game.get_player_info()
        gui.set_player_pose(player_info["pose"])
        sleep(args.period)
    if game.player_state == game.victory_rule["win"]:
        gui.set_player_state("victory")
    else:
        gui.set_player_state("defeat")
    gui.mode = "final"
    sleep(3)
    gui.running = False


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--player_name", help="Name of the player", type=str, default="Jack")
parser.add_argument("-m", "--mode", help="Behaviour of the agent", type=str, default="do_nothing")
parser.add_argument("-p", "--period", help="Period between two consecutive moves", type=float, default=1.0)
args = parser.parse_args()

if os.name == "nt": #if you are on Windows
    screen_resolution_to_fix = False  #Set this boolean to True if you face window resolution issues
    if screen_resolution_to_fix:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  #Resolve the window resolution issue
    

game = Game()
player_info = game.get_player_info()
environment = game.get_env()

gui = GUI(player_pose=player_info["pose"], env=environment, player_name=args.player_name)

#TODO: Decommenter les 2 lignes suivantes uniquement apres validation de l'etape 1!
# t = Thread(target=thread_function, daemon=True)
# t.start()

try:
    while gui.running:
        gui.on_render()
except KeyboardInterrupt:
    print("Ctrl+C pressed, shutting down the process...")
finally:
    gui.on_cleanup()