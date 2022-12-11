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

        scenic_scores = {}
        for i in range(0, len(forest[0])):
            for j in range(0, len(forest)):
                # check to left
                left = 0
                for k in range(j-1, -1, -1):
                    left += 1
                    if forest[i][k] >= forest[i][j]:
                        break
                # check to right
                right = 0
                for k in range(j+1, w):
                    right += 1
                    if forest[i][k] >= forest[i][j]:
                        break
                # check above
                above = 0
                for k in range(i-1, -1, -1):
                    above += 1
                    if forest[k][j] >= forest[i][j]:
                        break
                # check below
                below = 0
                for k in range(i+1, h):
                    below += 1
                    if forest[k][j] >= forest[i][j]:
                        break

                scenic_scores[f'{i},{j}'] = left * right * above * below

        print(scenic_scores)
        print(max(scenic_scores.values()))

if __name__ == '__main__':
    main()
