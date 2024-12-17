import random 

secret_number = random.randint(1, 10)
guess_count = 0
while True:
    guess = int(input("Guess a number (between 1 and 10): "))
    guess_count += 1
    
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
            break
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high.Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
# Display the number of guesses it took
    print(f"It took you {guess_count} guesses to find the secret number.")
    
    # Offer to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_again()
    else:
        print("Thanks for playing!")

# Start the game
play_again()
