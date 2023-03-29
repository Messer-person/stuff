# # Create a program that asks the user to enter their name and their age. Print out a
# # message addressed to them that tells them the year that they will turn 100 years old.
# # Note: for this exercise, the expectation is that you explicitly write out the year
# import datetime
#
#
# def old_timer(identification):
#     now = datetime.datetime.now()
#     identification = identification.split(" ")
#     current_year = now.year
#     return f'''Look {identification[0]}, I'm gonna be honest here, you will not live that long, but...
# if you were to live up to a 100 yo, you'd reach that age in year {(100 - int(identification[1]) + current_year)}.'''
#
#
# personal_data = input('please enter your name, and age (no coma): ')
# print(old_timer(personal_data))

# ---------------------------------------------------------------------------------------------

# # Ask the user for a number. Depending on whether the number is even or odd,
# # print out an appropriate message to the user. Hint: how does an even / odd number react
# # differently when divided by 2?
#
#
# def odd_number_recognizer(num: int):
#     if num % 4 == 0:
#         return "even and multiplication of 4"
#     elif num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
#
#
# number = int(input("Please enter any number: "))
# print(odd_number_recognizer(number))
#
#
# # Extras:
# #
# # If the number is a multiple of 4, print out a different message.
# # Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# # If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#
#
# def two_number_modulus(numbs: int, check: int) -> str:
#     if numbs % check == 0:
#         return "first numer is a multiplication of the second one"
#     else:
#         return "those are 2 unrelated numbers"
#
#
# numbers = input("give me 2 random numbers(number number)(no coma): ")
# list_of_numbers = numbers.split(" ")
# print(two_number_modulus(int(list_of_numbers[0]), int(list_of_numbers[1])))

# --------------------------------------------------------------------------------------------------------------------

# # Take a list, say for example this one:
# #
# #   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # and write a program that prints out all the elements of the list that are less than 5.
# #
# # Extras:
# #
# # Instead of printing the elements one by one, make a new list that has all the elements less
# # than 5 from this list in it and print out this new list.
# # Write this in one line of Python.
# # Ask the user for a number and return a list that contains only elements from the
# # original list a that are smaller than that number given by the user.
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # [expression for item in items] - list comprehension
#
# print([item for item in a if item < 5])
# choice = int(input("enter a random number: "))
# print([number for number in a if number < choice])

# --------------------------------------------------------------------------------------------------------------------

array = [1, 2, 45, 7, 2, 8, 2, 7, 9, 34, 54, 254, 2, 67, 2, 6, 7, 24]
#
# def bubble_sorting(listx):
#     n = len(listx)
#     modded = True
#     while modded:
#         modded = False
#         x = 1
#         for number in range(n - 1):
#             if listx[number] > listx[x]:
#                 listx[number], listx[x] = listx[x], listx[number]
#                 modded = True
#             x += 1
#         n -= 1
#
#
# bubble_sorting(array)
# print(array)

# --------------------------------------------------------------------------------------------------------------------

# # Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# # (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# # For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
#
# players_choice = int(input("enter any number: "))
# # for number in range(players_choice):
# #     if players_choice % number == 0
#
# print(f'Divisors for this number: {[number for number in range(1, players_choice) if players_choice % number == 0]}')

# ---------------------------------------------------------------------------------------------------------------------

# # Take two lists, say for example these two:
# #
# #   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# #   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # and write a program that returns a list that contains only the elements that are common between the lists
# # (without duplicates). Make sure your program works on two lists of different sizes.
# #
# # Extras:
# #
# # Randomly generate two lists to test this
# # Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(*set([numb for numb in a if numb in b]))

# ---------------------------------------------------------------------------------------------------------------------

# # Ask the user for a string and print out whether this string is a palindrome or not.
# # (A palindrome is a string that reads the same forwards and backwards.)
# def palindrome_figure_outer(word_arg):
#     if word_arg[::-1] == word_arg:
#         return f'{word_arg} is a palindrome.'
#     else:
#         return f'{word_arg} is not a palindrome.'
#
#
# word = input("give me a word: ")
# print(palindrome_figure_outer(word))

# ---------------------------------------------------------------------------------------------------------------------

# # Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of
# # Python that takes this list a and makes a new list that has only the even elements of this list in it.
#
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([item for item in a if item % 2 == 0])

# ---------------------------------------------------------------------------------------------------------------------

# # Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# # whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the
# # very first exercise)
# #
# # Extras:
# #
# # Keep the game going until the user types “exit”
# # Keep track of how many guesses the user has taken, and when the game ends, print this out.
#
# import random
# import time
#
#
# def play_guesser():
#     print('guess the number Im thinking about. type "quit" to exit the game')
#     tries = 0
#     number = random.randrange(1, 10)
#     while True:
#         players_guess = (input("your guess: "))
#
#         # establish input, msg output, keeping count of tries:
#
#         try:
#             if int(players_guess) in range(1, 10):
#                 if number == int(players_guess):
#                     msg = "Correct!"
#                 elif int(players_guess) > number:
#                     msg = "Wrong, too high."
#                 else:
#                     msg = "wrong, too low."
#                 tries += 1
#             else:
#                 msg = "error"
#         except ValueError:
#             if players_guess.upper().strip() == "QUIT" or (players_guess.upper()).strip() == "Q":
#                 print("Thank you for playing.")
#                 time.sleep(1)
#                 break
#             else:
#                 msg = "error"
#
#         # delivering the output:
#
#         if msg == "Correct!":
#
#             # Clear variables, and establish new ones:
#
#             print(f'{msg} It took you {tries} tries.')
#             number = random.randrange(1, 10)
#             tries = 0
#             print("lets play again!")
#         elif msg == "error":
#             print("input one number between 1 - 9, or a command to quit.")
#         else:
#             print(msg)
#
#
# play_guesser()

# --------------------------------------------------------------------------------------------------------------------
# # string_reversing_tool
#
# def uno_tool(string):
#     return "".join([sign for sign in string[::-1]])
#
#
# # random_stuff = input("say a word: ")
# # print(uno_tool(random_stuff))

# ---------------------------------------------------------------------------------------------------------------------
#
# # try thing experimentation
#
# # x = "T"
# # if int(x) in range(1, 10):
# #     print(x)
#
# # ValueError
# def uno_tool(string):
#     return "".join([sign for sign in string[::-1]])
#
#
# def practicing_trying():
#     while True:
#         x = input("Say some shit or a number:")
#         try:
#             if int(x) % 3 == 0 and int(x) % 2 == 0:
#                 msg = "it's a number, and multiplication of 3, AND 2!"
#             elif int(x) % 2 == 0:
#                 msg = "it's a number, and multiplication of 2"
#             else:
#                 if int(x) <= 10:
#                     msg = "it's a number, and not very high one at that"
#                 else:
#                     msg = "it's a number, don't know what else to tell you about it"
#         except ValueError:
#             if uno_tool(x) == x:
#                 msg = "ah, that word is a palindrome!"
#             elif x.upper() == "QUIT":
#                 msg = "ok,bye"
#             else:
#                 msg = "eeeh it's a string..."
#         # executing commands
#
#         print(msg)
#         if msg == "ok,bye":
#             break
#
#
# # print([item for item in "hababla"])
# # x = "top"
# # y = [sign for sign in x[::-1]]
# # rf = 4
# #
# # z = "top"
# # print(y)
# # print([sign for sign in x])
# # print([sign for sign in x] == [sign for sign in x[::-1]])
# practicing_trying()

# ---------------------------------------------------------------------------------------------------------------------

