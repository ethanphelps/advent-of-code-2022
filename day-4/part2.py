def main():
    with open('input.txt') as f:
        pairs = f.readlines()
        count = 0
        for line in pairs:
            pair = line.strip().split(',')
            if detect_overlap(pair[0], pair[1]):
                count += 1
        print(count)

def detect_overlap(r1, r2):
    p1l = int(r1.split('-')[0])
    p1r = int(r1.split('-')[1])
    p2l = int(r2.split('-')[0])
    p2r = int(r2.split('-')[1])
    return (p1l >= p2l and p1r <= p2r) or (p2l >= p1l and p2r <= p1r) or (p2l <= p1r and p1l < p2l) or (p1l <= p2r and p2l < p1l)


if __name__ == "__main__":
    main()