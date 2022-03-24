# Sets

In Software there is many benefits to sets.

## Big O Notation

It is limiting behavior in coding. Being from a particular value to infinity. Big O notation tells you how fast your code will read the data. It is based off of how you read data. 

In sets big O notation is mainly just O(1) also. Which is pretty quick. All of the operations you will see are O(1).

## The meaning of a Sets.

It is a mutable collection of unique elements. It is not ordered. Like an ordered list. It It is useful data structure in its quick performance. 
It is also used with hashing. Causing us to be able to use more operations in it.

```python
set = {}
```
##  operaitions

The different operations in a stacks:

- `add(value)`  :  Adds a value to the set. It has a O(1) performance.
- `remove(value)` : It removes the value from the set. It is also O(1)
- `member(value)` : This is where you can decide if it is in the set. It is also O(1).
- `size()` : It will show you the size of the set. Like the length of the set. This is also O(1).

![This is an image](/Sets.jpg)
Example of a Stack:

```python
def sets():
    # Creates the set
    set = {1, 4, 8, 20}
    
    # adds the number to set, O(1)
    set.add(5)
    print(set)
    print("")
    
    # removes the number to the set, O(1)
    set.remove(8)
    print(set)
    print("")

    # checks if it is in the list O(1)
    if 4 in set:
        print("true")
    else: 
        print("false")
    print("")

    # Gives the length  of the set
    length = len(set)
    print(f"The size of the set is: {length}")

def main():
    sets()
if __name__ == "__main__":
    main()
```

## Problem to solve.

In this problem you will have to demostrate your knowledge of Stacks and how they work.

```python
def(set_work):
    '''
    Create a set of items and demonstrate how you can use these operations to create a menu system.
    Where the user can input what they want to know about the set. Hint use a while loop to show and 
    display your menu.
    
    '''


    pass


def main():
    set_work()
if __name__ == "__main__":
    main()

```


You can check your code with the solution here: [Solution](sets.py)
