from ast import operator
import re


#add
def add (n1, n2):
    return n1+n2
#subtract
def sub (n1, n2):
    return n1-n2
#multiple
def mul (n1, n2):
    return n1*n2
#divide
def div (n1, n2):
    return n1/n2
print(add(2,3))
operators={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
n1=int((input("enter first number:")))
n2=int((input("enter second nmber:")))
for symbol in operators:
    print(symbol)
operation_symbol=input("what operation do you want:")
calculation_function=operators[operation_symbol]
answer=calculation_function(n1,n2)
n3=int(input("enter the theird number:"))
operation_symbol=input("what operation do you want:")
second_answer=calculation_function(answer, n3)
print(f"{answer} {operation_symbol} {n3} = {second_answer}")

        