
def vowel_constonant(str):
    str_list = list(str)
    i=0
    vowel = 0
    consonant = 0
    while i<len(str_list):
        if str_list[i] in ('a', 'e', 'i', 'o', 'u', 'y'):
            vowel+=1
        else:
            consonant+=1
        i+=1
    return vowel, consonant

def main():
    input_string = input("Enter a word: ")
    vowels, consonant = vowel_constonant(input_string)
    print("The word " + input_string + " contains " + str(vowels)+" vowels and "+ str(consonant) +" consonants")
    #print(input_string.split())
main()






