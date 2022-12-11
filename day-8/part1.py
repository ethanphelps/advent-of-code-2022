def main():
    with open('input.txt') as f:
        forest = f.readlines()
        # remove new line characters
        for i in range(len(forest)):
            forest[i] = forest[i].strip()
        print(forest)
        w = len(forest[0])
        h = len(forest)
        print(f'{w}, {h}')

        visible_trees = {}
        for i in range(1, len(forest[0]) - 1):
            for j in range(1, len(forest) - 1):
                # check to left
                left = True
                for k in range(0, j):
                    if forest[i][k] >= forest[i][j]:
                        left = False
                        break
                # check to right
                if not left:
                    right = True
                    for k in range(j+1, w):
                        if forest[i][k] >= forest[i][j]:
                            right = False
                            break
                # check above
                if not (left or right):
                    above = True
                    for k in range(0, i):
                        if forest[k][j] >= forest[i][j]:
                            above = False
                            break
                # check below
                if not (left or right or above):
                    below = True
                    for k in range(i+1, h):
                        if forest[k][j] >= forest[i][j]:
                            below = False
                            break

                if left or right or above or below:
                    visible_trees[f'{i},{j}'] = forest[i][j]

        print(visible_trees)
        print(len(visible_trees) + 2*w + 2*(h-2))

if __name__ == '__main__':
    main()