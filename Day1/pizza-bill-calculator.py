#pizza bill calculator
size = input("what is the size:")
pepperoni= input('what do you whant the peperoni:')
cheese= input('what do you whant extra chees:')
bill = 0
if size == 'small':
   bill = 15
   if pepperoni == 'y':
       bill += 2
if size == 'medium':
   bill = 20
   if pepperoni == 'y':
         bill +=3
if size == 'large':
   bill = 25
   if pepperoni == 'y':
         bill +=3
   if cheese == 'y':
     bill += 1
print (f"the prise is ${bill}")

