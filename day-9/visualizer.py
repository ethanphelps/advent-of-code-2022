import math
from colors import *
from tkinter import *
from tkinter import ttk

LENGTH = 10
rope = [(0,0) for i in range(LENGTH)]
dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def main():
    window = Tk()
    window.title('Rope Simulation')
    window.maxsize(1000, 700)
    window.config(bg = dark_bg)
    


    window.mainloop()


# updated, next are indices of previously updated and next rope knots
def update_next(updated: int, next_node: int):
    if next_node < len(rope):
        # run updating code

        # print(f'head: {head}')
        # calculate distance / dir of head from tail
        dir_vect = get_dir(rope[updated], rope[next_node])
        moving = should_move(dir_vect)
        # move tail according to rules:
        # if head and tail on same axis, move tail one space in dir vector from tail to head
        # if not on same axis, move diagonally in direction from tail to head
        if moving:
            x_dir = 1 if dir_vect[0] > 0 else -1
            y_dir = 1 if dir_vect[1] > 0 else -1
            x_next = 0 if dir_vect[0] == 0 else rope[next_node][0] + x_dir
            y_next = 0 if dir_vect[1] == 0 else rope[next_node][1] + y_dir
            rope[next_node] = (x_next, y_next)

        # recursively call update_next
        update_next(next_node, next_node + 1)

def get_dir(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])

def should_move(dir_vect) -> bool:
    return abs(dir_vect[0]) > 1 or abs(dir_vect[1]) > 1

if __name__ == '__main__':
    main()