def full_justify(words, L):
    first_word = 0
    num_words = 0
    characters_in_line = 0
    solution = []
    for i in range(0, len(words)):
        if characters_in_line + num_words + len(words[i]) > L:
            line = []
            if num_words > 1:
                spaces = (L - characters_in_line) // (num_words - 1)
                extra_spaces = (L - characters_in_line) % (num_words - 1)
            for j in range(first_word, i):
                line.append(words[j])
                if j == i - 1:
                    break
                for n in range(0, spaces):
                    line.append(' ')
                if j - first_word < extra_spaces:
                    line.append(' ')
            if num_words == 1:
                for n in range(len(words[first_word]), L):
                    line.append(' ')
            solution.append(''.join(line))
            first_word = i
            num_words = 0
            characters_in_line = 0
        num_words += 1
        characters_in_line += len(words[i])
    line = []
    if first_word == 0 or first_word < len(words):
        line = []
        for j in range(first_word, len(words)):
            line.append(words[j])
            if j == len(words) - 1:
                break
            line.append(' ')
        for n in range(len(''.join(line)), L):
            line.append(' ')
        solution.append(''.join(line))
    return solution


def read_number(prompt, error_message="Wrong input"):
    try:
        return int(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    print("Enter text rows. Quit by entering an empty row.")
    words = ""
    words_result = ""
    while True:

        words = input("")

        words_result += words + " "

        if words == "":
            break

    num_chars_per_line = read_number("Enter the number of characters per line: ")
    # print(words_result)
    justified_list = full_justify(words_result.split(" "), num_chars_per_line)

    for element in justified_list:
        print(element)


main()















