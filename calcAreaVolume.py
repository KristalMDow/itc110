import math

def main():
    inputRadius = float(input("Enter the radius of a sphere:"))
    print("Your area is: " + str(round(sphereArea(inputRadius), 2)) + "\nYour volume is: " + str(round(sphereVolume(inputRadius), 2)))

def sphereArea(radius):
    area = 4 * math.pi * radius**2
    return area

def sphereVolume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

main()
