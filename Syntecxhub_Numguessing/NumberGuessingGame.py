import random

def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def play_game(best_score):
    max_number = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_number}.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

    if best_score is None or attempts < best_score:
        best_score = attempts
        print("🏆 New best score!")

    return best_score


def main():
    print("===== Number Guessing Game =====")
    best_score = None

    while True:
        best_score = play_game(best_score)

        print(f"Best (Lowest) Attempts So Far: {best_score}")

        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("\nThanks for playing! Goodbye 👋")
            break


if __name__ == "__main__":
    main()