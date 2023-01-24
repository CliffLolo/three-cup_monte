from random import shuffle


# function to shuffle the cup and ball list
def shuffle_cup_ball_list(cup_ball_list):
    """
    This function takes a list of cup and ball as an input and uses the shuffle() function from the random module
    to randomly shuffle the positions of the elements in the list. It then returns the shuffled list.
    """
    shuffle(cup_ball_list)  # shuffle the positions of elements in the list
    return cup_ball_list


# function to get user's name and guess
def user_guess():
    player_name = input("Hello Player! What is your name")
    player_guess = ''
    while player_guess not in ['0', '1', '2']:
        player_guess = input("Please enter which index you think the ball is in")
    return player_name, int(player_guess)


# function to check if the user's guess is correct
def game_check(shuffle_cup_ball_list, user_guess, player_name):
    if shuffle_cup_ball_list[user_guess] == 0:
        print(f"You guessed right, {player_name}!")
    else:
        print(f"Wrong choice, {player_name}! Try again")
        print("Take a look at where the ball is. Better luck next time!")
        print(shuffle_cup_ball_list)


# Initializing the list of cups and balls
cup_ball_list = [' ', 'O', ' ']

# shuffling the list
shuffled_list = shuffle_cup_ball_list(cup_ball_list)

# getting user's name and guess
player_name, player_guess = user_guess()

# checking the user's guess
game_check(shuffled_list, player_guess, player_name)
