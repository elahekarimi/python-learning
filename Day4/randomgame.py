import random
name= input('insert the names:')
name_sv=name.split(", ")
print(name_sv)
lens=len(name_sv)
randomnum=random.randint(0, lens-1)
who_will_pay=name_sv[randomnum]
print(who_will_pay)


