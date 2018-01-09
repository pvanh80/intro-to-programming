purchase_price = int(input("Purchase price: "))
p_money = int(input("Paid amount of money: "))
re_turn = p_money - purchase_price
if p_money < purchase_price : print("Need more money!")
if p_money == purchase_price : print("No change")
else:
    print("Offer change:")
    if re_turn%10==0 : print (int(re_turn/10), "ten-euro notes")
    elif re_turn/10>0 :
        print (re_turn/10, "ten-euro notes")
        a = int(re_turn % 10)
        if a >= 5:
            print (int(a / 5), "five-euro notes")
        b = int(a % 5)
        if b >= 2: print(int(b / 2), "two-euro coins")
        c = int(b % 2)
        if c != 0:
            print(c, "one-euro coins")
    else:

        a = int(re_turn%10)
        if a >= 5:

            print (int(a/5), "five-euro notes")
        b = int(a % 5)
        if b >= 2: print(int(b/2),"two-euro coins")
        c = int(b%2)
        if c !=0 :print(c,"one-euro coins" )




