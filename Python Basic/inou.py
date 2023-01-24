

# num =1234
# i=0

# while i<=3:
#     list=num%10
#     i+=1
#     print(i)
# # if len(str(num))<=4:
# #     print(str(i)+",",end="")

# flag = True

# while flag:

#     num = str(input("Enter your 3 hot numbers"))

#     if len(num) == 4:

#         flag = False
#         while num<0:


#         print(f"{num[0]},{num[1]},{num[2]},{num[3]}")

#         break

#     else:

#         print("Your input should be exactly 3 digit or this code doesn't work because I am don")

#         print("Try again")


# from ast import Num





# num=12345
# t=num
# store=0
# for i in range(0,len(num)):
#     last=t%10
#     store=store+last

#     if len(str(num)):
#             print(str(store)+"," end=" ")

#     else:
#          print(str(store),end="")
#          t=int(t/10)


num=str(input("Enter the number"))

count=len(str(num))
num=num%2

print(count)

