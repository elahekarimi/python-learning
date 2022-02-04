
#pizza bill calculator

print("for first question only use small large or medium")
 
size = input("what is the size:")

print("for other questionz only use y for yes or n for no")

pepperoni= input("do you want  peperoni:")
print("You can only buy cheese if you order large pizza") 
cheese= input("do you want  extra chees:")
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

