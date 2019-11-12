# makeacronym.py
# Kristal Dow 11/5/19
# Write a program that creates an acronym of the phrase given.

def main() :
    print("This program builds acronyms.\n")
    phrase = input("Enter a phrase:")

    acronym = "".join(e[0] for e in phrase.split())

    print(acronym)

main()
