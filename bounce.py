from graphics import *
from time     import sleep
from sys      import exit

def bounce(text):
    """
    argument(s):
      text :: text.

    side effects:
      step by step, change the font size of t from 5 to 32.

    return value: none.
    """

    # TODO: Change this.

    time.sleep(0.05)

def click(w, msg):
    print("Click anywhere in the window %s" % msg)
    print("  ==> you clicked on %s" % w.getMouse())

def init():
    w = GraphWin("test window", 500, 500)
    w.setBackground("black")
    t = Text(Point(250, 250), "Bounce")
    t.setTextColor("orange")
    t.draw(w)
    return (w, t)

def main():
    (w, t) = init()

    click(w, "to start bouncing.")

    for i in range(5):
        print("Bounce %d" % i)
        bounce(t)
        sleep(0.2)

    click(w, "to close the window and terminate the program.")
    w.close()

if __name__ == "__main__":
    main()
