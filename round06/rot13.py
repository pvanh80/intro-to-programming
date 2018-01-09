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
            if list_alphabet[i]== REGULAR_CHARS[j]:
              result += ENCRYPTED_CHARS[j]
            if list_alphabet[i]== REGULAR_CHARS[j].upper():
              result += ENCRYPTED_CHARS[j].upper()
        else:
          result+=list_alphabet[i]
    return result

def row_encryption(in_string):
    return encrypt(in_string)