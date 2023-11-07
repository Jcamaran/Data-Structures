import random

NumL = []
for i in range(0,10):
    ans = int(input("Enter an Integer: "))
    NumL.append(ans)
print(NumL)

print("The sum is", sum(NumL))
print('\nThe Min is,', min(NumL))
print('\nThe Max is', max(NumL))
print('\nthe length of the list is ', len(NumL))
print('\nBefore shuffling', NumL)

random.shuffle(NumL)

print("\nAfter shuffling", NumL)


NumL.sort()
print( "After sorting: ", NumL)

NumL = (set(NumL))

print("This is after removing duplicates: ", NumL)





