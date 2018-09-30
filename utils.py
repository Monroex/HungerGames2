from   graphics import *
from   time     import sleep
import random

def dawn_colors():
    '''
    Argument(s) :: None

    Side effects
       None

    Return value :: list
       List of black/white shade colors from black to white).
    '''

    grays = ["gray%s" % level for level in range(1,100, 2)]
    return ["black"] + grays + ["white"]

def dusk_colors():
    '''
    Argument(s) :: None

    Side effects
       None

    Return value :: list
       List of black/white shade colors from white to black.
    '''

    d = dawn_colors()[:]
    d.reverse()
    return d

def take(xs, n):
    '''
    Arguments:
       xs :: list
       n  :: integer

    Return value :: list
       n >= 0 ==> returns a list with the n first element of xs.
       n <  0 ==> returns a list with the n last elements of xs.

     Side effects: None
    '''

    if n >= 0:
        return xs[:n]
    else:
        return xs[-1:(n-1):-1]

def shuffle(xs):
    '''
    Argument(s)

       xs :: list

    Side effects
       None.

    Return value :: list
       A copy of xs where the order of the elements have been randomly shuffled.
    '''

    tmp = xs[:]
    random.shuffle(tmp)
    return tmp


def show(w, objects):
    '''
    Argument(s)
       w       :: GraphWin
       objects :: list of graphical objects

    Side effects
       Draws all objects in window w.

    Return value :: None
    '''

    for object in objects:
        object.draw(w)

def hide(objects):
    '''
    Argument(s)
       objects :: list of graphical objects

    Side effects
       Un-draws all objects.

    Return value :: None
    '''

    for object in objects:
        object.undraw()

def random_color():
    """
    Argument(s) :: None

    Side effects
       None

    Return value :: string
       A random color name.
    """

    return random.choice(["black", "white", "red", "blue", "green", "pink", "orange", "RoyalBlue1", "green3"])

def random_color_fill(shape):
    '''
    Argument(s)
       shape :: Circle or Rectangle

    Return value :: None

    Side effects
       Set the color of shape to a random color.
    '''

    shape.setFill(random_color())

def frame():
    '''
    Argument(s) :: None

    Side effects :: None

    Return value :: list
       List with Line objects for a blue frame around a 500 by 500 pixel window.
    '''

    f = [Line(Point(0, 0), Point(499, 0)),
         Line(Point(0, 499), Point(499, 499)),
         Line(Point(0, 0), Point(0, 499)),
         Line(Point(499, 0), Point(499, 499))]

    for line in f:
        line.setWidth(9)
        line.setFill("blue")

    return f

def make_grid():
    '''
    Argument(s) :: None

    Side effects :: None

    Return value :: list
       List with Line objects. The lines make up a 5 by 5 grid and a border for
       a 500 by 500 pixel window.
    '''

    lines = frame()

    steps = range(99, 499, 100)

    for y in steps:
        line = Line(Point(0, y), Point(499, y))
        line.setFill("blue")
        line.setWidth(5)
        lines.append(line)

    for x in steps:
        line = Line(Point(x, 0), Point(x, 499))
        line.setFill("blue")
        line.setWidth(5)
        lines.append(line)

    return lines
