import json
import random


# Gets the flashcard file
def get_flashcard_file(file_path):
    with open(file_path, "r") as file:
        file_json = json.load(file)
        return file_json


# Asks for the answer to the flashcard
def ask_question(card):
    question = card['q']
    answer = card['a']

    guess = input(f"{question} ")

    if guess.lower() == answer.lower():
        print(f"Correct! Your score is now {score}/{total}\n")
        return True
    print(f"Incorrect! The correct answer was {answer}\n")
    return False


flashcard_json = get_flashcard_file("me-capitals.json")
cards = flashcard_json["cards"]

# Shuffle the cards
random.shuffle(cards)

total = len(cards)
score = 0
attempts = 0

while score != total:
    for card in cards:
        attempts += 1

        guessed_right = ask_question(card)
        if guessed_right:
            score += 1
            cards.remove(card)

# End message
print(f"It took you {attempts} attempts to complete the flashcards.")

# Send a message based on the user's attempts
if attempts == total:
    print("Flawless!")
elif attempts >= round(total * 1.5):
    print("You need more practice!")
else:
    print("Good job!")
