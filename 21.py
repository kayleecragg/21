"""
Group name: A1_OnCampus4_Group3
Authors: Jodi Nguyen, Kaylee Cragg
"""


import time
import random

def display_rules():
  print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)
  input("Press enter to go back")
  return


def display_main_menu():
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")


def int_input(prompt="", restricted_to=None):
  """
  Helper function that modifies the regular input method,
  and keeps asking for input until a valid one is entered. Input 
  can also be restricted to a set of integers.

  Arguments:
    - prompt: String representing the message to display for input
    - restricted: List of integers for when the input must be restricted
                  to a certain set of numbers

  Returns the input in integer type.
  """
  while True:
    player_input = input(prompt)
    try:
      int_player_input = int(player_input)
    except ValueError:
      continue
    if restricted_to is None:
      break
    elif int_player_input in restricted_to:
      break

  return int_player_input


def cpu_player_choice(score):
  """
  This function simply returns a choice for the CPU player based
  on their score.

  Arguments:
    - score: Int

  Returns an int representing a choice from 1, 2 or 3.
  """
  time.sleep(2)
  if score < 14:
    return 1
  elif score < 17:
    return 3
  else:
    return 2



#  ------------------- TASK 1 ----------------------

def display_game_options(player):
    """
    Prints the game options depending on if a player's score is
    >= 14.
    Arguments:
    - player: A player dictionary object
"""
    #PRINT HEADER
    print("------------"+player['name']+"'s turn------------")
    print(player['name']+"'s score:",player['score'])
    #Checks if player scores is less than 14
    if player['score']< 14:
        print("1. Roll")
        print("2. Stay")
    #Otherwise player score is at 14 or above
    else:
        print("1. Roll")
        print("2. Stay")
        print("3. Roll One")

def display_round_stats(round, players):
    """
  Print the round statistics provided a list of players.

  Arguments:
    - round: Integer for round number
    - players: A list of player-dictionary objects
    """
    #Creates header
    print("-----------Round "+str(round)+"-----------")
    # Prints players scores
    for i in range(len(players)):
        print(players[i]['name'],"is at",players[i]['score'])





#  ------------------- TASK 2 ----------------------

def roll_dice(num_of_dice=1):
    """
  Rolls dice based on num_of_dice passed as an argument.

  Arguments:
    - num_of_dice: Integer for amount of dice to roll

  Returns the following tuple: (rolls, display_string)
    - rolls: A list of each roll result as an int
    - display_string: A string combining the dice art for all rolls into one string
"""
    die_art = {
    
    1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
    2: ["┌─────────┐", "│    ●    │", "│         │", "│    ●    │", "└─────────┘"],
    3: ["┌─────────┐", "│    ●    │", "│    ●    │", "│    ●    │", "└─────────┘"],
    4: ["┌─────────┐", "│   ● ●   │", "│         │", "│   ● ●   │", "└─────────┘"],
    5: ["┌─────────┐", "│   ● ●   │", "│    ●    │", "│   ● ●   │", "└─────────┘"],
    6: ["┌─────────┐", "│   ● ●   │", "│   ● ●   │", "│   ● ●   │", "└─────────┘"]
}
    #create a roll list using module random inorder to mimic a die roll, and append it to the empty roll list
    rolls_list = []

    for i in range(0, num_of_dice):
        rand_numbers = random.randint(1, 6)
        rolls_list.append(rand_numbers)

    #Create the die art, creates an empty string and appends according die art string to the empty string while appending a new line after every layer of die art inorder to create a completete image
    s = ""
    for num in rolls_list:
        s += die_art[num][0]
    s += "\n"
    for num in rolls_list:
        s += die_art[num][1]
    s += "\n"
    for num in rolls_list:
        s+= die_art[num][2]
    s+="\n"
    for num in rolls_list:
        s+= die_art[num][3]
    s+= "\n"
    for num in rolls_list:
        s+= die_art[num][4]
    s+= "\n"

    #creates the final tuple containing roll list and die art string
    final = ((rolls_list),s)
    print(rolls_list)
    return final




#  ------------------- TASK 3 ----------------------

