def main():
    with open('input2.txt') as f:
        lines = f.readlines()

        max_cals = 0
        cal_count = 0
        line_number = 0
        while line_number < len(lines):
            line = lines[line_number].strip()
            if line == '':
                if cal_count > max_cals:
                    max_cals = cal_count
                cal_count = 0
            else:
                cal_count += int(line)
            line_number += 1

        # check the last elf
        if cal_count > max_cals:
            max_cals = cal_count

        print(max_cals)

if __name__ == "__main__":
    main()