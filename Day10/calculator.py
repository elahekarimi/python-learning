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
def calculation():
    n1=float((input("enter first number:")))
    for symbol in operators:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("what operation do you want:")
        n2=float((input("enter next nmber:")))
        calculation_function=operators[operation_symbol]
        answer=calculation_function(n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input("enter y for continue:") == "y":
            n1=answer
        else:
            should_continue=False
            calculation()
calculation()

        