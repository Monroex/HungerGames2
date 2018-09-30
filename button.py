from graphics import *

class Button:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), text)
        self.text.setSize(25)
        self.text.setStyle("bold")

    def draw(self, w):
        self.shape.draw(w)
        self.text.draw(w)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def getShape(self):
        return self.shape

    def getCenter(self):
        return self.shape.getCenter()



