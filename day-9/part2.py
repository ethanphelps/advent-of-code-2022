import math

LENGTH = 10
rope = [(0,0) for i in range(LENGTH)]
# rope = [(-3,3), (-2,2), (-1,1), (0,0)]
# print(rope)
dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def main():
    with open('example2.txt') as f:
        positions = set([rope[-1]]) # keep track of unique positions the tail enters
        # print(positions)

        for instr in f.readlines():
            instr = instr.strip().split()
            direction = instr[0]
            distance = int(instr[1])
            # print(f'direction: {direction}, distance: {distance}')

            # split instruction into 1-move increments
            for i in range(distance):
                # move the head
                rope[0] = (rope[0][0] + dirs[direction][0], rope[0][1] + dirs[direction][1])
                # update rest of rope
                update_next(0, 1)
                print(rope)
            positions.add(rope[-1])

            # print(rope[-1])
            # print(f'tail: {tail}')

        # print(positions)
        print(rope)
        print(positions)
        print(len(positions))

        # todo: visualize with tkinter


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