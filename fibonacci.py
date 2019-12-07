#    fibonacci.py
#    A program that computes the nth Fibonacci value.
#    By Kristal Dow 11-24-2019

def main():
    print("This program calculates the nth Fibonacci value.\n")
    
    n = float(input("Enter the value of n: "))

    i = 1
    total = 0
    num1=0
    num2=1

    while i<n:
        total = num1+num2
        num1=num2
        num2=total
        i += 1

    print("The nth Fibonacci number is " + str(total))

main()
