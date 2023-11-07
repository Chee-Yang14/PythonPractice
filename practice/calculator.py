def plus(x,y): 
    z = x+y
    print(str(x)+" plus "+str(y)+" equals "+ str(z))

def multiply(x,y):
    z = x*y
    print(str(x)+" multiply "+str(y)+" equals "+ str(z))
    
def divide(x,y):
    z = x/y
    print(str(x)+" divide "+str(y)+" equals "+str(z))    

x = int(input("what is x"))
y = int(input("what is y"))


plus(x,y)
divide(x,y)
multiply(x,y)
