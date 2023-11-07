class Node:
    def __init__(self,nm,pr,st):
        self.name = nm
        self.problems = pr
        self.time = st
        self.ref = None

class LinkedList:
#---------- creatiing empty linked list -----------#
    def __init__(self):
        self.start_node = None

# ---------- Adding a team to the list -----------#
    def Add_to_start(self,nm,pr,st):
        new_node = Node(nm,pr,st)
        new_node.ref = self.start_node
        self.start_node = new_node

# ---------- Traverse and printing the -----------#
    def print_Teams(self):
        print("Linked List: ", end="\n")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            print("\nName      Problems     Time taken(minutes)")
            print("--------------------------------------")
            while n is not None:
                print(n.name, "\t ", n.problems, "\t\t\t", n.time, end="\n")
                n = n.ref
        print("")

# ---------- print Teams with more than 3 problems solved  -----------#
    def Teams_More3(self):
        print("Teams who solved more than 3 Problems:", end = "\n")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            print("\nName      Problems     Time taken(minutes)")
            print("--------------------------------------")
            while n is not None:
                if n.problems > 3:
                    print(n.name, "\t ", n.problems, "\t\t\t", n.time, end="\n")
                n = n.ref
        print("")

    def Winning_teams(self):
        print("\tWinning Teams:", end = "\n")
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            print("\nName      Problems     Time taken(minutes)")
            print("--------------------------------------")
            while n is not None:
                if n.problems == 10:
                    print(n.name, "\t ", n.problems, "\t\t\t", n.time, end="\n")
                n = n.ref
        print("")

#--------Average time taken---------------
    def Average_time(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            sum_vals = self.start_node.time
            count = 1
            current_v = self.start_node.ref
            while current_v is not None:
                sum_vals = sum_vals + current_v.time
                count = count + 1
                current_v = current_v.ref
            Avg = sum_vals / count
            print("\tAverage Time taken was", (round(Avg)),"Minutes")
    print = ("")



# ---------- Main program -----------#

My_List = LinkedList()

choice = 0
while choice != 6:
    print("\n Welcome to team scoring!")
    print("\nThere are 10 questions on the competition")

    print(" 1 = Add Team Name, Problems solved and time taken ")
    print(" 2 = Traverse and print all of List of Teams ")
    print(" 3 = Print all Teams with more then 3 probelms solved")
    print(" 4 = Print the winning teams: ")
    print(" 5 = Print average time taken")
    print(" 6 = Exit")
    choice = int(input("\n Enter Choice: "))

    if choice == 1 :
        name = input("\n Enter Team name: ")
        problems = int(input("\n Enter Number of problems solved: "))
        solved = float(input("\n Enter time taken:  "))
        My_List.Add_to_start(name, problems, solved)
        print(name,"inserted at the beginning")
    elif choice ==  2:
        My_List.print_Teams()
    elif choice == 3:
        My_List.Teams_More3()
    elif choice == 4:
        My_List.Winning_teams()
    elif choice == 5:
        My_List.Average_time()









