def longest_substring_in_list(input_string):
    list_temp = list(input_string)
    i = 0
    result = ''
    result_temp = ''
    list_str = []
    longest_substring = ''
    while True:

        if len(list_temp) < 2:
            list_str = list_temp
            break
        else:
            if i == len(list_temp) - 1:
                if list_temp[i] > list_temp[i - 1]:
                    result += list_temp[i]
                    list_str.append(result)
                break

            else:
                if list_temp[i] < list_temp[i + 1]:
                    result += list_temp[i]

                else:
                    # need a var to store the string when the next character is not in order,
                    # store character at i index
                    result_temp = result + list_temp[i]
                    list_str.append(result_temp)
                    result = ''  # reset result to empty when next character is not in order

            list_str.append(result)

        i += 1
    return list_str


def longest_substring_in_order(input_string):
    list_temp = list(input_string)
    i = 0
    result = ''
    result_temp = ''
    list_str = []
    longest_substring = ''
    while True:

        if len(list_temp) < 2:
            list_str = list_temp
            break
        else:
            if i == len(list_temp) - 1:
                if list_temp[i] > list_temp[i - 1]:
                    result += list_temp[i]
                    list_str.append(result)
                break

            else:
                if list_temp[i] < list_temp[i + 1]:
                    result += list_temp[i]

                else:
                    # need a var to store the string when the next character is not in order,
                    # store character at i index
                    result_temp = result + list_temp[i]
                    list_str.append(result_temp)
                    result = ''  # reset result to empty when next character is not in order

            list_str.append(result)

        i += 1

    j = 0
    while j < len(list_str):

        # for e in range(len(list_str)):
        if len(list_str[j]) < len(list_str[j - 1]):
            list_str.remove(list_str[j])
            # else:
            # list_str.remove(list_str[j-1])

        j += 1

    final_list = list_str

    k = 0
    while k < len(final_list):

        if input_string.find(final_list[k]) < input_string.find(final_list[k - 1]):
            longest_substring = final_list[k]

        k += 1
    # long_substring = list_str[len(list_str) - 1]

    return final_list


def main():
    a = "abcabcdefgabab"

    b = "xyzstuopqklmefgabc"

    # print(longest_substring_in_order(a))

    # print(longest_substring_in_list(a))

    print(longest_substring_in_list(b))

    print(longest_substring_in_order(b))

    print(a.find("bc"))


main()





