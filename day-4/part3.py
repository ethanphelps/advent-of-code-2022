def main():
    with open('input.txt') as f:
        pairs = f.readlines()
        count = 0
        faulty_count = 0
        correct_set = set([])
        faulty_set = set([])
        for line in pairs:
            pair = line.strip().split(',')
            if detect_overlap(pair[0], pair[1]):
                count += 1
                correct_set.add(line.strip())
            if detect_overlap_faulty(pair[0], pair[1]):
                faulty_count += 1
                faulty_set.add(line.strip())
        print(f'correct count: {count}')
        print(f'faulty count: {faulty_count}')
        print('faulty pairs: ')
        print(faulty_set.difference(correct_set))
        print(correct_set.difference(faulty_set))

def detect_overlap(r1, r2):
    p1l = int(r1.split('-')[0])
    p1r = int(r1.split('-')[1])
    p2l = int(r2.split('-')[0])
    p2r = int(r2.split('-')[1])
    return (p1l >= p2l and p1r <= p2r) or (p2l >= p1l and p2r <= p1r) or (p2l <= p1r and p1l < p2l) or (p1l <= p2r and p2l < p1l)

def detect_overlap_faulty(r1, r2):
    p1l = int(r1.split('-')[0])
    p1r = int(r1.split('-')[1])
    p2l = int(r2.split('-')[0])
    p2r = int(r2.split('-')[1])
    return p2l <= p1r
    # return (p2l <= p1r and p1l <= p2l) or (p1l <= p2r and p2l <= p1l)


if __name__ == "__main__":
    main()