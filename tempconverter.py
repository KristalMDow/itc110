# tempconverter.py
# convert celsius to fahrenheit

def main():
    #input
    celsius = eval(input("Enter the temp in Celsius ")) #convert string and store
    #processing
    fahrenheit = 9/5 * celsius + 32
    #output
    print("The fahrenheit temp is ", fahrenheit)
    input("Press the <Enter> key to quit.")

main()
