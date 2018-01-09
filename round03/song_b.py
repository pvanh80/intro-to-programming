def print_verse(animal,its_sound):
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a", animal)
    print("E-I-E-I-O")
    print("With a ", its_sound," ", its_sound," here", sep="")
    print("And a ",its_sound," ", its_sound ," there",sep="")
    print("Here a", its_sound + ",","there a", its_sound)
    print("Everywhere a ", its_sound," ", its_sound,sep="")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()


def main():

    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

main()