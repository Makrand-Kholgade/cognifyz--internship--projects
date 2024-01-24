# print("Guessing Game")
import random
lst = list(range(1, 101))
n = (random.choice(lst))
guesses= 1
print("Number of guesses - 9 only: ")
while (guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number>n:
        print("Too high \n")
    elif guess_number < n:
        print("Too Low \n")
    else:
        print("you have won the game\n")
        print(9 - guesses, "no. of guesses you took to finish.")
        break
    print(9-guesses, "no. of guesses left")
    guesses = guesses + 1

if(guesses>9):
    print("Game over")