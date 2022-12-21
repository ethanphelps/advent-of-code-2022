import math

def main():
    W,H = 40,6
    sprite = 1
    cycle = 1
    screen = [['.' for i in range(W)] for j in range(H)]

    with open('input.txt') as f:
        instr = None

        for line in f:
            instr = line.strip().split()
            draw(screen, sprite, cycle)

            if instr[0].startswith('add'):
                cycle += 1
                draw(screen, sprite, cycle)
                cycle += 1
                sprite += int(instr[1])
            else:
                cycle += 1

    render(screen)

def draw(screen, sprite, cycle):
    if (cycle % 40) - 1 in range(sprite - 1, sprite + 2): # check if current pixel to be drawn contains the sprite's position
        screen[cycle // 40][(cycle % 40) - 1] = '#'

def render(screen):
    for row in screen:
        line = ''
        for pixel in row:
            line += pixel
        print(line)


if __name__ == '__main__':
    main()
