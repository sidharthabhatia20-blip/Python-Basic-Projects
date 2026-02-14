def factorial(a):
    if a == 1 or a == 0:
        return 1
    elif a < 0:
        return "Factorial not for negative numbers"
    else:
        i = a - 1                        
        while i > 0:
            a *= i                       # (a x (i -1) x (i - 2) x ......x 1)
            i -= 1              
        return a
n = int(input("Enter a number: "))
print(f"factorial of {n} is {factorial(n)}")