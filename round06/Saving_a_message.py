def read_message(prompt):
    result = []
    result.append(input(prompt))

    return result


def main():

    print("Enter text rows to the message. Quit by entering an empty row.")
    #in_string = ""
    while True:
        result = read_message("")
        if result[len(result)-1] == "":
            break
    print("The same, shouting:")
    for e in result:
        print(e.upper())


main()
