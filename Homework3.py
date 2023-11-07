MagicWord = ("photosynthesize")
guessList = ["_" for i in range(len(MagicWord))]
print("Welcome to Hangman game!")
guesses = 0
count = 0
while True:
    letter = str(input("guess a letter: "))
    goodL = ("".join(guessList))
    if guesses == 21:
        print("Sorry There were only a maximum of 20 guesses :(")
        break
    elif goodL == "photosynthesize":
        print("\nCONGRATULATIONS")
        print(f"\nIt took you,{guesses} guesses to find the Magic word.")
        break
    elif letter in MagicWord:
        for x in range(len(MagicWord)):
            if MagicWord[x] == letter:
                guessList[x] = letter
                goodL = ("".join(guessList))
        print("Correct!...Here is your current status")
        print(goodL)
    else:
        print("Sorry no letters match your input, try again!")
        print(goodL)
    guesses += 1
print("\nThank you for playing Hangman!")


