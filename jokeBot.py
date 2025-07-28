PROMPT:str="what do you want?"
JOKE:str="Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"

def joke_bot():
    user_input = input(PROMPT)

    if user_input == "joke":
        print(JOKE)
    else:
        print("sorry,i only tell joke")    
joke_bot()        