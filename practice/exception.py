def main():
    x = get_int()
    print(f"you typed in {x}")

def get_int():    
    while True:
        try:
            x = int(input("type in an integer "))
            break
        except ValueError:
            print("you didn't type in an integer idiot")    
    return x

main()