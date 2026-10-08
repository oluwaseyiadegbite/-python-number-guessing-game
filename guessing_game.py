import random


def player_guesses(low, high):
    """Player tries to guess the computer's secret number."""
    secret = random.randint(low, high)
    guesses = 0
    while True:
        try:
            guess = int(input(f"Guess a number ({low}-{high}): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        guesses += 1
        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct! You took {guesses} guesses.")
            return


def computer_guesses(low, high):
    """Computer guesses your number using binary search."""
    guesses = 0
    while low <= high:
        mid = (low + high) // 2
        answer = input(f"Is it {mid}? (h=too high, l=too low, c=correct): ").lower()
        if answer == "c":
            print(f"Found it in {guesses + 1} guesses!")
            return
        elif answer == "h":
            high = mid - 1
        elif answer == "l":
            low = mid + 1
        else:
            print("Please type h, l or c.")
            continue
        guesses += 1
    print("That doesn't add up. Did you change your number?")


def main():
    choice = input("1 = You guess, 2 = Computer guesses: ")
    if choice == "1":
        player_guesses(1, 100)
    elif choice == "2":
        computer_guesses(1, 100)
    else:
        print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()
