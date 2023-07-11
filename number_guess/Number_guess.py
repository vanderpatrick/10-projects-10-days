from random import randint


def main():
    print("Welcome to the number guesser")
    while True:
        user_input = input("guess a number between 1 and 10: ")
        computer_guess = randint(1, 2)
        try:
            option = int(user_input)
        except ValueError:
            print("Input is not a number please choose a number between 1 and 10")
            continue
        if option == computer_guess:
            print(f"Hey you won: your guess was {option}, and the computer was {computer_guess}")
            if str(input("do you want to restart ? press R or any other to quit")).lower() != "r":
                print("Bye bye")
                break

        else:
            print(f"Yikes you got it wrong your guess was {option}, and computer was {computer_guess}")
            continue


if __name__ == "__main__":
    main()
