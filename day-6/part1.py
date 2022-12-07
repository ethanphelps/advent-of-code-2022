def main():
    with open('input.txt') as f:
        stream = f.readline()
        # print(stream)
        l = 0
        r = 13
        while r < len(stream):
            letters = set([])
            for i in range(l,r+1):
                letters.add(stream[i])
            if len(letters) == 14:
                print(r+1)
                return
            l += 1
            r += 1

if __name__ == "__main__":
    main()