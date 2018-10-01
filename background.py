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

    Change the background of w to each of the colors in the provided list in sequence.
    The speed of the color sequence is controlled by the delay.

    Return value :: None
    '''

    # TODO: Change this.
    time.sleep(delay)

def dusk(w):
    '''
    Argument(s)

    w :: GraphWin

    Side effects

    Gradually change the background of w from white to black.

    Return value :: None
    '''

    colors = dusk_colors()

    # TODO: use step_background()

def dawn(w):
    '''
    Argument(s)

    w :: GraphWin

    Side effects

    Gradually change the background of w from black to white.

    Return value :: None
    '''

    colors = dawn_colors()

    # TODO: use step_background()

def sequence():
    return ["red", "blue", "pink", "green", "orange", "white"]

def init():
    w = GraphWin("Test window", 500, 500)
    w.setBackground("white")
    return w

def pause(w, msg):
    print("Click anywhere in the window to %s" % msg)
    print("  ==> You clicked on %s" % w.getMouse())

def test_from_dusk_to_dawn():
    w = init()

    print("From dusk ...")
    dusk(w)

    print("... to dawn.")
    dawn(w)

    pause(w, "close the window.")
    w.close()

def test_step_background():
    w = init()

    colors = sequence()

    print("Color sequence %s" % colors)

    print("Step slow.")
    step_background(w, colors, 1)

    print("Step fast.")
    step_background(w, colors, 0.2)

    pause(w, "close the window.")
    w.close()

def test_all():
    w = init()

    pause(w, "set the background to yellow.")
    w.setBackground("yellow")

    pause(w, "set the background to red.")
    w.setBackground("red")

    pause(w, "set the background to white.")
    w.setBackground("white")

    pause(w, "step the background slowly.")
    colors = ["red", "blue", "pink", "green", "orange", "white"]
    step_background(w, colors, 1)

    pause(w, "step the background quickly.")
    step_background(w, colors, 0.2)

    pause(w, "dim the background using dusk().")
    dusk(w)

    pause(w, "brighten the background using dawn().")
    dawn(w)

    pause(w, "close the window.")
    w.close()

def main():
    # test_step_background()
    # test_from_dusk_to_dawn()
    test_all()

if __name__ == "__main__":
    main()
