def name (first, last):
    if first == "" or last =="":
        return "there is not valid input"
    a=first.title()
    b=last.title()
    return f"{a}{b}"
print(name(input("input your first name:"),input("input your last name:")))

