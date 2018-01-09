# TIE-02100 Johdatus ohjelmointiin
# dictionary
# Phan Viet Anh


def print_dict_one_line(diction):
    print("Dictionary contents:")
    print(", ".join(word for word in sorted(diction)))


def print_dict_eng_spa(diction):

    print()
    print("English-Spanish")

    for word in sorted(diction):
        print(word + " " + diction[word])


def print_dict_spa_eng(diction):
    print()
    print("Spanish-English")

    spa_eng = {}

    for key in diction:

        spa_eng[diction[key]] = key

    for element in sorted(spa_eng):
        print(element + " " + spa_eng[element])

    print()


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print_dict_one_line(english_spanish)
    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")

            if word in english_spanish:
                print(word, "in Spanish is " + english_spanish[word])

            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            key_dict = input("Give the word to be added in English: ")
            value_dict = input("Give the word to be added in Spanish: ")
            english_spanish[key_dict] = value_dict
            print_dict_one_line(english_spanish)

        elif command == "R":
            word_remove = input("Give the word to be removed: ")
            if word_remove in english_spanish:
                del english_spanish[word_remove]
            else:
                print("The word", word_remove, "could not be found from the dictionary.")

        elif command == "Q":
            print("Adios!")
            return

        elif command == "P":
            print_dict_eng_spa(english_spanish)
            print_dict_spa_eng(english_spanish)

        elif command == "T":
            text_translate = input("Enter the text to be translated in Spanish: ")
            text_list = text_translate.split(" ")

            for element in range(len(text_list)):

                if text_list[element] in english_spanish:
                    text_list[element] = english_spanish[text_list[element]]

            print("The text, translated by the dictionary: ")
            print(" ".join(text_list))

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
