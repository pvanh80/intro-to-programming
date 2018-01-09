num_in = int(input("Choose a number: "))
i = 1
while 1:
    print(i, "*", num_in, "= ", num_in * i)
    i += 1
    if num_in * i > 100:
        print(i, "*", num_in, "= ", num_in * i)
        break
