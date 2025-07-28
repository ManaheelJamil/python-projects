import random
selected = random.randint(1,9)
print(selected)
allowed_attempt:int = 5
user_attempt=0
while True:
    print("attempts left", allowed_attempt - user_attempt)
    if (user_attempt == allowed_attempt):
        print("GAME OVER")
        break
                
    user_input = int(input("Enter your number"))
    user_attempt += 1
    
    if user_input == selected:
        print("Congrats! your correct number is", selected)  
    if user_input < selected:
        print("Your guess is too low")
    elif user_input > selected:
        print("Your guess is too high")
    elif user_input == selected:
        break 
    else:
        print("invalid  input")
        
         
  
