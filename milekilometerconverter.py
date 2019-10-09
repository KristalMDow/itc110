# milekilometerconverter.py
# convert kilometers to miles

def main():
    print("This program converts kilometers to miles.")
    #input
    kilometers = eval(input("Enter the distance in kilometers:")) #convert string and store
    #processing
    miles = kilometers * .62
    #output
    print("The distance is", miles, "miles.")

main()
