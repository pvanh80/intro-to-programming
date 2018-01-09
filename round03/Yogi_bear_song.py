def repeat_name(name, reps):
    for i in range(reps):
        print(name + ",", name + " Bear")


def print_name(na):
    print(na + ", " + na)


def verse(lyric, name):
    print(lyric)
    print_name(name)
    print(lyric)
    repeat_name(name, 3)
    print(lyric)
    repeat_name(name, 1)
    print()

def main():

        verse("I know someone you don't know", "Yogi")
        verse("Yogi has a best friend too", "Boo Boo")
        verse("Yogi has a sweet girlfriend", "Cindy")

main()