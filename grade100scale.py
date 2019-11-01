def main() :

    score = int(input("Enter your exam score: "))
    grades = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"
    print("Your grade is: " + grades[score])

main()
