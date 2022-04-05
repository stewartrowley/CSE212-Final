

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

