def count_abbas(input_string):
    list_temp = list(input_string)
    i = 0
    count = 0
    a = ''
    comp_string = 'abba'
    while i < len(list_temp):

        if list_temp[i] == 'a':
            a = list_temp[i] + list_temp[i-1] + list_temp[i-2] + list_temp[i-3]

            if a == comp_string:
                count += 1
        i += 1

    return count


