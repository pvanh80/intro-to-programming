def get_first_letter(in_string):
    list0 = list(in_string)
    first_letter = list0[0].upper()
    return first_letter

def create_an_acronym(string_input):
    string_result = ''
    list_string = string_input.split(" ")
    for e in list_string:
        string_result +=get_first_letter(e)
    return string_result
