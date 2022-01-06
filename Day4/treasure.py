row1=['0', '0', '0']
row2=['0', '0', '0']
row3=['0', '0', '0']
map= [row1, row2, row3]
print(map)
#print(f"{row1}\n{row2}\n{row3}")
number=input("enter a number according to row and column:")
vertical=int(number[0])
horizontal=int(number[1])
vertical_map=map[vertical-1]
vertical_map[horizontal-1]="x"
print(f"{row1}\n{row2}\n{row3}")

