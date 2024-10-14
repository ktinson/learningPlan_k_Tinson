import random
def main():
   player1 = randomChoice()
   player2 = randomChoice()
   if player1 == player2:
       print(f'player1: {player1} vs player2: {player2} = tie')
   elif player2 == "rock" and player1 == "scissors" or player2 == "paper" and player1 == "rock" or player2 == "scissors" and player1 == "paper":
       print(f'player1: {player1} vs player2: {player2} = player 2 wins')
   else:
        print(f'player1: {player1} vs player2: {player2} = player 1 wins')



def randomChoice():
    return random.choice(['rock', 'paper', 'scissors'])


main()