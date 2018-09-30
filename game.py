from graphics import *
from sys      import exit
from time     import sleep
from utils    import show, hide, take, shuffle
from splash   import splash
from grid     import Grid
from sprite   import Sprite

def move_position(position, key):
    '''
    Argument(s)

       position :: a tuple (x1, y1)
            key :: string ("Right", "Left", "Up", "Down")

    Side effects :: None

    Return value :: tuple (x2, y2)
       The new position after moving one step according to key.
    '''

    (x, y) = position

    # TODO: Add code here.

    return (x, y)


def move_hero(hero, key):
    hero.move(move_position(hero.position, key))

def positions():
    return [(x,y) for x in range(5) for y in range(5)]

def random_positions(n):
    return take(shuffle(positions()), n)

def spawn():
    [pos1, pos2] = random_positions(2)
    hero   = Sprite(pos1, 35, "yellow")
    food   = Sprite(pos2, 20, "red")
    return (hero, food)

def eat(hero, food):
   return hero.position == food.position

def init(w):
   w.setBackground("white")
   grid = Grid()
   (hero, food) = spawn()

   objects = (grid, hero, food)

   show(w, objects)

   return objects

def game(w):
    """
    Argument(s):
      w :: Graphical window.

    Side effects:
      Let the user play the game by moving the hero around on the grid.
    """

    objects = init(w)
    (grid, hero, food) = objects

    play = True

    while play:
        key = w.getKey()
        print(key)
        move_hero(hero, key)

        # TODO: Make the game end.

    print("Game over!")
    hide(objects)


def main():
    """
    The main function of the game.

    Side effects:
      Shows a splash screen.
      When the player clicks on the play button, lets the user play the game.
      If the user clicks on the quit button, close the window.
    """

    w = GraphWin("The Hunger Games", 500, 500)
    input("")

    while True:
        action = splash(w)
        if action == "quit":
            print("So Long, and Thanks for All the Fish!")
            w.close()
            exit()
        elif action == "play":
            game(w)

if __name__ == "__main__":
    main()
