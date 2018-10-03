from graphics import *

def in_circle(p, c):
    """
    Argument(s):
      p :: Point
      c :: Circle

    Return value :: Bool
      True if p is inside the circle c, otherwise False.
    """

    dx = c.getCenter().x - p.x
    dy = c.getCenter().y - p.y
    distance = dx**2 + dy **2

    if distance >= c.getRadius()**2:
        return False
    else:
        return True

def in_rectangle(p, r):
    """
    Argument(s):
      p :: Point.
      r :: Rectangle.

    Return value:: Bool.
      True if p is inside the rectangle r, otherwise False.
    """

    if r.p1.x <= p.x <= r.p2.x and r.p1.y <= p.y <= r.p2.y:
        return True
    else:
        return False

def pause(w, msg):
    print("Click anywhere in the window %s" % msg)
    print("  ==> You clicked on %s" % w.getMouse())

def init():
    w = window()

    border = 5
    c1 = Circle(Point(150, 150), 100)
    c1.setWidth(border)
    c1.setFill("yellow")
    c1.draw(w)

    c2 = Circle(Point(0, 500), 150)
    c2.setWidth(border)
    c2.setFill("pink")
    c2.draw(w)


    r = Rectangle(Point(350, 45), Point(400, 300))
    r.setWidth(border)
    r.setFill("blue")
    r.draw(w)

    q = Rectangle(Point(250, 350), Point(350, 450))
    q.setWidth(border)
    q.setFill("red")
    q.draw(w)

    return (w, c1, c2, r, q)

def main():
    (w, c1, c2, r, q) = init()

    while True:
        p = w.getMouse()
        print("You clicked on %s" % p) 

        if in_circle(p, c1):
            print("  ==> inside the yellow circle.")
        elif in_circle(p, c2):
            print("  ==> inside the pink circle.")
        elif in_rectangle(p, r):
            print("  ==> inside the blue rectangle.")
        elif in_rectangle(p, q):
            print("  ==> inside the red rectangle, let's terminate.")
            exit() 

def window():
    w = GraphWin("Test window", 500, 500)
    w.setBackground("white")

    return w

if __name__ == "__main__":
    main()
