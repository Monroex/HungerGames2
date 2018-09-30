from  graphics   import *
from  time       import sleep
from  background import dusk, dawn
from  bounce     import bounce
from  button     import Button
from  in_shape   import in_circle, in_rectangle
from  utils      import show, hide, random_color_fill

def make_title(w):
    (x, y) = (w.getWidth() / 2, w.getWidth() / 3)
    p = Point(x, y)

    # TODO: Change this.
    t = Text(p, "The Name of the Game")

    # TODO: Change this.
    t.setTextColor("blue")

    return t

def make_egg():
    c = Circle(Point(250, -110), 200)
    c.setFill("blue") # TODO: Change this.
    return c

def make_buttons():
    c = Circle(Point(170, 300), 40)
    c.setFill("red")
    play = Button(c, "play")

    r = Rectangle(Point(290, 260), Point(370, 340))
    r.setFill("red")
    quit = Button(r, "quit")

    return (play, quit)

def init(window):

    # TODO: Make the window background dim from white to black.

    title = make_title(window)
    title.draw(window)

    # TODO: Make the title text bounce.

    time.sleep(0.5)
    egg = make_egg()

    (play, quit) = make_buttons()

    # TODO: Add the play button to the list of objects.
    objects = [egg]

    show(window, objects)

    return (egg, title, play, quit)

def handle_egg(egg, title):
    print("  ==> Inside the Easter Egg circle.")

    # TODO: Make the Easter egg circle change to a random color.

    bounce(title)

def handle_play(w, objects):
    print("  ==> Inside the play button circle.")

    # TODO: Hide the objects.

    dawn(w)
    return "play"

def handle_quit(w, objects):
    print("  ==> Inside the quit button rectangle")
    hide(objects)

    # TODO: Fade the window background from black to white.

    return "quit"

def action(w, egg, title, play, quit):
    objects = [egg, title, play, quit]

    state = "splash"

    while state == "splash":

        click = w.getMouse()
        print("Click on %s" % click)

        if in_rectangle(click, quit.shape):
            state = handle_quit(w, objects)

        # TODO: Add code here to detect and handle click on the
        # Easter egg and play button.

    return state

def splash(window):
    """
    Argument(s)
      w :: Graphical window.

    Side effects
      Shows the splash screen with a play button, a quit button,
      the title text "The Hunger Games" and a hidden
      Easter egg.

      When the user clicks on the hidden Easter egg area of the
      splash screen, the Easter egg are changes to a random color.

    Return value :: string
      Returns "play" if the user clicks on the play button.
      Returns "quit" if the user clicks on the quit button.
    """

    (egg, title, play, quit) = init(window)

    a = action(window, egg, title, play, quit)

    print("Action = %s" % a)

    return a

def main():
    window = GraphWin("The Hunger Games", 500, 500)
    window.setBackground("white")

    splash(window)

if __name__ == "__main__":
    main()
