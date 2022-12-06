def main():
    with open('input.txt') as f:
        lines = f.readlines()
        stack_lines, empty_line_index = get_stacks(lines)
        moves = lines[empty_line_index+1:]
        stacks = [None] # list of stacks, starting with None so indices from instructions line up

        # build stack from text and add to list
        i = 1
        while i < len(stack_lines[-1]):
            stack = []
            j = len(stack_lines) - 2
            while j >= 0 and stack_lines[j][i] != ' ':
                stack.append(stack_lines[j][i])
                j -= 1
            stacks.append(stack)
            i += 4 # items are four spaces apart
        # print(stacks)

        # run instructions
        for line in moves:
            instruction = line.split()
            count = int(instruction[1])
            index_from = int(instruction[3])
            index_to = int(instruction[5])
            while count > 0:
                item = stacks[index_from].pop()
                stacks[index_to].append(item)
                count -= 1

        # print(stacks)

        ans = ''
        for stack in stacks[1:]:
            ans += stack[-1]

        print(ans)

# iterates over input lines and returns just the lines for the stack configurations
def get_stacks(lines):
    i = 0
    stacks = []
    while lines[i][0] == ' ':
        stacks.append(lines[i])
        i += 1
    while lines[i][0] == '[':
        stacks.append(lines[i])
        i += 1
    stacks.append(lines[i])
    i += 1
    return stacks, i

if __name__ == "__main__":
    main()