def execute_turn(player, player_input):
    """
  Executes one turn of the round for a given player.

  Arguments:
    - player: A player dictionary object

  Returns an updated player dictionary object.
"""

    #Checks if player choses to roll with a score 21
    if (player["score"] == 21) and (player_input == 1 or 3):
        player["bust"] = True

    #PLAYER CHOOSES TO STAY, update stay key as well prints players score
    if player_input == 2:
        player["at_14"] = True
        print(player["name"],"has stayed with a score of", player["score"])
        if player["score"]>21:
            player["bust"] = True
            print(player["name"],"goes bust!")
        player["stayed"] = True

    #PLAYER CHOOSES TO ROLL TWO, checks whether player's score is less than 14 and calls roll_dice() function
    elif (player_input == 1) and (player["score"]<=14):
        print("Rolling both...")
        number_rolled = roll_dice(2)
        print(number_rolled[1])

        #Finds the sum of the roll and updates player dictionary
        rolled_sum = sum(number_rolled[0])
        player_score = rolled_sum + int(player["score"])
        print(player["name"],"is now on", player_score)
        player["score"] = player_score
        player["at_14"] = True
        player["stayed"] = False
        if player["score"]>21:
            player["bust"] = True
            print(player["name"],"goes bust!")

    #PLAYER ROLLS ONE, calls roll_dice() function
    else:
        print("Rolling one...")
        number_rolled = roll_dice(1)
        print(number_rolled[1])

        ##Finds the sum of the roll and updates player dictionary
        rolled_sum = sum(number_rolled[0])
        player_score = rolled_sum + int(player["score"])
        print(player["name"],"is now on", player_score)
        player["score"] = player_score
        player["at_14"] = True
        player["stayed"] = False
        if player["score"]>21:
            player["bust"] = True
            print(player["name"],"goes bust!")
    return player

# player = {'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust':
#     False}
# player = execute_turn(player, 1)
# print(player)

#  ------------------- TASK 4 ----------------------

def end_of_game(players):
    """
  Takes the list of all players and determines if the game has finished,
  returning false if not else printing the result before returning true.

  Arguments:
    - players: A list of player-dictionary objects

  Returns True if round has ended or False if not. If true results are
  printed before return.
"""

    all_bust = True
    max_score_count = 0
    # initialize maximum score to -1
    max_score = -1
    # use for loop to iterate over each player in the dictionary
    for player in players:
        # if the player is not bust
        if player['bust'] == False:
            # set all_bust flag to false
            all_bust = False
        # if the player score is greater than max_score
        if player['score'] > max_score:
            # assign the players score to max_score
            max_score = player['score']
            # set max_score_count to 1
            max_score_count = 1
            # assign the name of the player to winner_name
            winner_name = player['name']
            # if the player score is equal to max_score i.e. there are two players with the same score
        elif player['score'] == max_score:
            # increase the max_score_count by 1
            max_score_count += 1
        # if all players are bust
        if all_bust == True:
            # print the message
            print("Everyone's gone bust! No one wins :(")
            return True
        if max_score_count > 1:
            # print the message
            print("The game is a draw! No one wins :(")
            # then return True
            return True
        # if max_score_count is equal to one, i.e. there is a winner
        if max_score_count == 1:
            # print the message
            print(winner_name, "is the winner!")
            # then return True
            return True
        # otherwise return False
        return False


#  ------------------- TASK 5 ----------------------
def solo_game():
    """
  This function defines a game loop for a solo game of Twenty One against 
  AI.
"""
    round = 0
    player = {'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust':False}
    cpu_player = {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust':False}
    players = [player,cpu_player]
    while(True):
        display_round_stats(round,players)
        display_game_options(player)
        option = int(input("Please enter an option: "))
        execute_turn(player,option)
        display_round_stats(round,players)
        display_game_options(cpu_player)
        option = int(input("Please enter an option: "))
        execute_turn(cpu_player,option)

        if(end_of_game(players)):
            break
        else:
            round +=1


#  ------------------- TASK 6 ----------------------

def multiplayer_game(num_of_players):
    """
  This function defines a game loop for a local multiplayer game of Twenty One, 
  where each iteration of the while loop is a round within the game. 
"""
    round = 0
    player = {}
    players = []
    for i in range(0,num_of_players):
        player[i] = {'name': 'Player ' + str(i+1), 'score': 0, 'stayed': False, 'at_14': False, 'bust':False}
        players.append(player[i])
    while(True):
        for i in range(0,num_of_players):
            display_round_stats(round,players)
            display_game_options(player[i])
            option = int(input("Please enter an option: "))
            execute_turn(player[i],option)
        if(end_of_game(players)):
            break
        else:
            round +=1

#  ------------------- TASK 7 ----------------------

def main():
    """
  Defines the main loop that allows the player to start a game, view rules or quit.
"""
    while(True):
        print("---------- Main Menu ----------")
        print("Welcome to Twenty One!")
        print("1. Solo")
        print("2. Local Mulitplyer")
        print("3. Rules")
        print("4. Exit")
        option = int(input("Plase enter an Option: "))
        if(option==1):
            solo_game()
        elif(option==2):
            num = int(input("Please enter number of players: "))
            multiplayer_game(num)
        elif(option==3):
            print("""
      - Players begin with a score of 0.
      - Each player has one turn to either roll or stop rolling each round.
      - Players can only do a regular roll of two dice until they reach a score of at least 14.
      - Players with a score >= 14 have the option to only roll one dice.
      - If a player scores more than 21 they go bust and are out of the game.
      - The winning player is the one with the score closest to 21 when everyone has finished rolling.
      - If all players go bust, no one wins.
      - If more than one player has the winning score, no one wins.""")
        elif(option==4):
            print("Program Terminated")
            break
        else:
            print("Please enter a valid number")

main()
