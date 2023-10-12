import random

word_list = ["Strawberries", "Apple", "Banana", "Orange", "Mango"]

word = random.choice(word_list)
print(word)

guess = input("Choose one letter")
if len(guess) == 1:
    print("Good guess!")
else: print("Oops! That is not a valid input.")



