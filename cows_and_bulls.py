import random
import time


# Generates a 4 digit number
def generator():
    output = ""
    for _ in range(4):
        output += str(random.choice(range(10)))
    return output


# Cuts up a string into a list of strings components.
def string_cutter(string_para):
    output2 = []
    for num in string_para:
        output2.append(num)
    return output2


# Checks for a correct numbers in correct place in a sequence.
def cows(correct_pin, guess_para):
    cows_count = 0
    x = 0
    for _ in guess_para:
        if correct_pin[x] == guess_para[x]:
            cows_count += 1
            x += 1
        else:
            x += 1
    return cows_count


# Checks for a correct numbers in an incorrect place in a sequence.
def bulls(correct_pin, guess_para, cow_para):
    guess_shattered = string_cutter(guess_para)
    pin_shattered = string_cutter(correct_pin)
    bulls_count = 0
    for number in guess_shattered:
        if number in pin_shattered:
            bulls_count += 1
            pin_shattered.remove(number)
    return bulls_count - cow_para


pin = generator()

print("""
welcome to cows, and bulls game. 
You'll need to guess a 4 digit number.
for every number guessed correctly in the right place in the sequence it's a cow
for every number guessed correctly in the wrong place it's a bull.
good luck!""")


# Game loop.
def play():
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
            cow = cows(pin, guess)
            bull = bulls(pin, guess, cow)
            print(f"cows: {cow}, bulls: {bull}")
            pass


play()

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
        pass
