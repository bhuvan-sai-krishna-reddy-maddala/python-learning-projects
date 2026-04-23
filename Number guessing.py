import random

def get_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Please enter an integer")

def play_game():
    correct = random.randint(1, 100)
    chances = 10

    while chances > 0:
        guess = get_guess()

        if guess == correct:
            print("Hooray!")
            break
        elif guess > correct:
            print("Your guess is too high")
        else:
           print("Your guess is too low")

        chances -= 1
        print(f"Chances left: {chances}")


    else:
        print("Game Over")


while True:
    play_game()
    again = input("Play again? yes/no: ")
    if again.lower() =="yes":
        continue
    elif again.lower() =="no":
        break
    else:
        print("Game Over")