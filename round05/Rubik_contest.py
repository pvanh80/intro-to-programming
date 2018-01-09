def read_numer(prompt, errormessage="Incorrect input !"):
    try:
        return float(input(prompt))
    except ValueError as e:
        print(errormessage)
        return read_numer(prompt,errormessage)


def main():
    total = 0
    result = []
    NUMBERS = 5
    i = 0
    while i<NUMBERS:
        x = read_numer("Enter the time for performance " + str(i+1)+ ": ")
        i +=1
        result.append(x)
    result.remove(max(result))
    result.remove(min(result))
    for item in result:
        total +=item
    average = float(total/len(result))
    print("The official competition score is " +str(format(average,'.2f')) +" seconds.")
main()