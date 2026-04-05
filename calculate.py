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