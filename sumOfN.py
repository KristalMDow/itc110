def main():
    inputN = int(input("Enter a number:"))
    print("The sum of the first n natural numbers is: " + str(sumN(inputN)))
    print("The sum of the cubes of the first n natural numbers is: " + str(sumNCubes(inputN)))

def sumN(n):
    # returns the sum of the first n natural numbers
    sumNatural = 0
    for i in range(n+1):
        sumNatural = sumNatural + i

    return sumNatural

def sumNCubes(n):
    # returns the sum of the cubes of the first n natural numbers.
    sumAndCube = 0
    for i in range(n+1):
        sumAndCube = sumAndCube + (i**3)

    return sumAndCube

main()
