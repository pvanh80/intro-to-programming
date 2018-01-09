p1 = input("Player 1, enter your choice (R/P/S): ")
p2 = input("Player 2, enter your choice (R/P/S): ")
if p1=="P" :
    if p2 =="S": print("Player 2 won!")
    else:
        if p2 =="R": print("Player 1 won!")
        else: print("It's a tie!")
if p1 =="R" :
    if p2 == "P": print("Player 2 won!")
    else:
        if p2 =="S": print("Player 1 won!")
        else: print("It's a tie!")
if p1 =="S":
    if p2 == "P": print("Player 1 won!")
    else:
        if p2 =="R": print("Player 2 won!")
        else: print("It's a tie!")