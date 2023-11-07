import array
A = array.array("i",[])
for i in range(0,10):
    x =  int(input(" Enter an Integer: "))
    A.append(x)
print(A)

sum = 0
for mem in A:
    sum = sum + mem
print("The sum is", sum)
avg = sum / 10
print("\nThe averge is", avg)

print("Numbers bigger than average are")
for mem in A:
    if mem>avg:
        print(mem, end=",")

print("\nThe maximum number in this array is", max(A))
print("\nThe minimum number in this array is", min(A))
