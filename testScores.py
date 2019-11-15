def main():
    print("The Test Scores program\n\nEnter 999 to end input\n=============")

    score = 0
    counter = 0
    total = 0

    while (score != 999):
        score = eval(input("Enter test score:"))
        total = total + score
        counter = counter + 1

    average = total / counter

    print("============\nTotal Score:" + str(total) + "\nAverage Score:" + str(average))

main()
