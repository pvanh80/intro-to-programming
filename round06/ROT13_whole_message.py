def encrypt(alphabet):
    REGULAR_CHARS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]

    ENCRYPTED_CHARS = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                            "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m"]

    result = ''
    list_alphabet = list(alphabet)
    for i in range(len(list_alphabet)):
        if list_alphabet[i].isalpha():
            for j in range(len(REGULAR_CHARS)):
                if list_alphabet[i] == REGULAR_CHARS[j]:
                    result += ENCRYPTED_CHARS[j]
                if list_alphabet[i] == REGULAR_CHARS[j].upper():
                    result += ENCRYPTED_CHARS[j].upper()
        else:
            result += list_alphabet[i]
    return result

def row_encryption(in_string):
    return encrypt(in_string)

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    in_string = ''
    result = []
    while True:
        in_string = input("")
        result.append(row_encryption(in_string))
        if in_string == "":
            break
    print("ROT13:")
    for e in result:
        print(e)
main()


