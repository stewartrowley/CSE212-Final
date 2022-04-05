# Trees

In Software there is many benefits to trees.

## Big O Notation

It is limiting behavior in coding. Being from a particular value to infinity. Big O notation tells you how fast your code will read the data. It is based off of how you read data. 

In trees, big O notation is O(n) and O(Log n) also. Which is really quick in getting data. All of the operations you will see are O(n) and O(Log n).

## The meaning of a tree.

It is non-linear data structure. It is usually represented by nodes that are connected by edges. It consist of of root nodes. It has parent nodes and children nodes. It It is useful data structure in its quick performance. 

##  operations

The different operations in a stacks:

- `insert(value)`  :  Adds a value to the tree. It has a O(log n) performance.
- `remove(value)` : It removes the value from the set. It is also O(log n)
- `empty(value)` : This is where you can empty the set It is O(1).
- `size(1)` : It will show you the size of the tree. Like the length of the set. This is also O(1).

![This is an image](/images/tree.png)
Example of a tree:

```python


class List:
    """
    Example of using nodes to insert into a tree. That is created. In this example it is like the directions of a compass. 
    You insert north in this example but you could do it with any of the other directions.
    It is also an example of removing north.
    """

    class Node:


        def __init__(self, data):

            self.data = data
            self.east = None
            self.west = None

    def __init__(self):

        self.north = None
        self.south = None

    def insert_north(self, value):

        new_node = List.Node(value)  
        
        if self.north is None:
            self.north = new_node
            self.south = new_node
        else:
            new_node.east = self.north 
            self.north.west = new_node 
            self.north = new_node      

    def remove_north(self):

        if self.north == self.south:
            self.north = None
            self.south = None

        elif self.north is not None:
            self.north.east.west = None  
            self.north = self.north.east  


    def __str__(self):

        output = "["
        first = True
        curr = self.north
        while curr is not None:
            if first:
                first = False
            else:
                output += ", "
            output += str(curr.data)
            curr = curr.east
        output += "]"
        return output

    
# It will create an empty list
numbers = List()
print("Empty List: {}\n".format(numbers))

# Inserts 4 numbers into the tree
numbers.insert_north(7)
numbers.insert_north(5)
numbers.insert_north(2)
numbers.insert_north(3)
print("Inserting 4 numbers: {}\n".format(numbers))

# Removes north from the tree
numbers.remove_north()
print("Removing north: {}\n".format(numbers))
```

## Problem to solve.

In this problem you will have to demostrate your knowledge of Stacks and how they work.

```python
'''
Create a way to insert a node. Remember the example and make it your own.
'''

class List:
    pass

    class Node:
        pass


```

Start your work on this file:
[Solution](trees.py)

You can check your code with the solution here: [Solution](trees.py)
