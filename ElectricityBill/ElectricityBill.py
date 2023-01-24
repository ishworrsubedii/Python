"""Write a program to calculate the electricity bill(accept number od unit from user) according to the following criteria
	Unit				Price
	First 100 unit			no charge
	Next 100 nuit			Rs 5 per unit
	After 200 units			Rs 10 oer unut
(for example if input unit is 350 than total bill amount rs 2000)"""


owner_name = (input("Enter the owner name: "))
owner_address = (input("Enter the owner address: "))
electricity_unit = int(input("Enter the total unit consumed: "))
print("**************Sunway International Electricity Billing System***************")
print("****************************Maitidevi,Kathmandu****************************")
print("Consumer Name: ", owner_name)
print("Consumer Address: ", owner_address)
print("Consumed Unit: ", electricity_unit)


if electricity_unit <= 100:
    print("You dont have to pay for the bill")


elif 200 >= electricity_unit > 100:
    a = electricity_unit - 100
    total_amount = a * 5
    discount=0

    print("Total amount to pay= ", total_amount)
    print(f'The total bill amount of {electricity_unit} unit is Rs {total_amount}')
    print(f' {owner_name} Customer of Sunway international Electricity billing system has to pay total amount {total_amount} with discount price {discount}')

elif electricity_unit > 200:


    a = electricity_unit - 100
    b = 100 * 5
    c = a - 100
    d = c * 10

    total_amount = b + d
    discount=0
    if electricity_unit>500:
        total_unit=electricity_unit-500
        discount=total_unit*10/100
        print(f'Total discount price: {discount}')

    print("Total amount to pay= ", total_amount)
    print(f'{owner_name} Customer of Sunway international Electricity billing system has to pay total amount {total_amount - discount} with discount price {discount}')

else:
    print("Not valid Input ")
