#    windchill.py
#    A program that computes a table of windchill.
#    By Kristal Dow 11-24-2019

def main():
    print("Wind Chill Table\n")

    # T = temperature in fahrenheit
    # V = windspeed in mph
    T = -20
    V = 0

    # Temperature is -20 to 60
    # Speed range is 0 to 50 in 5 mph increments

    print("             Temperature\n MPH| -20 -10   0  10  20  30  40  50  60\n----+--------------------------------------")
    # Loop through temperature
    for V in range(0, 55, 5):
        if V < 0:
            print(" " + str(V) + "|", end="")
        elif V <=5:
            print("   " + str(V) + "|", end="")
        else:
            print("  " + str(V) + "|", end="")
        for T in range(-20, 70, 10):
            # Formula to calculate index.
            windchillIndex = round(35.74+(0.6215*T)-(35.75*(V**0.16))+((0.4275*T)*(V**0.16)))
            if windchillIndex < -9:
                print(" " + str(windchillIndex), end="")
            elif windchillIndex < 0:
                print("  " + str(windchillIndex), end="")
            elif windchillIndex <=9:
                print("   " + str(windchillIndex), end="")
            else:
                print("  " + str(windchillIndex), end="")
        print("")
    
main()
