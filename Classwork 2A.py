
def TempConvert(temp):
    c  = (5.0/9.0) * (temp - 32.00)
    return c
print("==================")
print("Fahrenheit  Celsius")
for f in range(50,101,5):
    celsius = TempConvert(f)
    print(f,"\t\t\t\t",round(celsius,0))
