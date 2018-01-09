con_in = input("Bored? (y/n) ")
while con_in !='Y' or con_in !='y':
    if con_in == 'Y' or con_in =='y':
        print("Well, let's stop this, then.")
        break
    elif con_in == 'N' or con_in =='n':
        con_in = input("Bored? (y/n) ")

    else:
        print("Incorrect entry.")
        con_in = input("Please retry: ")