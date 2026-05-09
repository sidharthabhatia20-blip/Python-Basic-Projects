r = 0
while True:
    yn = input("Do you want to do calculation yes or no? ")
    if yn.lower() == "no":
        print("Calculation ended")
        break
    else:
        a = int(input("Enter number: "))
        b = input("Enter operator +, -, x, (÷ or /): ")
        if b == "÷" or b == "/":
            r //= a
        elif b == "+":
            r += a
        elif b.lower() == "x":
            if r == 0:
                r = 1
            r *= a
        elif b == "-":
            r -= a
        else:
            print("Invalid arithmetic operator")
    print(r)