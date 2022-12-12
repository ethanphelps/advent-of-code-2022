''' 
attempting an O(n) solution to the tree visibility problems using monotonic stacks
make 4 matrices: 
    1 for next greater element to right of each element, 
    1 for next greater element to left of each element
    1 for next greater element above each element
    1 for next greater element below each element
then for each element in the input, if the corresponding element in any of these matrices is -1, 
it is visible from outside the forest
'''

def next_greater_right(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in enumerate(arr):
        while len(stack) > 0 and arr[stack[-1]] <= num:
            index = stack.pop()
            res[index] = num
        stack.append(i)
    return res
            
def next_greater_left(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in reversed(list(enumerate(arr))):
        while len(stack) > 0 and arr[stack[-1]] <= num:
            index = stack.pop()
            res[index] = num
        stack.append(i)
    return res

# replaces values in arr with index of next greater number, instead of value
def modified_next_greater_right(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in enumerate(arr):
        while len(stack) > 0 and arr[stack[-1]] <= num:
            index = stack.pop()
            res[index] = i
        stack.append(i)
    return res
            
# replaces values in arr with index of next greater number, instead of value
def modified_next_greater_left(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in reversed(list(enumerate(arr))):
        while len(stack) > 0 and arr[stack[-1]] <= num:
            index = stack.pop()
            res[index] = i
        stack.append(i)
    return res


def part1():
    with open('input.txt') as f:
        # turn lines of input into 2d array of integer heights
        forest = list(map(lambda l: l.strip(), f.readlines()))
        forest = [[int(c) for c in row] for row in forest]
        inverted_forest = invert(forest)

        # print(forest)
        # print(inverted_forest)
        w = len(forest[0])
        h = len(forest)
        print(f'{w}, {h}')

        blocking_trees_right = [next_greater_right(row) for row in forest]
        blocking_trees_left = [next_greater_left(row) for row in forest]
        blocking_trees_above = invert([next_greater_left(row) for row in inverted_forest])
        blocking_trees_below = invert([next_greater_right(row) for row in inverted_forest])

        visible_trees = {}
        for i, row in enumerate(forest):
            for j, col in enumerate(forest[i]):
                if (blocking_trees_left[i][j] == -1 
                    or blocking_trees_right[i][j] == -1 
                    or blocking_trees_above[i][j] == -1 
                    or blocking_trees_below[i][j] == -1
                    ):
                    visible_trees[f'{i},{j}'] = forest[i][j]

        # print(visible_trees)
        print(len(visible_trees))

def part2():
    with open('input.txt') as f:
        # turn lines of input into 2d array of integer heights
        forest = list(map(lambda l: l.strip(), f.readlines()))
        forest = [[int(c) for c in row] for row in forest]
        inverted_forest = invert(forest)
        w = len(forest[0])
        h = len(forest)

        # blocking trees 2d arrays now have index of blocking tree from given direction instead of its height
        blocking_trees_right = [modified_next_greater_right(row) for row in forest]
        blocking_trees_left = [modified_next_greater_left(row) for row in forest]
        blocking_trees_above = invert([modified_next_greater_left(row) for row in inverted_forest])
        blocking_trees_below = invert([modified_next_greater_right(row) for row in inverted_forest])

        highest_dist = 0
        for i, row in enumerate(forest):
            for j, col in enumerate(forest):
                right_dist = blocking_trees_right[i][j] - j if blocking_trees_right[i][j] > 0 else w-j-1
                left_dist = j - blocking_trees_left[i][j] if blocking_trees_left[i][j] > 0 else j
                above_dist = i - blocking_trees_above[i][j] if blocking_trees_above[i][j] > 0 else i
                below_dist = blocking_trees_below[i][j] - i if blocking_trees_below[i][j] > 0 else h-i-1

                viewing_dist = right_dist * left_dist * above_dist * below_dist
                highest_dist = max(highest_dist, viewing_dist)
            
        print(highest_dist)


# inverts a rectangular 2d list (aka matrix)
def invert(mat):
    res = []
    w = len(mat[0])
    h = len(mat)
    for j in range(w):
        res.append([mat[i][j] for i in range(h)])
    return res

def main():
    # part1()
    # next_greater_right([1,2,3,4,5])
    # pass
    # with open('example.txt') as f:
    #     lines = list(map(lambda i: i.strip(), f.readlines()))
    #     for line in f:
    #         print(line.strip())
    #     print(lines)
    #     print(invert(lines))
    part1()

    # with open('example.txt') as f:
    #     forest = list(map(lambda l: l.strip(), f.readlines()))
    #     for i, row in enumerate(forest):
    #         forest[i] = [int(c) for c in row]
    #     inverted_forest = invert(forest)
    #     print(forest)
    #     # print(inverted_forest)

    #     blocking_trees_right = [next_greater_right(row) for row in forest]
    #     blocking_trees_left = [next_greater_left(row) for row in forest]
    #     blocking_trees_above = invert([next_greater_left(row) for row in inverted_forest])
    #     blocking_trees_below = invert([next_greater_right(row) for row in inverted_forest])

    #     print(blocking_trees_left)
    #     print(blocking_trees_right)
    #     print(blocking_trees_above)
    #     print(blocking_trees_below)
    part2()


if __name__ == '__main__':
    main()