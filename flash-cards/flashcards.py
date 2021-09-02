import json
import random


def get_flashcard_file(file_path):
    with open(file_path, "r") as file:
        file_json = json.load(file)
        return file_json


file_json = get_flashcard_file("me-capitals.json")
cards = file_json["cards"]
random.shuffle(cards)

total = len(cards)
score = 0
attempts = 0

while score != total:
    for card in cards:
        guess = input(f"{card['q']} ")

        attempts += 1

        if guess.lower() == card["a"].lower():
            score += 1
            cards.remove(card)
            print(f"Correct! Your score is now {score}/{total}\n")
        else:
            print(f"Incorrect! The correct answer was {card['a']}\n")
print("You've completed the flashcards!")

