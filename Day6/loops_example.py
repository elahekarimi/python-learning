student_hight=input('write the student hight:').split()
for n in range(0, len(student_hight)):
    student_hight[n]=int(student_hight[n])

sum_hight=0
for hight in student_hight:
  sum_hight+=hight


number_of_s=0
for number in student_hight:
    number_of_s+=1

avg=(sum_hight/number_of_s)
print(avg)