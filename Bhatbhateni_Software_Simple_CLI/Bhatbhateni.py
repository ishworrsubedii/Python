# Develop a Software for Bhatbhateni Software for multiple Customer using list. (Also system can check the discount)
# 1) TOTAL PRICE <= 5000    5 % DISCOUNT
#     2) TOTAL PRICE <= 8000    8 % DISCOUNT
#     3) TOTAL PRICE <= 10000    10 % DISCOUNT

#     4) TOTAL PRICE > 10000 OR MORE    15 % DISCOUNT

#     Need to calculate total discount(if 8000 then initial discount for 5000 and next 3000 need to sum and finalize total discount on the category 8000)

#     Basic function:
#     a) InitialDisplay()
#     b)inputInformation()
#     c)calculate()  # with discount check
#     d)display()
#     e) all console print should be in the file write.


# creating empty list to store values
from datetime import date


def initialDisplay():
    Display = f'''            Bhatbhateni Billing System
                                Maitidevi, Kathmadu                         
                                            Date:{date.today()}'''


def inputInformation():
    no_Cus = int(input("Enter the no of customer:"))
    no_items = int(input("Enter the no of Items:"))
    cusId = []
    cusName = []
    cusAddress = []
    cusEmail = []
    cusPh = []
    itemsName = []
    quantity = []
    price1 = []
    totalPrice = []

    for i in range(no_Cus):
        id = int(input(f"Enter the Id of customer[{i+1}]:"))
        cusId.append = (id)

        name = input(f"Enter the name of customer[{i+1}]:")
        cusName.append = (name)

        address = input(f"Enter the customer address[{i+1}]:")
        cusAddress.append = (address)

        email = input(f"Enter the Customer email[{i+1}]:")
        cusEmail.append = (email)

        ph_no = int(input(f"Enter the customer Ph.np[{i+1}]:"))
        cusPh.append = (ph_no)

        for j in range(no_items):
            i_Name = input("Enter the Name of item:")
            itemsName.append = (i_Name)

            i_quantity = int(input(f'''Quantity of item[{j+1}]:'''))
            quantity.append = (i_quantity)

            i_price1 = int(input("Unit Price of item[{j}]:"))
            price1.append = (i_price1)

            t_Price = int(input(f"TotalPrice:", (i_quantity*i_price1)))
            totalPrice.append = (t_Price)

    return no_Cus, no_items, cusName, cusAddress, cusEmail, cusPh, itemsName, quantity, price1, totalPrice


def calculation(totalPrice):
    netAmount = []
    discount = []
    if totalPrice <= 5000:
        disAmt = (totalPrice*0.05)
        AmtAterDis = totalPrice-discount

    elif 5000 > totalPrice <= 7000:
        disAmt = (totalPrice-5000)*0.08 + (2000*0.05)
        AmtAfterDis = totalPrice-discount

    elif 7000 < totalPrice <= 10000:
        disAmt = (5000*0.05)+(2000*0.08)+(totalPrice-7000)*0.10
        AmtAfterDis = totalPrice-discount
    else:
        disAmt = (5000*0.05)+(2000*0.08)+(3000*0.10)+(totalPrice-10000)*0.15
        AmtAfterDis = totalPrice-discount

    discount.append(disAmt)
    netAmount.append(AmtAfterDis)

    return netAmount, discount


initialDisplay()
nCus, nitems, cName, cAddress, cEmail, cPh, iName, qty, price, tPrice = inputInformation()
netAmt, disAmt = calculation(totalrice)
