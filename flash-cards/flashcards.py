import json
import random
import os


# Gets the contents of the flashcard file
def get_flashcard_file(file_path):
    with open(file_path, "r") as file:
        file_json = json.load(file)
        return file_json


# Gets all the possible flashcards from the given directory
def get_flashcards(directory):
    files = os.listdir(directory)
    flashcard_files = [fc for fc in files if fc.endswith(".json") and fc.startswith("me-")]
    return flashcard_files


# Lets the user select a set of flashcards to study
def select_flashcards(flashcards):
    # Exit if no flashcards exist
    if len(flashcards) == 0:
        print("No flashcards were found!")
        exit()

    # Ask the user for the file name
    while True:
        print("Which flashcards would you like to study?")
        selected_fc = input(f"Options include: {' '.join(flashcards)}\n")
        if selected_fc in flashcards:
            print(f"\nYou are now studying {selected_fc}\n")
            return get_flashcard_file(selected_fc)
        else:
            print("\nInvalid flashcard file! Please try again.\n")


# Asks for the answer to the flashcard
def ask_question(question, answer):
    guess = input(f"{question} ")

    if guess.lower() == answer.lower():
        return True
    return False


flashcard_options = get_flashcards("./")
flashcard_json = select_flashcards(flashcard_options)
cards = flashcard_json["cards"]

# Shuffle the cards
random.shuffle(cards)

total = len(cards)
score = 0
attempts = 0

# Keep asking for the flashcards until the user gets all of them correct at least once
while score != total:
    for card in cards:
        attempts += 1

        question = card['q']
        answer = card['a']

        guessed_right = ask_question(question, answer)
        if guessed_right:
            score += 1
            print(f"Correct! Your score is now {score}/{total}\n")
            cards.remove(card)
        else:
            print(f"Incorrect! The correct answer was {answer}\n")

# End message
print(f"It took you {attempts} attempts to complete the flashcards.")

# Send a message based on the user's attempts
if attempts == total:
    print("Flawless!")
elif attempts >= round(total * 1.5):
    print("You need more practice!")
else:
    print("Good job!")
