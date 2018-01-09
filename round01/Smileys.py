smiley = int(input('How do you feel? (1-10) '))
if smiley >= 1 and smiley <= 10:
    if smiley == 10: print ("A suitable smiley would be :-D")
    else:
        if smiley >=8 and smiley<=9 : print("A suitable smiley would be :-)")
        else:
            if smiley >=3 and smiley <=7: print("A suitable smiley would be :-|")
            else:
                if smiley ==2: print("A suitable smiley would be :-(")
                else :
                    if smiley ==1: print("A suitable smiley would be :'(")
else :
    print("Bad input!")
