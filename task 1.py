import random 
num = random.randint(1,10)
guess = None

while guess!= num:
    guess = int(input("guess a number: "))
    
    if guess == num:
        print("congratilations!!")
        break
    else:
        print("Invalid number....Please try again!!")
    
