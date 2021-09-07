import random
print("The Guessing Game!")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")
while chances <= 5:
    userInput = int(input("Enter the guess"))
    if userInput == number:
        print("Congrats! You have won.")
        break
    elif userInput < number:
        print("Your number was lower than ", userInput)
        
    else:
        print("your number is higher than", userInput)
    
    chances = chances +1
if not chances <= 5:
    print("you lose! the number is", number)



