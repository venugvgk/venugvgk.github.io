import random

TARGET_SCORE = 30
COMPUTER_HOLD_AT = 20


def roll_die():
    return random.randint(1, 6)


def print_turn_header(name, score):
    print(f"\n{name}'s turn. Current score: {score}")


def player_turn(score):
    turn_total = 0
    print_turn_header("You", score)

    while True:
        choice = input("Roll or hold? (r/h): ").strip().lower()

        if choice not in {"r", "h"}:
            print("Please type r to roll or h to hold.")
            continue

        if choice == "h":
            print(f"You hold. You add {turn_total} points.")
            return turn_total

        roll = roll_die()
        print(f"You rolled: {roll}")

        if roll == 1:
            print("Pig! You lose all points from this turn.")
            return 0

        turn_total += roll
        print(f"Turn total: {turn_total}")

        if score + turn_total >= TARGET_SCORE:
            print(f"You reached {score + turn_total} points.")
            return turn_total


def computer_turn(score):
    turn_total = 0
    print_turn_header("Computer", score)

    while True:
        if score + turn_total >= TARGET_SCORE:
            print(f"Computer holds at {turn_total} to try to win.")
            return turn_total

        if turn_total >= COMPUTER_HOLD_AT:
            print(f"Computer holds at {turn_total}.")
            return turn_total

        roll = roll_die()
        print(f"Computer rolled: {roll}")

        if roll == 1:
            print("Computer got Pig and loses the turn total.")
            return 0

        turn_total += roll
        print(f"Computer turn total: {turn_total}")


def main():
    player_score = 0
    computer_score = 0

    print("Pig Dice")
    print(f"First to {TARGET_SCORE} wins.")
    print(f"Computer strategy: hold at {COMPUTER_HOLD_AT} or when it can win.\n")

    while player_score < TARGET_SCORE and computer_score < TARGET_SCORE:
        player_score += player_turn(player_score)
        print(f"Your total score is now {player_score}.")

        if player_score >= TARGET_SCORE:
            break

        computer_score += computer_turn(computer_score)
        print(f"Computer total score is now {computer_score}.\n")

    print("Final scores")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")

    if player_score >= TARGET_SCORE:
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main()