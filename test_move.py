import random
from   game   import move_position

def random_key():
    return random.choice(["Right", "Left", "Up","Down"])

def random_keys(n):
    return [random_key() for _ in range(n)]

def test_keys(pos, keys):

    for key in keys:
        pos = move_position(pos, key)
        print("Move %s ==> pos = %s" % (key.ljust(5), pos ))

    return pos

def wrap_around():
    keys =  ["Right"]*5 + ["Down"]*5 + ["Left"]*5 + ["Down"]
    return keys

def main():
    pos = (2,2)

    print("pos = %s" % (pos, ))

    pos = test_keys(pos, wrap_around())
    test_keys(pos, random_keys(10))

if __name__ == "__main__":
    main()
 
