#intro to programming
# lambda functions
# Phan Viet Anh
# 256296



def sort_neglecting_case(list_in):

    return sorted(list_in, key=lambda word: word)


def järjestä_kirjainkoosta_välittämättä(list_in):

    return sorted(list_in, key=lambda word: word.lower())


def järjestä_luvut_aakkosjärjestykseen(list_in):

    return sorted(list_in, key=lambda number: str(number))

def tulosta_nurinpäin_aakkostettuna(english_spanish):
    for word in sorted(english_spanish, key=lambda word: english_spanish[word]):
        print(english_spanish[word], word, sep=" ")


def sum(a, b):
    return a + b


def main():
    vehicles = ["Mercedes", "BMW", "Lada", "car", "Audi", "automobile"]
    integers = [10, 1, 101, 2, 111, 212, 100000, 22, 222, 112, 10101, 1100, 11, 0]
    #print(järjestä_kirjainkoosta_välittämättä(vehicles))
    #print(järjestä_luvut_aakkosjärjestykseen(integers))

    english_spanish = {"hi": "hola", "thanks": "gracias", "yes": "si", "no": "no"}
    tulosta_nurinpäin_aakkostettuna(english_spanish)
    s = lambda a, b: a + b
    add  = sum(5,6)
    #print(add(5,6))
    dict_name={"+": lambda a,b: sum(a,b)}
    total = dict_name["+"]
    print(total(5,6))
    
main()
