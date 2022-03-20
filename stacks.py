

def stacks():

    stack = [1, 2, 4, 6]

    user = ''
    while user != 'no':
        print('')
        print(stack)
        user = input(
            'Do you want to append or pop or size or empty the stack?(type a or p or s or e or no to end) ')

        # Pushes - on the stack.
        if user == 'a':
            answer = input('What number would your like to append? ')
            stack.append(answer)

        # Pop - removes last item from the stack.
        if user == 'p':
            stack.pop()

        # Size - returns the size of it.
        if user == 's':
            print('')
            print(f' The length of the stack is: {len(stack)}')

        # Empty - returns true if the stack is.
        if user == 'e':
            if len(stack) == 0:
                print('The stack is already empty')
            else:
                stack.clear()
                print(stack)
                print('The stack is empty')


def stack_work():

    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # add to the stack until it gets to 15.
    numbers_to_append = [11, 12, 13, 14, 15]
    for i in numbers_to_append:
        stack.append(i)
    print(f'Here is the stack: {stack}') # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print('')

    # remove the stack until it has 1 through 4 only left.
    for i in range(11):
        stack.pop()
    print(f'Here is the stack: {stack}') # [1, 2, 3, 4]
    print('')

    # Give me the size of the stack.
    length = len(stack)
    print(f'Here is the size of the stack: {length}') # size = 4
    print('')

    # clear all the items left in the stack.
    stack.clear()
    print(f'Here is the stack: {stack}') # []
    print('')


def main():
    # Here is the example problem.
    stacks()

    # Here is the solutions solved.
    stack_work()



if __name__ == '__main__':
    main()
