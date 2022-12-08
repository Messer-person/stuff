import random


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


# Checks for a correct numbers in correct place in a sequence. and stuff.
def cows(correct_pin, guess_para):
    cows = 0
    x = 0
    for numb in guess_para:
        if correct_pin[x] == guess_para[x]:
            cows += 1
            x += 1
        else:
            x += 1
    return cows


#Checks for a correct numbers in a incorrect place in a sequence.
def bulls(correct_pin, guess_para, cow_para):
    guess_shattered = string_cutter(guess_para)
    pin_shattered = string_cutter(correct_pin)
    bull = 0
    for number in guess_shattered:
        if number in pin_shattered:
            bull += 1
            pin_shattered.remove(number)
    return bull - cow_para


pin = generator()

print("""
welcome to cows, and bulls game. 
You'll need to guess a 4 digit number.
for every number guessed correctly in the right place in the sequence it's a cow
for every number guessed correctly in the wrong place it's a bull.
good luck!""")

# Game loop.
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
        print("Thank you for plaing, bye.")
        break
    else:
        cow = cows(pin, guess)
        bull = bulls(pin, guess, cow)
        print(f"cows: {cow}, bulls: {bull}")
        pass
