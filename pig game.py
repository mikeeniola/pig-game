import random


def roll(): #define a function by writeing def then anem the function after
    min_value = 1
    max_value = 6
    roll =  random.randint(min_value, max_value)

    return roll #sends a value back to the code that called the function


#code for AI decision-making function based on memory(luck)
def ai_decision_with_memory(current_score, total_score, past_rolls):
    average_roll = sum(past_rolls) / len(past_rolls) if past_rolls else 0 #so if the ai everage roll is below 3 (indication bad luck),stop early
    if average_roll < 3 and total_score > 15:
        return current_score < 15
    else:
        return current_score < 25
   #make the AI keep rolling until the current score for the turn is ... or more
     #   return False
    #return True


#code for AI decision-making function based on memory(luck)
def ai_decision_based_on_opponent(current_score, ai_total_score, opponent_score):
    if ai_total_score < opponent_score: #so if the AI is lossing, it would play more aggressively so risky
        return current_score <25
    else: #so if the ai is winning, it can continue to play cautiously
        return current_score < 15
    
#combining both ai thinking into one
def combined_ai_decision(current_score, ai_total_score, opponent_score, past_rolls):
    return (ai_decision_with_memory(current_score, ai_total_score, past_rolls) and ai_decision_based_on_opponent(current_score, ai_total_score, opponent_score))


while True: #so keep asking until the user gives a number that is valid
    players = input("Enter the number of players (1-4): ") #Allowing 1-4 players
    if players.isdigit(): #isdigit is gonna tell us if its a valid all number
        players = int(players) #convert a string into a integer 
        if 1 <= players <= 4:
            break #exist outside this function, so we will have access to player variables down function
        else:
            print("Must be between 1 - 4 players. ")
    else:
        print("Invalid, try again.")

ai_active = False # set a flag to indicate if AI is playing

if players == 1:
        ai_active = True #Activate AI as the second player

ai_past_rolls = []
max_score = 100
player_scores = [0 for _ in range (players)] # puts a score of zero for every single player we have and range loop the number times we have

if ai_active: #Add an AI player score if AI is active
    player_scores.append(0)

while max(player_scores) < max_score: #as long as no one as reached the max score it keep looping but stop when someone reaches the max and tell the player who won the game
    for player_idx in range(players + (1 if ai_active else 0)): #in this for loop it simulates one person entires turn
       if ai_active and player_idx == players: #this is the AI turn if there is only 1 player
        print ("\nAI's turn!\n")
        current_score = 0
        while True:
            opponent_score = player_scores[0] #assuming player 1 is the opponent
            if combined_ai_decision(current_score, player_scores[player_idx], opponent_score, ai_past_rolls):
                value = roll()
                ai_past_rolls.append(value) #track ai past rolls
                if value == 1:
                    print("AI rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("AI rolled a:", value)
                    print("AI's score is:", current_score)
            else:
                    print("AI stops its turn.")
                    break
        player_scores[player_idx] += current_score
        print("AI's total score is:", player_scores[player_idx])                   
       else: #normal player turn
        print("\nPlayer number", player_idx + 1, "turn has just started!\n") #let them know its their

        print("Your total score is:", player_scores[player_idx], "\n") #tells them their total score at the start of each round
        current_score = 0

        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y": #if u didnt hit y, your turn will be stopped
                    break
            #.lower convert it to lower case, this is done because so i weither they give capital y or lower case y it still covert it to lower case y
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done1") # if you roll a one your turn is done and we are gonna break it out
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)
        
        player_scores[player_idx] += current_score #current score is score per turn and total score is what we are adding to after they finish their turn 
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores) 
winning_idx = player_scores.index(max_score) #give us the idex so either 0,1,2 or 3 of where the maximum score is, which tell us player 0,1, 2 nd so on
if ai_active and winning_idx == players:
    print("AI is the winner with a score of:", max_score)
else:
    print("Player number", winning_idx +1, 
      " is the winner with a score of:", max_score) # adding 1 cause we awnt to start from 1