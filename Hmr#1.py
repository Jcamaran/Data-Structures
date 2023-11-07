hall = 300
mezzanine = 100
while hall or mezzanine != 0:
    ans = int(input("Enter 1 for Hall, 2 for Mezzanine, 3 to Terminate: "))
    if ans == 1:
        adult = int(input("\nNumber of adults?:  "))
        kid = int(input("\nNumber of children?:  "))
        count = adult + kid
        acost = adult * 10
        kcost = kid * 7
        hall = hall - count
        if hall < 0:
            print("\nThere is not enough seats for your order")
            hall = hall + count
            print("\nThere are ", hall,"seats remaining in the hall please redo your order ")
        else:
            print("Great you got", adult," adult ticket for $", acost,"and", kid, " child tickets for $", kcost,", so your total is $", acost+kcost)
            print(" Remaining seats: Hall", hall,"Mezzanine",mezzanine)
    elif ans == 2:
        adult = int(input("\nNumber of adults?:  "))
        kid = int(input("\nNumber of children?:  "))
        count = adult + kid
        acost = adult * 8
        kcost = kid * 5
        mezzanine = mezzanine - count
        if mezzanine < 0:
            print("\nThere is not enough seats for your order")
            mezzanine = mezzanine + count
            print("\nThere are ", mezzanine,"seats remaining in the mezzanine please redo your order ")
        else:
            print("\nGreat you got", adult," adult ticket for $", acost,"and", kid, " child tickets for $", kcost,", so your total is $", acost+kcost)
            print("\nRemaining seats: Hall", hall,"Mezzanine",mezzanine)
    elif ans == 3:
        break
    else:
        print("invalid choice try again")
        continue
print("\nThank you, and have a great day!")