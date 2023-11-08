MagicWord = ("Hang in there bro")
guessList = ("---- -- ----- ---")
print("Welcome to Hangman game!")
guesses = 0
while True:
    letter = str(input("guess a letter: "))
    if guesses == 21:
        print("Sorry There were only a maximum of 20 guesses :(")
        break
    elif guessList == MagicWord:
        print("CONGRATULATIONS")
        print(f"\nIt took you,{guesses} guesses to find the Magic word.")
        break
    elif letter in MagicWord:
        for x in range(len(MagicWord)):
            if MagicWord[x] == letter:
                print("Correct!...Here is your current status")
        guessList = guessList.replace(guessList[x], letter)
        print(guessList)
    else:
        print("Sorry no letters match your input, try again!")
        print(guessList)
    guesses += 1
print("\nThank you for playing Hangman!")


