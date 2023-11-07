import math
def getArea(r):
    a = math.pi * math.pow(r,2)
    return a

def getCircumference(r):
    c = 2 * math.pi * r
    return c
print("Number       Area     Circumference")
print("======================================")
for r in range(1,11):
    print(r,"\t\t\t",round(getArea(r),1),"\t\t", round(getCircumference(r),1))

print("\nThank you!")