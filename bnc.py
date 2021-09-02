from random import randint

roles = ["Bear", "Ninja", "Cowboy"]

computer = roles[randint(0, 2)].lower()


# Ask the player if they want instructions to the game
def instructions():
    wants_instructions = input("Would you like the instructions? (yes/no) > ").lower()
    if wants_instructions == "yes":
        print(
            "\nBear, Ninja, Cowboy is an exciting game of strategy and skill! Pit your wit against the computer! Choose"
            " a player: Bear, Ninja, or Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy "
            "and cowboy shoots bear.")


# Get the players input for their role
def get_player_action():
    player_input = input("Bear, Ninja, or Cowboy? > ")
    player = player_input.lower().capitalize()
    if player not in roles:
        print("\nInvalid role! Please try again\n")
        return get_player_action()
    return player


# Randomly pick a role for the computer
def get_computer_action():
    computer = roles[randint(0, 2)]
    return computer


# Compare the player's role to the computer's role
def compare_roles(player_role, computer_role):
    if computer_role == player_role:
        print("DRAW!")
        return False
    elif computer_role == "Cowboy":
        if player_role == "Bear":
            print("You lose!", computer_role, "shoots", player_role)
            return False
        else:
            print("You win!", player_role, "defeats", computer_role)
            return True
    elif computer_role == "Bear":
        if player_role == "Cowboy":
            print("You win!", player_role, "shoots", computer_role)
            return True
        else:
            print("You lose!", computer_role, "eats", player_role)
            return False
    elif computer_role == "Ninja":
        if player_role == "Cowboy":
            print("You lose!", computer_role, "defeats", player_role)
            return False
        else:
            print("You win!", player_role, "eats", computer_role)
            return True


# Ask the player if they wish to play again
def play_again():
    answer = input("\nWould you like to play again? (yes/no) > ").lower()
    if answer == 'yes':
        return True
    else:
        return False


wins = 0
total_plays = 0

instructions()
print("\nGet ready to play Bear, Ninja, Cowboy!\n")

# Game loop
while True:
    total_plays += 1

    player = get_player_action()
    computer = get_computer_action()

    has_won = compare_roles(player, computer)

    if has_won:
        wins += 1

    wants_new_game = play_again()
    if wants_new_game:
        continue
    else:
        print(f"You won {wins} out of {total_plays} games!")
        break
