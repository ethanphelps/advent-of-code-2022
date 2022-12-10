class Node():
    def __init__(self, name, parent, item_type='dir', val=0):
        self.parent = parent
        self.item_type = item_type
        self.name = name
        self.val = val
        self.children = {} # folder and file names should be unique, so use a dictionary
        self.visited = False


def main():
    with open('input.txt') as f:
        lines = f.readlines()[1:]
        
        root = Node('/', None, 'dir', 0)

        i = 0
        ptr = root
        while i < len(lines):
            command = lines[i].strip().split()
            # first character should be $
            if command[1] == 'ls':
                # iterate over remaining lines until next line that starts with a $, adding children along the way
                i += 1
                while i < len(lines) and lines[i][0] != '$':
                    command = lines[i].strip().split()
                    node = Node(command[1], ptr, 'dir', 0) if command[0] == 'dir' else Node(command[1], ptr, 'file', int(command[0])) 
                    ptr.children[command[1]] = node
                    i += 1
                # print(ptr.children)
            elif command[1] == 'cd':
                directory = command[2]
                if directory == '..':
                    # move ptr up to parent 
                    ptr = ptr.parent
                else:
                    # move ptr to specified directory
                    ptr = ptr.children[directory]
                i += 1

        # once the tree is built, determine size of each directory, starting from root
        # take depth first approach, reaching a "leaf" if you're at a node that doesn't have directory children ??
        # iterate over children, recursing down the tree if there's a dir, adding to this node's sum if there's a file
        # print(root.children)

        max_space = 70000000
        print(f'total memory: {max_space}')

        sizes = {}
        total_size = calculate_sizes(root, sizes)
        print(f'used memory: {total_size}')

        remaining_space = max_space - total_size
        print(f'remaining space: {remaining_space}')
        space_to_delete = 30000000 - remaining_space
        print(f'amount of memory to delete: {space_to_delete}')

        smallest = find_smallest_to_delete(root, space_to_delete, max_space)
        print(smallest)



# each dir has val set to its size, so iterate in DFS manner to find min
def find_smallest_to_delete(node, space_to_delete, smallest=70000000):
    for item in node.children.values():
        if item.item_type == 'dir':
            subtree_min = find_smallest_to_delete(item, space_to_delete, smallest)
            if subtree_min >= space_to_delete:
                smallest = min(subtree_min, smallest)
    if node.val >= space_to_delete:
        smallest = min(smallest, node.val)
    return smallest


def calculate_sizes(node, sizes, prefix=''):
    size = 0
    prefix += node.name
    for item in node.children.values():
        if item.item_type == 'file':
            size += item.val
        elif item.item_type == 'dir':
            dir_size = calculate_sizes(item, sizes, node.name if node.name == '/' else prefix + '/') 
            item.val = dir_size
            size += dir_size
    # print(f'size of dir {prefix} = {size}')
    if size <= 100000:
        sizes[prefix] = size

    return size

if __name__ == '__main__':
    main()