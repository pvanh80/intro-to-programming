con_in = input("Answer Y or N: ")
while con_in !='Y' or con_in !='N' or con_in !='y' or con_in !='n':
    if con_in == 'Y' or con_in =='y':
        print("You answered ",con_in)
        break
    elif con_in == 'N' or con_in =='n':
        print("You answered",con_in )
        break
    else:
        print("Incorrect entry.")
        con_in = input("Please retry: ")