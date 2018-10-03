from graphics import *
from button import Button
from in_shape import in_circle, in_rectangle
from sys import exit

def pause(w, msg):
    print("Click anywhere in the window %s" % msg)
    print("  ==> You clicked on %s" % w.getMouse())

def init():

    w = window()

    border = 5

    c = Circle(Point(250, 150), 100)
    c.setWidth(border)
    c.setFill("yellow")

    play = Button(c, "play")
    play.draw(w)

    r = Rectangle(Point(100, 350), Point(400, 450))
    r.setWidth(border)
    r.setFill("red")

    quit = Button(r, "quit")
    quit.draw(w)
    return (w, play, quit)

def handle_play():
    print("  ==> inside the play button.")

def handle_quit(w):
    print("  ==> inside the quit button.")
    print("  ==> close the window")
    w.close()
    print("  ==> terminate")
    exit()

def main():

    (w, play, quit) = init()

    while True:
        p = w.getMouse()
        print("You clicked on %s" % p)

        if in_circle(p, play.getShape()):
            handle_play()
        elif in_rectangle(p, quit.getShape()):
            handle_quit(w)
        

def window():
    w = GraphWin("Test window", 500, 500)
    w.setBackground("white")

    return w

if __name__ == "__main__":
    main()
