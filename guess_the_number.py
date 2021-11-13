# Main File to start the app
from random import randint
import time

starter_script = "Welcome..."
menu_choose_continuation = "0. to continue"
menu_choose_difficulty_mode = "1. Easy\n2.Difficult"
menu_choose_range = "1. Amateur\n2. Adbenturous\n3. Pro"
menu_choose_player_mode = "1. Computer\n2.Multiplayer"
range_limit = [(0, 100), (0, 1000), (-1000, 1000)]


def display_winner(score_list, runner_up_possibility):
    print(f"The final score list is:\n{score_list}")

    # IMPLEMENT PROPER LOGIC
    winner = max(score_list, key=score_list.get)
    print(f"{winner} wins with max score of {score_list[winner]}")

    if runner_up_possibility == True:
        score_list[winner] = 0
        runner_up = max(score_list, key=score_list.get)
        print(
            f"{runner_up} is the runner_up with second_highest score of {score_list[runner_up]}")


def give_chance(difficulty_level, ans, range_option, player):
    prev_guesses = []
    lower_limit, upper_limit = range_limit[range_option]
    guess = 0

    for chance in range(7, 1, -1):
        print(f"{player}! You have {chance} chances left.")

        if chance != 7 and difficulty_level == 1:
            print(f"The previous guesses are:\n{prev_guesses}")

        if player == "Robo":
            guess = randint(lower_limit, upper_limit)
            print(f"Robo guesses: ", end="")
            time.sleep(0.025)
            print(guess)
        else:
            guess = int(
                input(f"Enter your guess within {lower_limit} - {upper_limit}: _"))

        if guess == ans:
            print(
                f"Congratulations {player}! Correct Answer! Your score for this round: {chance}")
            return chance

        # implement the logic
        if abs(guess - ans) <= 10:
            print("hot")
        else:
            print("cold")

        if difficulty_level == 1:
            prev_guesses.append(guess)

    print("Sorry! Wrong Answers! You Lost this time.")
    return 0


def start_game(difficulty_level, range_option, players, score_list, runner_up_possibility=False):
    lower_limit, upper_limit = range_limit[range_option]
    continue_game = 'y'

    try:
        while continue_game == 'y' or continue_game == 'Y':

            for index, player in enumerate(players):
                if player == "Robo":
                    ans = randint(lower_limit, upper_limit)
                    print(ans)
                else:
                    ans = int(
                        input(f"Hey {player}. Enter a number within {lower_limit} - {upper_limit} for your opponent to guess: _"))

                if index == len(players) - 1:
                    score = give_chance(
                        difficulty_level, ans, range_option, players[0])
                    score_list[players[0]] = score_list[players[0]] + score
                else:
                    score = give_chance(
                        difficulty_level, ans, range_option, players[index+1])
                    score_list[players[index+1]
                               ] = score_list[players[0]] + score

            continue_game = input(
                f"For further rounds: \n{menu_choose_continuation}")
    except Exception as e:
        print(e)

    display_winner(score_list, runner_up_possibility)


def single_player_mode(difficulty_level, range_option):
    player = input("Enter your name: _")
    score_list = {
        f"{player}": 0,
        "Robo": 0,
    }
    start_game(difficulty_level, range_option, [player, "Robo"], score_list)


def multi_player_mode(difficulty_level, range_option):
    n = int(input("Enter number of players: _"))
    print("Enter names of players:")
    players = []
    score_list = {}

    for index in range(n):
        players.append(input(f"Player {index+1}: _"))
        score_list = {f"{players[-1]}": 0}

    start_game(difficulty_level, range_option, players, score_list, n > 4)


def play_game():
    print(starter_script)
    input()

    difficulty_level = int(input(f"{menu_choose_difficulty_mode}\n"))
    range_option = int(input(f"{menu_choose_range}\n"))

    choice = int(input(f"{menu_choose_player_mode}\n"))
    if choice == 1:
        single_player_mode(difficulty_level, range_option)
    else:
        multi_player_mode(difficulty_level, range_option)

    choice = input(f"To play again: {menu_choose_continuation}:\n?_")
    if choice == 'y' or choice == 'Y':
        play_game()


if __name__ == "__main__":
    play_game()
