from graphics import GraphWin
from game import game

def main():
    w = GraphWin("The Hunger Games", 500, 500)
    game(w)

if __name__ == "__main__":
    main()
