from graphics import *
from time     import sleep
from utils    import dusk_colors, dawn_colors
from sys      import exit

def step_background(w, colors, delay):
    '''
    Argument(s)

    w      :: GraphWin
    colors :: List of colors
    delay  :: Delay in seconds between color changes. The delay may be
              a floating point number for subsecond precision.

    Side effects

    Changes the background of w to each of the colors in the provided list in sequence.
    The speed of the color sequence is controlled by the delay.

    Return value :: None
    '''

    for color in colors:
        w.setBackground(color)
        time.sleep(delay)
        

def dusk(w):
    '''
    Argument(s)

    w :: GraphWin

    Side effects

    Gradually change the background of w from white to black.

    Return value :: None
    '''

    step_background(w, dusk_colors(), 0.05)

    

def dawn(w):
    '''
    Argument(s)

    w :: GraphWin

    Side effects

    Gradually change the background of w from black to white.

    Return value :: None
    '''

    step_background(w, dawn_colors(), 0.05)

def sequence():
    return ["red", "blue", "pink", "green", "orange", "white"]

def init():
    w = GraphWin("Test window", 500, 500)
    w.setBackground("white")
    return w

def click_to(w, msg):
    print("Click anywhere in the window to %s" % msg)
    print("  ==> You clicked on %s" % w.getMouse())

def test_from_dusk_to_dawn(w):

    click_to(w, "go from dusk ...")

    dusk(w)
    dawn(w)

    print("... to dawn.")


def test_step_background(w):

    colors = sequence()

    print("Color sequence %s" % colors)

    click_to(w, "step the background slow.")
    step_background(w, colors, 1)

    click_to(w, "step the background fast.")
    step_background(w, colors, 0.2)

def test_set_background(w):
    click_to(w, "set the background to yellow.")
    w.setBackground("yellow")

    click_to(w, "set the background to red.")
    w.setBackground("red")

    click_to(w, "set the background to white.")
    w.setBackground("white")

def main():
    w = init()

    test_set_background(w)
    # test_step_background(w)
    # test_from_dusk_to_dawn(w)

    click_to(w, "close the window.")
    w.close()

if __name__ == "__main__":
    main()
