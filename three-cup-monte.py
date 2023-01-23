from random import shuffle

cup_ball_list = [' ', 'O', ' ']


def shuffle_cup_ball_list(cup_ball_list):
    shuffle(cup_ball_list)
    return cup_ball_list


def user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Please enter which index you think the ball is in")
    return int(guess)


def game(shuffle_cup_ball_list, user_guess):
    if shuffle_cup_ball_list[user_guess] == 0:
        print("you win")
    else:
        print("Sorry")

h = shuffle_cup_ball_list(cup_ball_list)
v = user_guess()

game(h,v)