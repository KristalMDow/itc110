# pizzaPricePerInch.py
# Calculates the price of a pizza per inch.

import math

def main():
    print("This program computes the cost per square inch of a pizza.\n")
    
    #input
    diameter = eval(input("Enter the diameter of the pizza (in inches): "))
    pizzaPrice = eval(input("Enter the price of the pizza (in cents): "))
    
    #processing
    pricePerSqInch = round(pizzaPrice/(math.pi*((diameter/2)**2)), 1)
    
    #output
    print("\nThe cost is", pricePerSqInch, "cents per square inch.")

main()
