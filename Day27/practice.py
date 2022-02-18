def add(*number):
    n = 0
    for num in number:
        n += num
    return n


print(add(1, 3, 4, 5, 6))
