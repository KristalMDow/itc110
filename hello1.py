#hello with an argument

def hello(personName):
    print("Hello", personName, "How are you today?")

def main():
    person = input("Enter your name ")
    hello(person)

main()
