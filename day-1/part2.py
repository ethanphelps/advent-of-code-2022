# find sum of top 3 elves

def main():
    with open('input.txt') as f:
        lines = f.readlines()

        top_three = [0,0,0]
        cal_count = 0
        line_number = 0
        while line_number < len(lines):
            line = lines[line_number].strip()
            if line == '':
                rank_calories(top_three, cal_count)
                cal_count = 0
            else:
                cal_count += int(line)
            line_number += 1

        # check the last elf
        rank_calories(top_three, cal_count)

        print(sum(top_three))

def rank_calories(top_three, count):
    if count > top_three[2]:
        if count > top_three[1]:
            if count > top_three[0]:
                top_three[2] = top_three[1]
                top_three[1] = top_three[0]
                top_three[0] = count
            else:
                top_three[2] = top_three[1]
                top_three[1] = count
        else:
            top_three[2] = count

if __name__ == "__main__":
    main()