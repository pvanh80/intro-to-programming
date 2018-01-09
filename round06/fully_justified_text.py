# http://codereview.stackexchange.com/questions/95505/text-justification


def main():
    in_string = "Although a prince may rise from a private station in two ways, neither"
    list_para = list(in_string)
    print(in_string)
    num_char_per_line = 20
    len_string = len(in_string)
    row = len_string//num_char_per_line
    index = num_char_per_line
    while index < len(list_para):
        if list_para[index] == " ":
            list_para.insert(index,"\n")
        else:

            decrease_index = index
            while decrease_index > 0:

                if list_para[decrease_index] == " ":
                    list_para[decrease_index] = "\n"
                    index = decrease_index
                    break
                decrease_index -= 1

                num_spacing_added = num_char_per_line % index - 1

                # when we have the number of spaces should be added in the line
                # then we a list with elements already are seperated by line
                # Now just go through all elements of the list, then add num of
                # nesscesary spaces in to elements

                # use absolute to know where to start the list
                while True:
                    for i in range(len(list_para[:index - 1])):

                        if list_para[i] == " ":
                            list_para[i] += " "

                            num_spacing_added -= 1

                    if num_spacing_added == 0:
                        break

        index += num_char_per_line

    print(''.join(list_para))

main()