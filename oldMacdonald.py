def main():
    animals = ["cow", "pig", "horse", "duck", "chicken"]
    sounds = ["moo", "oink", "niegh", "quack", "cluck"]

    for i in range(5):
        chorus(animals[i], sounds[i])
        print()

def chorus(animal, sound):
    print("old MacDonald had a farm, Ee-igh, Ee-igh, oh!")
    print("And on that farm he had a " + animal + ", Ee-igh, Ee-igh, oh!")
    print("With a " + sound + ", " + sound + " here and a " + sound + ", " + sound + " there.")
    print("Here a " + sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound + ".")
    print("old MacDonald had a farm, Ee-igh, Ee-igh, oh!")

main()
