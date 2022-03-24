# Sets

In Software there is many benefits to sets.

## Big O Notation

It is limiting behavior in coding. Being from a particular value to infinity. Big O notation tells you how fast your code will read the data. It is based off of how you read data. 

In sets big O notation is mainly just O(1) also. Which is pretty quick. All of the operations you will see are O(1).

## The meaning of a Stack.

It is a mutable collection of unique elements. It is not ordered. Like an ordered list. It It is useful data structure in its quick performance. 
It is also used with hashing. Causing us to be able to use more operations in it.

```python
set = {}
```
##  operaitions

The different operations in a stacks:

- `pop()`  :  Removes what is in the end of the     stack. It has a O(1) performance.
- `push()` : Adds to the end of the stack. It is also O(1)
- `size()` : It returns what the length of the stack is. You use the len() operation for this. It is also O(1).
- `empty()` : It returns an empty stack. You use clear or other operations.

![This is an image](/Stacks.png)
Example of a Stack:

```python
def stacks():

    # Creates the stack of 1,2,4 and 6
    stack = [1, 2, 4, 6]


    user = ''
    # loops through until users is done.
    while user != 'no':
        print('')
        print(stack)
        user = input('Do you want to append or pop or size or empty the stack?(type a or p or s or e or no to end) ')

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

def main():
    stacks()
```

## Problem to solve.

In this problem you will have to demostrate your knowledge of Stacks and how they work.

```python
stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
# add to the stack until it gets to 15.


print(f'Here is the stack: {stack}')
print('') 
	
# remove the stack until it has 1 through 4 only left.
 

print(f'Here is the stack: {stack}') 
print('') 

# Give me the size of the stack. 


print(f'Here is the stack: {stack}') 
print('') 

# clear all the items left in the stack.

	
print(f'Here is the stack: {stack}') 
print('') 

```


You can check your code with the solution here: [Solution](stacks.py)
