name1=input('what is your name1:')
name2=input('what is your name2:')
names=name1+name2
names_lowercase=names.lower()
t=names_lowercase.count('t')
r=names_lowercase.count('r')
u=names_lowercase.count('u')
e=names_lowercase.count('e')
trues=t+r+u+e
l=names_lowercase.count('l')
o=names_lowercase.count('o')
v=names_lowercase.count('v')
e=names_lowercase.count('e')
love=l+o+v+e
sum_all=int(str(trues) + str(love))
if (sum_all < 10)  or (sum_all > 90):
    print(sum_all,"%",'you go together like coke and mentos')
elif ( sum_all >= 40) and (sum_all <= 50):
    print(sum_all,"%","you are alrigt together")
else:
    print(sum_all,'%')


