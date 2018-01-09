# Intro to Programming
# The censor - C Task
# Phan Viet Anh
# 256296


def mark_replace(word_content, censored_word, censored_mark ):
    """
    Replacing the censored word by given mark

    :param word_content: a list of words need to be censored
    :param censored_word: black list word
    :param censored_mark: a given mark
    :return: a list of word after replacing censored word by marks

    """

    for index in range(len(word_content)):

        if word_content[index].lower() == censored_word.lower():
            word_content[index] = censored_mark

    return word_content


def censored(black_list, content_list):
    """

    This function is going to go though every word in black list, then compare
    those word with word in the content message. If there are word need to be
    censored, then it replaces them with given mark

    :param black_list: a list of word need to be censored
    :param content_list: a message with some word need to be censored
    :return: a list of words after being censored

    """

    word_saved = []

    censored_mark = "###"

    for word in black_list:
        for element in range(len(content_list)):

            word_in_content = content_list[element].split(" ")

            censored_word_list = mark_replace(word_in_content,word,censored_mark)

            censored_word = " ".join(e for e in censored_word_list)

            content_list[element] = censored_word

    return content_list


def main():
    black_list = []
    censor_list = []
    content_list = []
    print("Enter the blacklist. Quit by entering an empty row.")
    while True:

        black_word = input("")

        if black_word == "":
            break

        black_list.append(black_word)

    print("Enter text rows to the message. Quit by entering an empty row.")

    while True:

        word_content = input("")

        if word_content == "":
            break

        content_list.append(word_content)

    censor_list = censored(black_list, content_list)

    print("Censored message:")

    for element in censor_list:

        print(element)


main()
