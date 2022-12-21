import math
import time
from colors import *
from tkinter import *
from tkinter import ttk

CELL_SIZE = 10
ROPE_LENGTH = 5
SPEED = 0.05
WINDOW_SIZE = 600
middle = int((WINDOW_SIZE/CELL_SIZE)/2) # divide by LENGTH since visuals will use a grid with cell size 10x10
rope = [(middle,middle) for i in range(ROPE_LENGTH)]
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

    speed_name = StringVar()
    speed_list = ['Fast', 'Medium', 'Slow']
    
    UI_frame = Frame(window, width= WINDOW_SIZE, height=WINDOW_SIZE, bg=dark_bg)
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    # dropdown to select sorting speed 
    l2 = Label(UI_frame, text="Sorting Speed: ", bg=dark_bg)
    l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
    speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
    speed_menu.grid(row=1, column=1, padx=5, pady=5)
    speed_menu.current(0)

    b3 = Button(UI_frame, text="Start", command=start, bg=grey)
    b3.grid(row=2, column=0, padx=5, pady=5)

    canvas = Canvas(window, width=WINDOW_SIZE, height=WINDOW_SIZE, bg=dark_bg)
    canvas.grid(row=1, column=0, padx=10, pady=5)

    # list of canvas square object ids
    rope_squares = [canvas.create_rectangle(knot[0]*CELL_SIZE, knot[1]*CELL_SIZE, (knot[0]*CELL_SIZE) + CELL_SIZE, (knot[1]*CELL_SIZE) + CELL_SIZE, fill=green) for knot in rope]

    start(canvas, rope_squares, window)

    # window.mainloop()



def draw_rope(rope, window, canvas):
    canvas.delete("all")
    for knot in rope:
        canvas.create_rectangle(knot[0]*CELL_SIZE, knot[1]*CELL_SIZE, (knot[0]*CELL_SIZE) + CELL_SIZE, (knot[1]*CELL_SIZE) + CELL_SIZE, fill=green)
    window.update()


def start(canvas, rope_squares, window):
    # call a recursive function that draws/updates squares continuously 
    with open('example2.txt') as f:
        positions = set([rope[-1]]) # keep track of unique positions the tail enters
        # print(positions)

        for instr in f.readlines():
            time.sleep(SPEED)
            instr = instr.strip().split()
            direction = instr[0]
            distance = int(instr[1])
            # print(f'direction: {direction}, distance: {distance}')

            # split instruction into 1-move increments
            for i in range(distance):
                # time.sleep(SPEED)
                rope[0] = (rope[0][0] + dirs[direction][0], rope[0][1] + dirs[direction][1])
                # canvas.move(rope_squares[0], map_x(rope[0][0]), map_y(rope[0][1]))
                # window.update()
                draw_rope(rope, window, canvas)

                for j in range(1, len(rope)):
                    # move the head
                    # update rest of rope
                    # update_next(0, 1, canvas, rope_squares)
                    # time.sleep(SPEED)

                    dir_vect = get_dir(rope[j-1], rope[j])
                    moving = should_move(dir_vect)
                    # move tail according to rules:
                    # if head and tail on same axis, move tail one space in dir vector from tail to head
                    # if not on same axis, move diagonally in direction from tail to head
                    if moving:
                        x_dir = 1 if dir_vect[0] > 0 else -1
                        y_dir = 1 if dir_vect[1] > 0 else -1
                        x_next = 0 if dir_vect[0] == 0 else rope[j][0] + x_dir
                        y_next = 0 if dir_vect[1] == 0 else rope[j][1] + y_dir
                        # time.sleep(0.5)
                        rope[j] = (x_next, y_next)
                        # canvas.move(rope_squares[j], map_x(rope[j][0]), map_y(rope[j][1]))
                        # window.update()
                        draw_rope(rope, window, canvas)

                # print(rope)
            positions.add(rope[-1])

# updated, next are indices of previously updated and next rope knots
def update_next(updated: int, next_node: int, canvas, rope_squares):
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
            time.sleep(0.5)
            rope[next_node] = (x_next, y_next)
            canvas.move(rope_squares[next_node], map_x(rope[next_node][0]), map_y(rope[next_node][1]))

        # recursively call update_next
        update_next(next_node, next_node + 1, canvas, rope_squares)

def get_dir(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])

def should_move(dir_vect) -> bool:
    return abs(dir_vect[0]) > 1 or abs(dir_vect[1]) > 1

def map_x(x):
    return x * CELL_SIZE
def map_y(y):
    return ((WINDOW_SIZE/CELL_SIZE) - y - 1) * CELL_SIZE

if __name__ == '__main__':
    main()