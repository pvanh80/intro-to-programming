def read_number(prompt, errormessage="Incorrect input !"):
    try:
        return int(input(prompt))
    except ValueError as e:
        print(errormessage)
        return read_number(prompt, errormessage)
def search_in_list(my_list, x):
    count=0;
    index=0
    while index < len(my_list):
        if x == my_list[index]:
            count+=1
        index+=1
    return count
def input_to_list(n):
    my_list = []
    print("Enter " + str(n) + " numbers: ")
    i = 1
    while i <= n:
        x = read_number("")
        my_list.append(x)
        i += 1
    return my_list
def main():
    n = read_number("How many numbers do you want to process: ")
    my_list = input_to_list(n)
    number = read_number("Enter the number to be searched: ")
    found = search_in_list(my_list,number)
    if found!=0:
        print( str(number) +" shows up "+ str(found)+ " times among the numbers you have entered.")
    else:
        print(str(number) + " is not among the numbers you have entered.")
main()