history = []

r = 0

while True:

    yn = input("Do you want to do calculation yes or no? ")

    if yn.lower() == "no":
        print("Calculation ended")
        break

    a = float(input("Enter number: "))
    op = input("Enter operator +, -, x, /: ")

    if op == "+":

        r += a

    elif op == "-":

        r -= a

    elif op.lower() == "x":

        if r == 0:
            r = 1

        r *= a

    elif op == "/":

        if a == 0:
            print("Cannot divide by zero")
            continue

        r /= a

    else:

        print("Invalid arithmetic operator")
        continue


    history.append(f"{op} {a} = {r}")

    print("Result:", r)


print("\nCalculation History:")

for i in history:
    print(i)
