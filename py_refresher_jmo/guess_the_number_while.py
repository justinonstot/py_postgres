# magic number app

from random import randrange

number = 7
user_prompt = "Would you like to play? (Y/n) "
user_replay_prompt = "Would you like to play again? (Y/n) "

while True: 
    user_input = (input(user_prompt))

    if user_input == "n":
        print("Okay, see ya!")
        break

    user_number = int(input("Guess our number: "))
    
    if user_number == number:
        print(f"You guessed correctly! {number} is the correct number!")
        number = randrange(11)
    elif user_number in (number-1, number+1):
        print("You are very close. Off by one!")
    else:
        print(f"Sorry, {user_number} is incorrect")


