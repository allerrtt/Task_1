from parsing import parsing
from calculate import calculate
answer="y"
while answer=="y":
    a,action,b = parsing()
    if a is None:
        continue  # неправильний ввід, повтор
    result=calculate(a,action,b)
    print(result)
    answer=input("Continue?(y/n)").lower().replace(" ","")
print("zlagger67")