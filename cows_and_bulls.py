import random
import time


# Generates a 4 digit number
def generator():
    return "".join(str(random.choice(range(10))) for _ in range(4))


def cows_and_bulls(correct_pin, guess_para):
    cows_count = 0
    bulls_count = 0
    x = 0
    for number in guess_para:
        if number in correct_pin:
            bulls_count += 1
        if correct_pin[x] == guess_para[x]:
            cows_count += 1
            x += 1
        else:
            x += 1
    bulls_count = bulls_count - cows_count
    return cows_count, bulls_count


# Game loop.
def play():
    print("""
    Welcome to cows, and bulls game. 
    You'll need to guess a 4 digit number.
    for every number guessed correctly in the right place in the sequence it's a cow
    for every number guessed correctly in the wrong place it's a bull.
    good luck!""")
    pin = generator()
    attempt = 0
    while True:
        guess = (input("give me a number: "))
        attempt += 1
        if pin == guess:
            print(f"""correct, the number was {pin}!
             It took you {attempt} tries! 
             Thanks for playing!""")
            break
        elif len(guess) != 4:
            print("Enter 4 digits.")
            pass
        elif guess.upper() == "QUIT":
            print("Thank you for playing, bye.")
            break
        else:
            cow, bull = cows_and_bulls(pin, guess)
            print(f"cows: {cow}, bulls: {bull}")
    while True:
        continuation = input("""Would you like to play again or quit the app? 
        Play again/ quit app "P"/"Q" :""")
        if continuation.upper() == "P":
            play()
        elif continuation.upper() == "Q":
            print("Thank you for playing")
            time.sleep(2)
            break
        else:
            print("Wrong command, please try again: ")


play()
