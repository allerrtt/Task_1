def parsing():
    us_input=input("Enter your expression ")
    us_input = us_input.replace(" ","")
    if "+" in us_input:
        a,b=us_input.split("+")
        action="+"
    elif "-" in us_input:
        a,b=us_input.split("-")
        action="-"
    elif "*" in us_input:
        a,b=us_input.split("*")
        action="*"
    elif "/" in us_input:
        a,b=us_input.split("/")
        action="/"
    else:
       print("Error: Invalid input format")
       return None,None,None
    try:
        a=float(a)
        b=float(b)
    except:
        print("Error: Invalid numbers")
        return None, None, None
    return a,action,b
def calculate(a,action,b):
    if action=="+":
        return a+b
    elif action=="-":
        return a-b
    elif action=="*":
        return a*b
    elif action=="/":
        if b==0:
            return "Error: Division by zero"
        return a / b
answer="y"
while answer=="y":
    a,action,b = parsing()
    if a is None:
        continue  # неправильний ввід, повтор
    result=calculate(a,action,b)
    print(result)
    answer=input("Continue?(y/n)").lower().replace(" ","")
print("zlagger")