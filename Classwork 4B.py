price = { "Banana": 1.5, "Apple":2.3,
       "Orange": 4.5, "Cherries":6.0}
count = {"Banana": 35, "Apple": 42,
      "Orange": 40, "Cherries": 12}

print("Fruit       Price      Stock     Value")
print("=======================================")
sum = 0
for x in price :
    print(x, "\t\t", price[x], "\t\t",count[x],"\t",(price[x] * count[x]))
    sum = sum + (price[x] * count[x])

print("\nThe sum of all values is: ",sum)


