import re

def main():
    ques = input("what is the question?")
    
    match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)', ques)

    if not match:
        print("Invalid input. Please enter an expression like '5 + 3'.")
    else:
        x = float(match.group(1))
        operation = match.group(2)
        y = float(match.group(3))
        if operation == "*":
            multiply(x,y)
        if operation == "+":
            plus(x,y)
        if operation == "-":
            minus(x,y)
        if operation == "divide":
            divide(x,y)
            
    
def minus(x,y): 
    z = x-y
    print(str(x)+" minus "+str(y)+" equals "+ str(z))

def plus(x,y): 
    z = x+y
    print(str(x)+" plus "+str(y)+" equals "+ str(z))

def multiply(x,y):
    z = x*y
    print(str(x)+" multiply "+str(y)+" equals "+ str(z))
    
def divide(x,y):
    z = x/y
    print(str(x)+" divide "+str(y)+" equals "+str(z))    

main()