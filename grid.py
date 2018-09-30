from graphics import Point, Line

def frame():
    f = [Line(Point(0, 0), Point(499, 0)),
         Line(Point(0, 499), Point(499, 499)),
         Line(Point(0, 0), Point(0, 499)),
         Line(Point(499, 0), Point(499, 499))]

    for line in f:
        line.setWidth(9)
        line.setFill("blue")

    return f


class Grid:
    def __init__(self):

        self.lines = frame()

        steps = range(99, 499, 100)

        for y in steps:
            line = Line(Point(0, y), Point(499, y))
            line.setFill("blue")
            line.setWidth(5)
            self.lines.append(line)

        for x in steps:
            line = Line(Point(x, 0), Point(x, 499))
            line.setFill("blue")
            line.setWidth(5)
            self.lines.append(line)

    def draw(self, w):
        for line in self.lines:
            line.draw(w)

    def undraw(self):
        for line in self.lines:
            line.undraw()
