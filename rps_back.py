import random
import matplotlib.pyplot as plt
import rps


def instructions(response):
    instruction_string = "Choose rock, paper, or scissors from the buttons. "
    instruction_string += "The computer will then choose a move. "
    instruction_string += "Rock beats scissors, scissors beats paper, and paper beats rock."

    response = response.lower()
    if response == "yes":
	rps.print_instructions(instruction_string)
    

def check_name(name):

    error = "Somethings wrong. "

    if len(name) > 30:
        rps.quit_game(error + "Your name is too long!")
    if len(name) < 2:
        rps.quit_game(error + "Your name is too short!")
    if ' ' in name:
        rps.quit_game(error + "Your name cannot contain spaces!")
    if name[0].isupper() == False:
        rps.quit_game(error + "Your name must start with an upper case letter!")
    return name


def check_times_to_play(num):
    error = "Number is not correct"
    
    if int(num) > 21:
        rps.quit_game(error + "Your number is too big!")
    if int(num) < 2:
        rps.quit_game(error + "Your number is too small!")
    return num


def play_game(name):
    
    # This gets the move from a player when they push a button.
    player_move = rps.get_player_move()

    # Use the random library to chose a random move for the player.

    # Use if statements to check who won. Set who_won equal to 'Computer', 'Player', or 'Tie'
    

    who_won = ""

    # After determines who won, build a results string.
    # The next 3 lines partially builds this string. Complete for computer, add for tie, and add line for winner
    results = "Player played " + player_move
    results += "\n"
    results += "Computer played " + computer_move

    if who_won == "Tie":
        results += "The match was a tie."

    # Use rps.display_results to display the results string for the game.


    # return the variable who_won
  


def play_match():

    rps.ask_instructions()

    player_name = rps.get_name()

    num_times = rps.get_num_play()

    
    # Use these variables to keep track of who won
    ties = 0
    player_wins = 0
    computer_wins = 0


    # Use a while or for loop to call play_game the correct amount of times
    count = 0
    while count < num_times:
        game_winner = play_game(player_name)
        # Now use an if statement to increment total for winner
        # i.e. will increment either ties, player_wins, or computer_winds
        count = count + 1

    # Call make_graph using the variables for win counts above.
    make_graph(player_name, player_wins, computer_wins, ties)




# Create a graph as we did in the previous lab
def make_graph(name, player_wins, comp_wins, ties):
    print "Not implemented yet"


