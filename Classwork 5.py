class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    # ---------------Create an empty linked list -------------

    def __init__(self):
        self.start_node = None

    # --------------- Traverse the linked list  ----------------------

    def traverse_list(self):
        print("Linked List: ", end=" ")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, end=" ")
                n = n.ref
        print(" ")

        #  ------------- Insert at start  ----------------------

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    #  ------------- Insert at end  ----------------------

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    #  ------------ Insert in middle  ----------------------

    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("Item not in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    #  ------------ Count nodes ---------------------------

    def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count

    #  ------------ Find Sum ---------------------------

    def get_sum(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        sum = 0
        while n is not None:
            sum = sum + n.item
            n = n.ref
        return sum
    # --------------- Get min ---------------

    def get_min(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        min = n.item
        while n is not None:
            if n.item < min:
                min = n.item
            n = n.ref
        return min
    # --------------- get Max ---------------
    def get_max(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        max = n.item
        while n is not None:
            if n.item > max:
                max = n.item
            n = n.ref
        return max
    # --------------- Get Average ---------------

    def get_avg(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        sum = 0
        while n is not None:
            sum = sum + n.item
            count = count + 1
            avg = sum/count
            n = n.ref
        return avg

    #  ------------- Search List for an item  ------------

    def search_item(self, x):
        if self.start_node is None:
            print(" List has no items")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("Item not found")
        return False

    # -------------- Delete first item  ------------------

    def delete_at_start(self):
        if self.start_node is None:
            print("Linked list is empty!")
            return
        self.start_node = self.start_node.ref

    # -------------- Delete last item  --------------------

    def delete_at_end(self):
        if self.start_node is None:
            print("Linked list is empty!")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    # --------------- Delete a certain item ---------------

    def delete_element(self, x):
        if self.start_node is None:
            print("Linked list is empty!")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found")
        else:
            n.ref = n.ref.ref


# ----------------------- MAIN -----------------------------


My_List = LinkedList()

choice = 0
while choice != 14:
    print("\n LinkedList Demo, what do you want to do?")
    print(" 1 = Insert at beginning ")
    print(" 2 = Insert at the end ")
    print(" 3 = Insert in the middle")
    print(" 4 = Traverse and print List ")
    print(" 5 = Count number of nodes ")
    print(" 6 = Search for an item ")
    print(" 7 = Delete the first node ")
    print(" 8 = Delete the last node ")
    print(" 9 = Delete a particular node ")
    print(" 10 = Sum the linked list ")
    print(" 11 = The minimum of the list ")
    print(" 12 = The Maximum of the list ")
    print(" 13 = The average of the list ")
    print(" 14 = Exit")

    choice = int(input("\n Enter Choice: "))

    if choice == 1:
        num = int(input("\n Enter number to add to linked list: "))
        My_List.insert_at_start(num)
        print(num, " inserted at the beginning")
    elif choice == 2:
        num = int(input("\n Enter number to add to linked list: "))
        My_List.insert_at_end(num)
        print(num, " inserted at the end")
    elif choice == 3:
        num = int(input("\n Enter number to add to linked list: "))
        x = int(input(" Put it after which number? "))
        My_List.insert_after_item(x, num)
        print(num, " inserted at the end")
    elif choice == 4:
        My_List.traverse_list()
    elif choice == 5:
        x = My_List.get_count()
        print("List has ", x, " items now")
    elif choice == 6:
        x = int(input(" Enter number to search for: "))
        My_List.search_item(x)
    elif choice == 7:
        My_List.delete_at_start()
        print("Removed first item")
    elif choice == 8:
        My_List.delete_at_end()
        print("Removed last item")
    elif choice == 9:
        x = int(input(" Enter number to delete: "))
        My_List.delete_element(x)
        print("Removed it (if found)")
    elif choice == 10:
        x = My_List.get_sum()
        print("The sum is ", x,)
    elif choice == 11:
        x = My_List.get_min()
        print("The Minimum is ", x, )
    elif choice == 12:
        x = My_List.get_max()
        print("The Maximum is ", x, )
    elif choice == 13:
        x = My_List.get_avg()
        print("The Average is ", x, )


print("\n Goodbye \n")

