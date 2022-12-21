def main():
    def check_strength():
        if (cycle % 40) - 20 == 0:
            strength = cycle * reg
            print(f'signal strength at cycle {cycle}: {strength}')
            if cycle <= 220:
                strengths[str(cycle)] = strength

    with open('input.txt') as f:
        reg = 1
        cycle = 1
        wait = 0
        instr = None
        strengths = {}

        for line in f:
            instr = line.strip().split()
            check_strength()

            if instr[0].startswith('add'):
                cycle += 1
                check_strength()
                cycle += 1
                reg += int(instr[1])
            else:
                cycle += 1

        print(sum(map(lambda x: int(x), strengths.values())))


if __name__ == '__main__':
    main()