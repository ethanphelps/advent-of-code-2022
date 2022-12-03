def main():
    with open('input.txt') as f:
        rucksacks = f.readlines()
        count = 0
        ''' 
        iterate over lines in sets of three
        use a shared dictionary mapping characters to a list
        process characters in 1st, 2nd, 3rd rucksack, appending a 1, 2 or 3 to the list value
        in the dict depending on which rucksack in the set of 3 you're examining
        then iterate over the items of the dict. the key that maps to a list of length 3 is the
        item type that corresponds to the badge.
        add the priority of that item type to the count and move on to the next set of three
        '''
        
        print(count)

def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    elif c.isupper():
        return ord(c) - ord('A') + 27

if __name__ == "__main__":
    main()