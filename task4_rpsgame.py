import random

CHOICES = ["rock", "paper", "scissors"]

BEATS = {
    "rock":     "scissors",
    "scissors": "paper",
    "paper":    "rock",
}

EMOJI = {
    "rock":     "🪨",
    "paper":    "📄",
    "scissors": "✂️",
}


def get_computer_choice():
    return random.choice(CHOICES)


def get_result(player, computer):
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "win"
    return "lose"


def print_round(player, computer, result):
    print(f"\n  you:      {EMOJI[player]}  {player}")
    print(f"  computer: {EMOJI[computer]}  {computer}")
    print()

    if result == "tie":
        print("  it's a tie!")
    elif result == "win":
        print("  you win! 🎉")
    else:
        print("  you lose. better luck next round.")


def print_score(wins, losses, ties):
    total = wins + losses + ties
    print(f"\n  score — you: {wins}  computer: {losses}  ties: {ties}  (of {total} rounds)")


def get_player_choice():
    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}

    while True:
        raw = input("  your choice (r/p/s): ").strip().lower()

        if raw in shortcuts:
            return shortcuts[raw]
        if raw in CHOICES:
            return raw

        print("  type r, p, or s.\n")


def main():
    print("\n  === rock, paper, scissors ===")
    print("  first to have fun wins.\n")

    wins, losses, ties = 0, 0, 0

    while True:
        player   = get_player_choice()
        computer = get_computer_choice()
        result   = get_result(player, computer)

        print_round(player, computer, result)

        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            ties += 1

        print_score(wins, losses, ties)

        print()
        again = input("  play again? (y/n): ").strip().lower()
        print()

        if again != "y":
            break

    print("  thanks for playing. final score:")
    print_score(wins, losses, ties)

    if wins > losses:
        print("\n  you came out ahead. nice.\n")
    elif losses > wins:
        print("\n  computer wins this time.\n")
    else:
        print("\n  all square. solid session.\n")


main()
