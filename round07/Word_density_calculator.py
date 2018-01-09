

def main():
    word_storage = []
    content_list = []
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:

        black_word = input("")

        if black_word == "":
            break

        word_storage.append(black_word)

    content = " ".join(word for word in word_storage).lower()

    word_list = content.split(" ")

    word_list.sort()

    for index in range(len(word_list)):

        if word_list[index] != word_list[index-1]:

            print(word_list[index] + ' : ' +
                  str(word_list.count(word_list[index])) + " times")

main()
