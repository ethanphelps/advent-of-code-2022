def main():
    with open('input.txt') as f:
        rucksacks = f.readlines()
        count = 0
        for r in rucksacks:
            r = r.strip()
            left = {}
            right = {}
            for c in r[:int(len(r)/2)]:
                left[c] = 1 if c not in left else left[c] + 1
            for c in r[int(len(r)/2):]:
                right[c] = 1 if c not in right else right[c] + 1
            for key in left:
                if key in right:
                    # print(key)
                    count += priority(key)
                    break
        print(count)

def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    elif c.isupper():
        return ord(c) - ord('A') + 27

if __name__ == "__main__":
    main()