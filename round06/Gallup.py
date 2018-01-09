#Intro to Programming
#Coffee Gallup
#Phan Viet Anh - 256296

def read_input(input):
    print()

def remove_zero_correspondent(list):
    count=0
    for i in range(len(list)-1):
        if list[i]<=0:
            list.remove(list[i])
            count+=1
    return count, list

def read_number(prompt, errormessage="Incorrect input!"):
    try:

        return int(input(prompt))
    except ValueError as e:
        print(errormessage)
        return read_number(prompt,errormessage)

def main():
    list_result = []
    print("Enter one response per line. End by entering an empty row.")
    while True:
        correspondent = input("")
        if str(correspondent) == "":
            break
        else:
            try:
                x = int(correspondent)
                if x >= 0:
                    list_result.append(x)
                else:
                    print("Error Value")

            except ValueError:
                print("Error: Wrong Value !")
    nums_non_coffee_drinker, list_result_after = remove_zero_correspondent(list_result)
    print("Removed " + str(nums_non_coffee_drinker) +" non-coffee-drinkers responses")
    print(list_result)
    print(list_result_after)
main()
