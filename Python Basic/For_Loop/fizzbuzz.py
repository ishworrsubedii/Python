def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        print("Fizz_Buzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    else:
        print(input)
fizz_buzz(15)
