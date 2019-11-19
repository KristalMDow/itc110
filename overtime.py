#    overtime.py
#    A program that computes someone's pay.
#    By Kristal Dow 11-18-2019

def main():
    print("Weekly pay calculator\n")
    
    hrs = float(input("Enter hours worked: "))
    wages = float(input("Enter hourly wage: "))

    pay = 0
    
    if hrs > 40:
        pay = ((hrs-40)*1.5*wages)+40*wages
    else:
        pay = hrs*wages

    print("Your week's pay is " + str(pay))

main()
