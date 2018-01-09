num_in = int(input("How many numbers would you like to have? "))
i = 1
while i<=num_in:
    if i%3==0 and i%7==0 : print("zip boing")
    elif i%3==0: print("zip")
    elif i%7==0: print("boing")
    else: print(i)
    i = i+1