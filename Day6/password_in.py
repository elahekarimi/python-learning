import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1','2','3','4','5','6','8','9']
symbol=['!','$', '#', '%', '^', '&', '*', '(' ,')']
password=''
for l in random.choice(letters):
    password+=l
    for l in random.choice(letters):
        password+=l 
        for l in random.choice(letters):
         password+=l
         for l in random.choice(letters):
          password+=l
for n in random.choice(numbers):
    password+=n
    for n in random.choice(numbers):
     password+=n
     for n in random.choice(numbers):
      password+=n
      for n in random.choice(numbers):
       password+=n
for s in random.choice(symbol):
    password+=s
    for n in random.choice(symbol):
     password+=n
     for n in random.choice(symbol):
      password+=n
      for n in random.choice(symbol):
       password+=n
print(password)




