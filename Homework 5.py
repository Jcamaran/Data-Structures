class Node:
    def __init__(self,n,pr,st):
        self.name = nm
        self.price = pr
        self.stock = st
        self.ref = None

class LinkedList:
#---------- creatiing empty linked list -----------#
    def __init__(self):
        self.start_node = None

# ---------- Adding product to begining of list -----------#
    def Add_to_start(self,nm,pr,st):
        new_node = Node(nm,pr,st)
        new_node.ref = self.start_node
        self.start_node = new_node

# ---------- Traverse and printing the products list -----------#
    def print_products(self):
        print("Linked List: ", end="\n")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.name,":",n.price,":",n.stock, end = "\n")
                n = n.ref
        print("")

# ---------- print products above $8  -----------#
    def Products_Above8(self):
        print("Products above $10 in price", end = "\n")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.price > 10:
                    print(n.name,": $",n.price,":",n.stock,"pounds",  end = "\n")
                n = n.ref
        print("")

# ---------- print products with less than 20 pounds in stock  -----------#
    def Products_under20_stock(self):
        print("Low stock products under 20 pounds:", end = "\n")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.stock < 20:
                    print(n.name, ": $", n.price, ":", n.stock,"pounds", end="\n")
                n = n.ref
        print("")

# ---------- Main program -----------#

My_List = LinkedList()

choice = 0
while choice != 5:
    print("\n LinkedList Demo, what do you want to do?")
    print(" 1 = Insert at beginning ")
    print(" 2 = Traverse and print all of List ")
    print(" 3 = Print all products above $10")
    print(" 4 = Print all products under 20 pounds in stock")
    print(" 5 = Exit")
    choice = int(input("\n Enter Choice: "))

    if choice == 1 :
        name = input("\n Enter Name of product to add to linked list: ")
        price = float(input("\n Enter price of the product: "))
        stock = float(input("\n Enter the stock of the item(in pounds):  "))
        My_List.Add_to_start(name, price, stock)
        print(name,"inserted at the beginning")
    elif choice ==  2:
        My_List.print_products()
    elif choice == 3:
        My_List.Products_Above8()
    elif choice == 4:
        My_List.Products_under20_stock()








