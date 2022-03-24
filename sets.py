
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

def set_work():
    # Creates the set
    set = {"Nintendo Switch", "Laptop", "Phone", "Basketball", "Tv"}

    # A while loop that will loop through the menu
    user = ""
    while user != 5:

        print("Menu Options")
        print("1. Add item to set")
        print("2. Remove item from set")
        print("3. Check if item is in set")
        print("4. Show size of set")
        print("5. Select this to exit")

        user = input("Select which option you want(type a number 1-5): ")

        # if the user picks one then it will add that item to the set.
        if user == '1':
            print("")
            print(set)
            print("")
            add_item = input("What item would you like to add? ")
            set.add(add_item)

            print("")
            print(set)
            print("")

        # if the user picks 2 then it will delete that exact item from the set.
        elif user == '2':
            print("")
            print(set)
            print("")
            delete_item = input("What item would you like to delete? ")
            set.remove(delete_item)

            print("")
            print(set)
            print("")

        # if the user picks 3, it will find the item.
        elif user == '3':
            print("")
            print(set)
            print("")
            find_item = input("What item would you like to find in your set? ")
            if find_item in set:
                print(f"{find_item} is in your set!")
            else:
                print("We were unable to find your item in the set.")
            print("")

        # if user picks 4 then it show what the size is of the set.
        elif user == '4':
            print("")
            size = len(set)
            print(f"The size of the set is: {size} items!")
            print("")
        
        # will break the loop and end it.
        else:
            print("")
            print(f"Here is your final set {set}")
            print("")
            break

            
            
            

def main():
    # Example of sets
    sets() 

    # Problem to solve sets
    set_work()



if __name__ == "__main__":
    main()