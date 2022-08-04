#Factorial function
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == "__main__":
    n = int(input("Type in a number: "))
    print("The factorial of ", n, "is" , factorial(n))
"""
def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return (n+1)**3 + f(n-1)

if __name__ == "__main__":
    n = int(input("Type in a number: "))
    print("The number is: ", f(n))

