fruit = ["apple", "orange", "pear"]
def my_pie(index):
    try:
        fruits = fruit[index]
    except IndexError:
        print("pie")
    else:
        print(fruits + "pie")
my_pie(4)
