import random

def play():
    user = input("Choose your option: 'r' for Rock, 'p' for Paper, or s for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a draw!'
    
    if winner(user, computer):
        return 'You won!'

    return 'You lost! Better luck next time!' 
       
def winner(player, opponent):
    # return true if player wins
    # r > s, p > r, s > p        
    if (player == 'r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
        return True
    
print(play())