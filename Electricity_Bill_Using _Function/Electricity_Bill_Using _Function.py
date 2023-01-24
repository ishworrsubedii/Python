from datetime import date


def initial_display():
    print(f'''
            Sunway Electricity System
                Maitidevi,Kathmandu
            ________*__________*_______*
                                        Date:{date.today()}
    ''')


def input_information():
    owner_name = (input("Enter the owner name: "))
    owner_address = (input("Enter the owner address: "))
    electricity_unit = int(input("Enter the total unit consumed: "))

    return (owner_name, owner_address, electricity_unit)


def calculation_unit(electricity_unit):
    if electricity_unit <= 20:
        total_amount = electricity_unit * 4


    elif 20 < electricity_unit < 50:
        discount=(20*4)+((electricity_unit-20)*7.5)-(electricity_unit-20*7.5)
        total_amount=((20*4)+((electricity_unit-20)*7.5))-discount

    elif 50 < electricity_unit < 150:
        discount=((20*4)+(30*7.5)+((electricity_unit-50)*1/100))
        total_amount=20*4+30*7.5+1


    elif 150 < electricity_unit < 250:
        a = electricity_unit - 150
        total_amount = (a * 11.5 + 100 * 9 + 30 * 7.5 + 20 * 4)
        discount = a * 11.5 * 10 / 10


    else:
        print("Invalid input")

    return total_amount, discount


def output_display(owner_name, total_amount, discount):
    print(owner_name)
    print("Total amount to pay= ", total_amount)
    print(
        f'{owner_name} Customer of Sunway international Electricity billing system has to pay total amount {total_amount - discount} with discount price {discount}')


initial_display()
owner_name, owner_address, electricity_unit=input_information()
total_amount, discount=calculation_unit(electricity_unit)
output_display(owner_name, total_amount, discount)
