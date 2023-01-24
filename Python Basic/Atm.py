# Write a program in java that takes a 4-digit PIN from the user. The user should have a total of 3
# attempts of putting in the PIN. If incorrect, the user should be warned with the remaining attempts.
# P.S. Actual PIN is 5730
# Output:
# Please input the PIN: <take input>
# Sorry, your PIN is incorrect. You have 2 attempts left.

# pin=5730




pin=int(input("Enter the 4 digit number: "))

att=0
while att<3:

    if pin==5730:
        print("Access granted")
        break

    else:
        print("Incorrect pin")
    
        pin=int(input("Enter the 4 digit number: "))
        att+=1
        if att==3:
            print("Enter the valid pin: ")
            break
        

