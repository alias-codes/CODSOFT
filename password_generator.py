import random
import string

l=int(input("Enter the length of your password: "))
def generate(l):
    password=[]
    level=input("Difficulties:- \ne for Easy\nm for Medium\nh for Hard\nEnter difficulty: ").lower()
    if level=='e':
        chars=string.ascii_letters
    elif level=='m':
        chars=string.ascii_letters+string.digits
    elif level=='h':
        chars=string.ascii_letters+string.digits+string.punctuation
    else:
        print("Invalid input!")
        return
    
    for i in range(l):
        char=random.choice(chars)
        password.append(char)

    p=''.join(password)
    print("Your password :",p)

generate(l)