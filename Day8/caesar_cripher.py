number=input('enter a number:')
number=int(number)
def prime (number):
    is_prime=True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime=False
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")
prime(number) 


