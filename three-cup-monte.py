from random import shuffle


# function to shuffle the cup and ball list
def shuffle_cup_ball_list(cup_ball_list):
    """
    This function takes a list of cup and ball as an input and uses the shuffle() function from the random module
    to randomly shuffle the positions of the elements in the list. It then returns the shuffled list.
    """
    shuffle(cup_ball_list)  # shuffle the positions of elements in the list
    return cup_ball_list


# function to get the user's name and guess
def user_guess():
    """
    This function prompts the user to enter their name and then repeatedly prompts them to enter a guess of
    which index they think the ball is in (0, 1, or 2) until they enter a valid input.
    It then returns the user's name and guess as a tuple.
    """
    player_name = input("Hello Player! What is your name?")
    player_guess = ''
    while player_guess not in ['0', '1', '2']:
        player_guess = input("Please enter which index you think the ball is in")
    return player_name, int(player_guess)


# function to check if the user's guess is correct
def game_check(shuffle_cup_ball_list, user_guess, player_name):
    """
    This function takes the shuffled list, the user's guess, and the user's name as inputs, and checks if the user's
    guess is correct by comparing it to the index of the element in the shuffled list. If the guess is correct,
    it prints a message of congratulations to the user, otherwise it prints a message of failure and displays the
    shuffled list. The code then creates a list of cups and balls, shuffles it, prompts the user for their name and
    guess, and checks the user's guess.
    """
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
