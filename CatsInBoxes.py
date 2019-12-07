# catsinboxes.py
# Calculates cats in boxes over time and releases hounds to remove some.

from cats import Cats

def main():
    numOfBoxes = int(input("How many boxes do you have?"))

    totalCats = Cats(numOfBoxes)
    totalCats.accrueCats()
    print("Oh no! There are " + str(totalCats.getValue()) + " cats in your boxes!")
    totalCats.accrueCats()
    print("Wait, there are " + str(totalCats.getValue()) + " cats, now.")
    totalCats.accrueCats()
    print("Heck, actually NOW there are " + str(totalCats.getValue()) + " cats!")

    answer = int(input("Let's get rid of them. How many dogs should we let out?"))
    totalCats.releaseHounds(answer)
    print("Okay, now there are " + str(totalCats.getValue()) + " cats.")

if __name__ == "__main__":
    main()
