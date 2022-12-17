import math

def main():
    with open('input.txt') as f:
        head = (0,0)
        tail = (0,0)
        dirs = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1),
        }
        positions = set([tail]) # keep track of unique positions the tail enters

        for instr in f.readlines():
            instr = instr.strip().split()
            direction = instr[0]
            distance = int(instr[1])
            # print(f'direction: {direction}, distance: {distance}')

            # split instruction into 1-move increments
            for i in range(distance):
                # move the head
                head = (head[0] + dirs[direction][0], head[1] + dirs[direction][1])
                # print(f'head: {head}')
                # calculate distance / dir of head from tail
                dir_vect = get_dir(head, tail)
                mag = magnitude(dir_vect)
                # move tail according to rules:
                # if head and tail on same axis, move tail one space in dir vector from tail to head
                # if not on same axis, move diagonally in direction from tail to head
                if mag > 1:
                    if dir_vect[0] == 0 or dir_vect[1] == 0:
                        # non-diagonal movement
                        tail = (tail[0] + dirs[direction][0], tail[1] + dirs[direction][1])
                    else:
                        # diagonal movement
                        if mag > 2:
                            # tail movement required
                            x_axis_multiplier = 1 if dir_vect[0] > 0 else -1
                            y_axis_multiplier = 1 if dir_vect[1] > 0 else -1
                            tail = int(x_axis_multiplier*(dir_vect[0]/dir_vect[0]) + tail[0]), int(y_axis_multiplier*(dir_vect[1]/dir_vect[1]) + tail[1])

                    positions.add(tail)
                # print(f'tail: {tail}')

        print(len(positions))


def get_dir(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])

def magnitude(vect):
    return math.sqrt(vect[0]**2 + vect[1]**2)

if __name__ == '__main__':
    main()