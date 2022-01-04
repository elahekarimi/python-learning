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
sum_all=str(trues) + str(love)
print(sum_all,"%")

