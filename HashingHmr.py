class Node:
    def __init__(self,num,cue):
        self.num = num
        self.cue = cue
        self.ref = None

class HashTable:
#---------- creating hashtable with size 8000  -----------#
    def __init__(self):
        self.Table_Size = 8011
        self.start_node = [None] * self.Table_Size

#-------Takes input and return location on linked list by getting the modules ------#
    def hashing_index(self, num):
        return (num % self.Table_Size)

# ---------- Adding a team to the list -----------#
    def Add_to_Table(self,num,cue):
        index = self.hashing_index(num)
        if self.start_node[index] is None:
            self.start_node[index] = Node(num,cue)
        else:
            Cnode = self.start_node[index]
            while Cnode.ref is not None:
                Cnode = Cnode.ref
            Cnode.ref = Node(num,cue)

# ---------- Printing the hashtable -----------#
    def print_Hashtable(self):
        for x in range(self.Table_Size):
            print(f"{x}:", end = "")
            Cnode = self.start_node[x]
            while Cnode is not None:
                print(f"{Cnode.cue}, {Cnode.num} ===>", end ="")
                Cnode = Cnode.ref
            print("None")

# ---------- print Teams with more than 3 problems solved  -----------#
    def Find_Record(self, num):
        index = self.hashing_index(num)
        Cnode = self.start_node[index]
        while Cnode is not None:
            if Cnode.num == num:
                print( "\n",Cnode.cue,"At index",index)
                Cnode = Cnode.ref
        return None

#----------- Remove certain indexes ----------#
    def RemoveFrom_Table(self, num):
        index = self.hashing_index(num)
        Cnode = self.start_node[index]
        Pnode = None
        while Cnode is not None:
            if Cnode.num == num:
                if Pnode:
                    Pnode.ref = Cnode.ref
                else:
                    self.start_node[index]= Cnode.ref
                return
            Pnode = Cnode
            Cnode = Cnode.ref

# ---------- Main program -----------#

My_List = HashTable()

choice = 0
while choice != 5:
    print("\n 1 = Add new student number to hash table ")
    print(" 2 = Print out Hash table ")
    print(" 3 = Finding a students record using their number")
    print(" 4 = Remove a student record from Table")
    print(" 5 = Exit")
    choice = int(input("\n Enter Choice: "))

    if choice == 1:
        name = input("\n Enter Student name: ")
        number = int(input("\n Enter student number:  "))
        My_List.Add_to_Table(number,name)
        print(name,"inserted")
        print("")
    elif choice ==  2:
        My_List.print_Hashtable()
    elif choice == 3:
        number = int(input("Enter Student number to look up: "))
        My_List.Find_Record(number)
    elif choice == 4:
        number = int(input("Enter Student number to Remove: "))
        My_List.RemoveFrom_Table(number)












