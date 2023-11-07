def Check_Bracket(ans):

    Stack = []
    open_brackets = ['(', '[', '{']
    closed_brackets = [')', ']', '}']
    pairs = {'(': ')', '[': ']', '{': '}'}

    for x in ans:
        if x in open_brackets:
            Stack.append(x)
        elif x in closed_brackets:
            if not Stack:
                return "Wrong bracket closed but never opened"
            else:
                Last = Stack.pop()
                if pairs[Last] != x:
                    return "Wrong mismatched brackets"

    if Stack:
        return "Wrong bracket opened but never closed"
    else:
        return "Correct"


ans = input("Enter a string with parentheses: ")
x = Check_Bracket(ans)
print(x)
