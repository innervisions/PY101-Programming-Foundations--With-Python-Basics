import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

BEATS = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
}

LOSES_TO = {
    "rock": ["paper", "spock"],
    "paper": ["scissors", "lizard"],
    "scissors": ["rock", "spock"],
    "lizard": ["rock", "scissors"],
    "spock": ["paper", "lizard"],
}


def prompt(message):
    print(f"==> {message}")


def process_choice(player_choice: str) -> str:
    player_choice = player_choice.lower()
    if player_choice.startswith("r"):
        return "rock"
    if player_choice.startswith("p"):
        return "paper"
    if player_choice.startswith("sc"):
        return "scissors"
    if player_choice.startswith("l"):
        return "lizard"
    if player_choice.startswith("sp"):
        return "spock"
    
    return ""


def determine_winner(player: str, computer: str) -> str:
    if computer in BEATS[player]:
        return "player"
    if computer in LOSES_TO[player]:
        return "computer"

    return "tie"


def display_winner(player: str, computer: str):
    prompt(f"You chose {player}. Computer chose {computer}.")
    winner = determine_winner(player, computer)

    if winner == "player":
        prompt("You win!\n")
    elif winner == "computer":
        prompt("Computer wins.\n")
    else:
        prompt("It's a tie.\n")


def display_header(player_score: int, computer_score: int):
    print("-" * 55)
    print(
        f"|        Player: {player_score}        |"
        + f"        Computer: {computer_score}        |"
    )
    print("-" * 55)


def display_match_winner(scores: dict):
    print("*" * 55)
    print(f"You won {scores["player"]}.")
    print(f"Computer won {scores["computer"]}.\n")

    if scores["player"] >= scores["computer"]:
        print("You win the match!")
    else:
        print("Computer wins the match.")

    print("*" * 55)


def play_game() -> str:
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    player_choice = process_choice(input())

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = process_choice(input())

    computer_choice = random.choice(VALID_CHOICES)
    display_winner(player_choice, computer_choice)
    return determine_winner(player_choice, computer_choice)


def play_match():
    scores = {"player": 0, "computer": 0}
    while all(score < 5 for score in scores.values()):
        display_header(scores["player"], scores["computer"])
        winner = play_game()
        if winner in scores:
            scores[winner] += 1

    display_match_winner(scores)


### Main Loop
while True:
    play_match()
    prompt("Would you like to play another match? (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith("n") or answer.startswith("y"):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == "n":
        break
