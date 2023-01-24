#write a program to find wheather a given number is prime or not
x=int(input("Enter the number "))
if(x>0):
    for i in range(2,x):
     if x%2==0:
        print("not prime num")
        break
    else:
        print("prime number")
        
        
else:
    print("Enter the valid num")
