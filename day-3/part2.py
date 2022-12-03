def main():
    with open('input.txt') as f:
        rucksacks = f.readlines()
        count = 0
        ''' 
        iterate over lines in sets of three
        use a shared dictionary mapping characters to a set
        process characters in 1st, 2nd, 3rd rucksack, appending i, i+1 or i+2 to the set 
        in the dict depending on which rucksack in the set of 3 you're examining
        then iterate over the items of the dict. the key that maps to a set of length 3 is the
        item type that corresponds to the badge.
        add the priority of that item type to the count and move on to the next set of three
        this has a running time of O(n)
        '''
        i = 0
        letters = {} # char -> set<char> where elements of set are i, i+1, or i+2
        while i < len(rucksacks):
            # iterate over group of three
            for j in range(i, i+3):
                line = rucksacks[j].strip()
                # add j to character's set if character encountered
                for c in line:
                    if c in letters:
                        letters[c].add(j)
                    else:
                        letters[c] = set([j])
            # find item that appears three times and add priority to count
            for item in letters:
                if len(letters[item]) == 3:
                    count += priority(item)
            i += 3
            letters = {}
        
        print(count)

def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    elif c.isupper():
        return ord(c) - ord('A') + 27

if __name__ == "__main__":
    main()