counter = 0
for m in range(12):
    if m+1 == 1:
      d=3
      while d<=31:
        if counter % 7==0:
          print(d,m+1,"", sep=".")
        counter+=1
        d+=1

    if m+1 ==2:
        for d in range(28):
            if counter % 7==0:
                print(d+1,m+1,"",sep=".")
            counter += 1
    if m+1 == 3 or m+1 == 5 or m+1 == 7 or m+1 == 8 or m+1 == 10 or m+1 == 12:
        for d in range(31):
          if counter%7==0:
            print(d+1,m+1,"",sep=".")
          counter += 1
    if m+1 == 4 or m+1 == 6 or m+1 == 9 or m+1 == 11  :
        for d in range(30):
            if counter % 7==0:
                print(d+1,m+1,"",sep=".")
            counter += 1