
def double_it():
    user_input =int(input("Enter your number"))
    while user_input <= 100:
        user_input = 2 * user_input
        print(user_input,end=" ")
    
double_it()