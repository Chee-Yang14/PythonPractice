def loop(l):
    for str in l:
        print(str)
        
def whileloop():
    c=0
    while(c<5):
        c= c+1
        print(c)

        
l = {"printing", "as many", "stuff", "as", "possible"}
loop(l)
whileloop()

for i in range(3):
    for j in range(3):
        print("*", end="")
    print()