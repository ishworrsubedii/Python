conversion=(input("Enter l for pound and k for kilo"))
weight=int(input("Enter your weight"))
print(weight)
if conversion=='l' or 'L':
    x=weight / 0.45
    print(x,"pounds")
elif conversion=='k' or 'K':
    y=weight *0.45
    print(y,"kg")

else:
    print("*Enter valid input")