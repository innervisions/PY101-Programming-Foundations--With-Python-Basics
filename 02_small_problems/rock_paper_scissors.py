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


def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if computer in BEATS[player]:
        prompt("You win!")
    elif computer in LOSES_TO[player]:
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")


def play_rps():
    while True:
        prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
        choice = process_choice(input())

        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            choice = process_choice(input())

        computer_choice = random.choice(VALID_CHOICES)
        display_winner(choice, computer_choice)

        prompt("Do you want to play again (y/n)?")
        answer = input().lower()
        while True:
            if answer.startswith("n") or answer.startswith("y"):
                break

            prompt('Please enter "y" or "n".')
            answer = input().lower()

        if answer[0] == "n":
            break


play_rps()
