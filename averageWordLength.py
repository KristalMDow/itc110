# Write a program that calculates the average word length in a sentence entered by the user.

def main() :
    print("Average word length")
    print()

    phrase = input("Enter a phrase.")

    count =0
    total=0
    for word in phrase.split():
        total = total + len(word)
        count = count + 1

    print ("Average word length", total/count)

main()
    
