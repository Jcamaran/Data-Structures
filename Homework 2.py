import array
import random

rNum = array.array("i",[])
for j in range(0,5000):
    x = random.randint(0,20000)
    rNum.append(x)
    rNum = (sorted(rNum))
print(rNum)

# writing linear way
while True:
    x = int(input("\nPlease enter an Integer to search: "))
    if x < 0 or x > 20000:
        print("invalid choice try again")
        continue
    else:
        a = rNum.count(x)
        print("\n",x, "Was found,", a, "times")
        break

# Writing binary function
def BinarySearch(s):
    l = 0
    r = len(rNum) - 1
    while (l <= r):
        m = (l + r) // 2
        if (rNum[m] == s):
            return m
        elif(rNum[m] < s):
            l = m + 1
        else:
            r = m - 1

while True:
    x = int(input("\nEnter number to search in binary form between 0, and 20,000: "))
    loc =  BinarySearch(x)
    if x < 0 or x > 20000:
        print("invalid choice try again")
        continue
    else:
        break

if loc == -1:
    print(x,"was not found in the array")
else:
    print(x,"found at location", loc)
