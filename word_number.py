a = input("Set a word/number: ")
b = 0
c = 5
while (True):
    print(f"You have {c} chances to enter word correctly")
    b += 1
    print("This is your",b, "attempt")
    b += 1
    d = input("Enter your guess: ")
    if (a.lower() == d.lower()):
        print("You won the game")
        break
    elif c == 1:
        print("You have finished your attempts")
        break
    c -= 1