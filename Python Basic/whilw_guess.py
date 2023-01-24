n=9
i=0
while i<3:
    guess=int(input("Enter the number"))
    
    if guess== 9:
     print("won")
     break
    else:
        print("Enter again: ")
        i+=1