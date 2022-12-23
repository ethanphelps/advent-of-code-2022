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
                false_monkey = false_line.strip().split()[31]
                monkeys[monkey_id]['false'] = false_monkey
            line = f.readline()

        print(monkeys)

        NUM_ROUNDS = 500
        for i in range(NUM_ROUNDS):
            # process each monkey
            for monkey in monkeys.values():
                for item in monkey['items']:
                    new_worry, test_result = operation_and_test(monkey, item, monkey['test'])
                    if test_result == 0:
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
                    

def operation_and_test(monkey, item, divisor):
    operator = monkey['operation']['operator']
    operand = monkey['operation']['operand']
    # (a*b)%c == (a%c * b%c)%c
    # (a+b)%c == (a%c + b%c)%c
    if operator == '+':
        if operand == 'old':
            return item+item, (((item % divisor) + (item % divisor)) % divisor)
        else:
            return item+int(operand), (((item % divisor) + (int(operand) % divisor)) % divisor)
    elif operator == '*':
        if operand == 'old':
            return item*item, (((item % divisor) * (item % divisor)) % divisor)
        else:
            return item*int(operand), (((item % divisor) * (int(operand) % divisor)) % divisor)


if __name__ == '__main__':
    main()
