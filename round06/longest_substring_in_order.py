"""
Task: The longest substring in order
Course: Intro to Programming
Name: Phan Viet Anh
ID: 256296
"""


def longest_substring_in_order(input_string):

    list_temp = list(input_string)  # list stores all letters
    index = 0
    result = ''  # current string
    result_temp = ''  # if e
    list_str = []
    list_empty = ''
    while True:
        # if input string is list of one letter
        if len(list_temp) < 2:
            list_str = list_temp
            break
        else:
            # if last letter are in order added to current string
            if index == len(list_temp) - 1:
                if list_temp[index] > list_temp[index - 1]:
                    result += list_temp[index]
                    list_str.append(result)
                break

            else:
                # letters are in order
                if list_temp[index] < list_temp[index + 1]:
                    result += list_temp[index]

                else:
                    # need a var to store the string when the next character is not in order,
                    # store character at i index
                    result_temp = result + list_temp[index]
                    list_str.append(result_temp)
                    result = ''  # reset result to empty when next character is not in order

            list_str.append(result)

        index += 1

    if len(list_str) == 0:
        return list_empty
    else:

        return max(list_str, key=len)


def main():
    print(longest_substring_in_order(""))
main()

