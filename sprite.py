from graphics import *

class Sprite:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color

        (x, y) = self.position
        p = Point(x*100 + 50, y*100 + 50)
        circle = Circle(p, radius)
        circle.setWidth(10)
        circle.setFill(color)

        self.circle = circle

    def draw(self, w):
        self.circle.draw(w)

    def undraw(self):
        self.circle.undraw()

    def move(self, position):
        (x1, y1) = self.position
        (x2, y2) = position
        dx = x2 - x1
        dy = y2 - y1
        self.circle.move(dx*100, dy*100)
        self.position = (x2, y2)

    def collision(self, sprite):
       return self.position == sprite.position

def translate(position):
    (x, y) = position
    return (50 + 100*x, 50 + 100*y)