# # Dictionary comprehension
#
# # x = "badamdabamdabam"
# # # y = [item for item in x]
# # # y = [*x]
# # z = {item: [*x].count(item) for item in [*x]}
# # a = []
# # # print(item[0] for group in z if item[1] > 6)
# # print(z)
# #
# #
# # def sort_dict(item):
# #     return item[1]
# #
# #
# # def sorting_by_appearance_frequency(idk):
# #     idk.sort(idk[1])
# #
# #
# # # print(z.sort(key=sorting_by_appearance_frequency))
# #
# # # for sign, amount in item:
# # #     x=1
# # #     a.append(item)
# # #     if item[1] >
# # #
# #
# # print(a)
# # b = [*z]
# # print(*b)
# #
# # # "*" ->it's an unpacking operator
# #
# # # for item in z:
# # #     n = len(z)
# # #     a.append(item)
# # #     x = 1
# # #     if
# #
# #
# # def dict_sign_amount(string):
# #     # exp for item in items
# #     return {item: [*string].count(item) for item in [*string]}
# #
# #
# # dic = dict_sign_amount(x)
# # print(f"dic = {dic}")
# # dic_signs = [*dic]
# # print(dic_signs)
# #
# #
# # def analizer(dictionary):
# #     keys_list = [*dictionary]
# #     values_list = [dictionary[key] for key in keys_list]
# #     # for key in keys_list:
# #     #     values_list.append(dictionary[key])
# #     dict_to_list = list(zip(keys_list, values_list))
# #     # lamda expression -> argument(s): expression
# #     dict_to_list.sort(key=lambda item: item[1])
# #     answer = dict_to_list[-1]
# #     return f"""In that sentence the most common sign is "{answer[0]}", it appeared {answer[1]} times"""
#
#
# # def string_counter(string):
# #     dictionary = {sign: [*string].count(sign) for sign in [*string]}
# #     keys_list = [*dictionary]
# #     values_list = [dictionary[key] for key in keys_list]
# #     dict_to_list = list(zip(keys_list, values_list))
# #     # dict_to_list = dictionary.items()
# #     dict_to_list.sort(key=lambda item: item[1])
# #     answer = dict_to_list[-1]
# #     return f"""In that sentence the most common sign is "{answer[0]}", it appeared {answer[1]} times"""
#
#
# x = "badamdabamdabam"
# # print(string_counter(x))
#
# # z = {item: [*x].count(item) for item in [*x]}
# # list_thing = z.items()
# # print(list_thing)
# # pffft = sorted(list_thing, key=lambda item: item[1])
# # print(pffft)
# # print(pffft[-1])
#
#
# # def string_counter(string):
# #     dictionary = {sign: [*string].count(sign) for sign in [*string]}
# #     # keys_list = [*dictionary]
# #     # values_list = [dictionary[key] for key in keys_list]
# #     # dict_to_list = list(zip(keys_list, values_list))
# #     # # dict_to_list = dictionary.items()
# #     # dict_to_list.sort(key=lambda item: item[1])
# #     dict_to_list = sorted(dictionary.items(), key=lambda item: item[1])
# #     answer = dict_to_list[-1]
# #     return f"""In that sentence the most common sign is "{answer[0]}", it appeared {answer[1]} times"""
#
#
# def sign_counter(string):
#     dictionary = {sign: [*string].count(sign) for sign in [*string]}
#     dict_to_list = sorted(dictionary.items(), key=lambda item: item[1])
#     answer = dict_to_list[-1]
#     return f"""In that sentence the most common sign is "{answer[0]}", it appeared {answer[1]} times"""
#
#
# def letter_counter(string):
#     dictionary = {sign: [*string].count(sign) for sign in [*string]}
#     dict_to_list = sorted(dictionary.items(), key=lambda item: item[1])
#     undesirable = [" ", "'", ",", ".", "!", "?", "/", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#     cleared = [item for item in dict_to_list if item[0] not in undesirable]
#     answer = cleared[-1]
#     return f"""In that sentence the most common letter is "{answer[0]}", it appeared {answer[1]} times"""
#
#
# print(sign_counter(x))
#
# sentence = "this is one of the most common interview questions, but I hope not for an intern, or a junior position..."
#
# print(sign_counter(sentence))
# print(letter_counter(sentence))
#
#
# # change introduced by Pawel
# # def character_counter(string):
# #     counted_chars = {char: string.count(char) for char in string}
# #     result = max(counted_chars.items(), key=lambda item: item[1])
# #     return f"""In that sentence the most common sign is "{result[0]}", it appeared {result[1]} times"""
#
#
# def character_counter(string):
#     undesirable = "1234567890 -=!@#$%^&*()_+/.,?><';:][}{}"
#     counted_chars = {char: string.count(char) for char in string if char not in undesirable}
#     result = max(counted_chars.items(), key=lambda char: char[1])
#     return f"""In that sentence the most common sign is "{result[0]}", it appeared {result[1]} times"""
#
#
# print(character_counter(x))
# print(character_counter(sentence))

# ---------------------------------------------------------------------------------------------------------------------
#
#
# def permuting_array(array):
#     n = len(array)
#     working = True
#     for number in array:
#         if number not in range(1, n+1):
#             array.remove(number)
#     while working:
#         working = False
#         for number in range(1, n+1):
#             if number in array:
#                 if array.count(number) > 1:
#                     array.remove(number)
#                     working = True
#                 else:
#                     pass
#             else:
#                 array.append(number)
#                 working = True
#
#
# ar = [2, 2, 9]
# permuting_array(ar)
# print(ar)

# ---------------------------------------------------------------------------------------------------------------------

