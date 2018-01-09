def read_number(prompt, errormessage="Incorrect input"):
    try:
        return float(input(prompt))
    except ValueError as e:
        print(errormessage)
        return read_number(prompt,errormessage)

def search_index(time_in, time_table):
    return time_table.index(time_in)

def search_suitable_time(time_in, time_table):
    suitable = 0
    index = 0
    while True:
        if time_in <= time_table[index]:
            suitable = index
            break
        index +=1

    return search_index(time_table[suitable], time_table)

def main():
    time_schedule = [630, 1015, 1415, 1620, 1720, 2000]
    time_in = read_number("Enter the time (as an integer): ")
    print("The next buses leave: ")
    if time_in > 2000 or time_in < 630:

        for item in time_schedule[0:3]:
            print(item)
    else:

        index = search_suitable_time(time_in,time_schedule)

        roller = index + 2
        if roller > len(time_schedule)-1 :
            for item in range(3):
                print(time_schedule[index - len(time_schedule) + item])
        else:
            for item in time_schedule[index:index+3]:
                print(item)

main()