for number in range(1,101):
    if number % 3 == 0:
        print("fizz")
    if number % 5 == 0:
        print("buzz")
    if number % 5 and number % 3 == 0:
        print("fizzbuzz")
else:
    print(number)
