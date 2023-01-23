from random import shuffle


def shuffle_cup_ball_list(cup_ball_list):
    shuffle(cup_ball_list)
    return cup_ball_list


def user_guess():
    player_name = input("Hello Player! What is your name")
    player_guess = ''
    while player_guess not in ['0', '1', '2']:
        player_guess = input("Please enter which index you think the ball is in")
    return player_name, int(player_guess)


def game_check(shuffle_cup_ball_list, user_guess, player_name):
    if shuffle_cup_ball_list[user_guess] == 0:
        print(f"You guessed right, {player_name}!")
    else:
        print(f"Wrong choice, {player_name}! Try again")
        print("Take a look at where the ball is. Better luck next time!")
        print(shuffle_cup_ball_list)


cup_ball_list = [' ', 'O', ' ']

shuffled_list = shuffle_cup_ball_list(cup_ball_list)
player_name, player_guess = user_guess()

game_check(shuffled_list, player_guess, player_name)
