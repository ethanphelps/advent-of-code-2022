def main():
    with open('input.txt') as f:
        # parse file contents into appropriate objects
        # then run the 'rounds'
        monkeys = {}
        line = f.readline()
        while line:
            data = line.strip().split()
            if data and data[0] == 'Monkey':
                monkey_id = data[1].split(':')[0]
                monkeys[monkey_id] = {
                    'items': [],
                    'operation': { 'operator': None, 'operand': None },
                    'test': None,
                    'true': None,
                    'false': None,
                    'count': 0
                }

                # get items
                line = f.readline()
                items_line = line.strip().split(':')
                items = items_line[1].strip().split(',')
                items = list(map(lambda x: int(x), items))
                monkeys[monkey_id]['items'] = items
                
                # get operation
                line = f.readline()
                op = line.strip().split('=')[1].strip().split()
                operator = op[1]
                operand = int(op[-1]) if op[-1] != 'old' else 'old'
                monkeys[monkey_id]['operation']['operator'] = operator
                monkeys[monkey_id]['operation']['operand'] = operand
                
                # not sure why this didn't work :(
                # if operator == '+':
                #     print('operator is +')
                #     monkeys[monkey_id]['operation'] = (lambda x: x + x) if self_operation else (lambda x: x + operand)
                # elif operator == '*':
                #     print('operator is *')
                #     monkeys[monkey_id]['operation'] = (lambda x: x * x) if self_operation else (lambda x: x * operand)

                # get test
                line = f.readline()
                divisible_by = int(line.strip().split()[-1])
                # monkeys[monkey_id]['test'] = (lambda x: x % divisible_by) # not sure why this didn't work :(
                monkeys[monkey_id]['test'] = divisible_by

                # get true and false monkeys
                true_line = f.readline()
                true_monkey = true_line.strip().split()[-1]
                monkeys[monkey_id]['true'] = true_monkey
                false_line = f.readline()
                false_monkey = false_line.strip().split()[-1]
                monkeys[monkey_id]['false'] = false_monkey
            line = f.readline()

        print(monkeys)

        num = 20
        for monkey in monkeys.values():
            print(operation(monkey, num))

        NUM_ROUNDS = 20
        for i in range(NUM_ROUNDS):
            # process each monkey
            for monkey in monkeys.values():
                for item in monkey['items']:
                    new_worry = operation(monkey, item)
                    new_worry = new_worry // 3
                    if new_worry % monkey['test'] == 0:
                        monkeys[monkey['true']]['items'].append(new_worry)
                    else:
                        monkeys[monkey['false']]['items'].append(new_worry)
                    monkey['count'] += 1
                monkey['items'] = []
        
        # TODO: keep track of how many items each monkey has inspected
        counts = []
        for monkey in monkeys.values():
            counts.append(monkey['count'])
        counts.sort()
        monkey_business = counts[-1] * counts[-2]
        print(f'monkey business: {monkey_business}')

        divisor = 11
        for i,j in zip(range(0,20), range(5,26)):
            product = i*j
            r1 = product % divisor
            r2 = ((i % divisor) * (j % divisor)) % divisor
            print(f'r1: {r1}, r2: {r2}')
        for i,j in zip(range(0,20), range(5,26)):
            product = i+j
            r1 = product % divisor
            r2 = ((i % divisor) + (j % divisor)) % divisor
            print(f'r1: {r1}, r2: {r2}')
                    

def operation(monkey, item):
    operator = monkey['operation']['operator']
    operand = monkey['operation']['operand']
    if operator == '+':
        return item + int(operand) if operand != 'old' else item + item
    elif operator == '*':
        return item * int(operand) if operand != 'old' else item * item


if __name__ == '__main__':
    main()