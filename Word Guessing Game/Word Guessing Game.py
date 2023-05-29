import sys
import random
import time
import re

choice = None
while choice != "0":
    print(
    """
    Hi traveler!
    This is a simple word guessing game, you have 5 tries.
    Enjoy!
    Choose a number:
    0 - exit
    1 - play a single game
    """
    )
    choice = input("You choose: ")
    print()
    # wyjdź
    if choice == "0":
        print("Bye!")
    elif choice == "1":

        no_of_tries = 5
        word_list = ["python", "index", "numbers"] #you can add your words
        word = random.choice(word_list)
        used_letters = set()
        user_word = []


        def find_indexes(word, letter):
            indexes = []
            for index, letter_in_word in enumerate(word):
                if letter == letter_in_word:
                    indexes.append(index)
            return indexes


        def show_state_of_game():
            print()
            print(user_word)
            print("Trials left: ", no_of_tries)
            print("Used letter:", used_letters)
            print()

        def used_correct_word(letter):
            if re.search(r'aa', letter):
                print("You cannot enter more than one letter")
                return True
            elif re.search(r'\d', letter):
                print("Numbers cannot be entered")
                return True
            elif re.search(r'[A-Z]', letter):
                print("Capital letters cannot be entered")
                return True
            else:
                return False

        for _ in word:
            user_word.append("_")

        while True:
            letter = input("Enter a letter: ")
            if letter in used_letters:
                print("This letter has already been used. Try typing a different letter.")
                continue

            used_letters.add(letter)

            if not used_correct_word(letter):
                found_index = find_indexes(word, letter)

                if len(found_index) == 0:
                    print("Trials left: ", no_of_tries)
                    no_of_tries -= 1
                    if no_of_tries == 0:
                        print("Game over!")
                        print("Program will close in 5 seconds...")
                        time.sleep(5)
                        sys.exit(0)
                else:
                    for index in found_index:
                        user_word[index] = letter

                    if "".join(user_word) == word:
                        print("Bravo that's the word!")
                        print("Program will close in 5 seconds...")
                        time.sleep(5)
                        sys.exit(0)
            show_state_of_game()
