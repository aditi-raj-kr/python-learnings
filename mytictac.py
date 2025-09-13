import random



def take1stPos():
    a = (int(input("Enter Your 1st Position:")))
    while True:
        
        if (a == (1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 6) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7)):
            print("you win")

    

def compChance(a):
    
    while True:
        b= random.randint(1,9)
        if b != a:
            print(b)
            break
        while True:
            if b == ((1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 6) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7)):
                print("you lose")
            

    
compChance(take1stPos())