from  graphics   import *
from  time       import sleep
from  background import dusk, dawn
from  bounce     import bounce
from  button     import Button
from  in_shape   import in_circle, in_rectangle
from  utils      import show, hide, random_color_fill, shuffle

def make_title(w):
    (x, y) = (w.getWidth() / 2, w.getWidth() / 3)
    p = Point(x, y)

    t = Text(p, "The Hunger Games")
    t.setTextColor("yellow")

    return t

def make_egg():
    c = Circle(Point(250, -110), 200)
    c.setFill("black") # TODO: Change this.
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

    dusk(window)

    title = make_title(window)
    title.draw(window)

    bounce(title)

    time.sleep(0.5)
    egg = make_egg()

    (play, quit) = make_buttons()

    # TODO: Add the play button to the list of objects.
    objects = [egg, play, quit]

    show(window, objects)

    return (egg, title, play, quit)

def handle_egg(egg, title):
    print("  ==> Inside the Easter Egg circle.")

    rcolor = shuffle(["blue", "green", "yellow", "orange", "purple", "pink", "red"]).pop()
    egg.setFill(rcolor)
    bounce(title)

    return "splash"
def handle_play(w, objects):
    print("  ==> Inside the play button circle.")

    hide(objects)
    
    dawn(w)
    return "play"

def handle_quit(w, objects):
    print("  ==> Inside the quit button rectangle")
    hide(objects)

    dawn(w)
    w.close()

    return "quit"

def action(w, egg, title, play, quit):
    objects = [egg, title, play, quit]

    state = "splash"

    while state == "splash":

        click = w.getMouse()
        print("Click on %s" % click)

        if in_rectangle(click, quit.shape):
            state = handle_quit(w, objects)
        elif in_circle(click, play.shape):
            state = handle_play(w, objects)
        elif in_circle(click, egg):
            state = handle_egg(egg, title)
        

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
