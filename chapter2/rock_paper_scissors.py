# rock paper scissors game
import random

### initialize global variables ##

flag = True
wins = 0
losses = 0
ties = 0

### Helper functions ###

def comp_selection():
    number = random.randint(1,3)
    if number == 1:
        return 'r'
    elif number == 2:
        return 'p'
    else:
        return 's'

def player_selection():
    selection = 'a'
    while selection not in ['r', 'p', 's', 'x']:
        selection = input("Type in r, p, or s to select for Rock, Paper, or Scissors\nTo exit, type x instead\n")
        selection = selection.lower()
    return selection

def output_translation(input):
    if input == 'r':
        return 'Rock'
    elif input == 'p':
        return 'Paper'
    else:
        return "Scissors"

def compare(p_input, c_input):
    win = ['rs', 'sp', 'pr']
    lose = ['sr', 'ps', 'rp']
    test = p_input + c_input
    global wins 
    global losses
    global ties

    if test in win:
        print('The player wins\n')
        wins += 1
    elif test in lose:
        print('The player loses.\n')
        losses += 1
    else:
        print('This round ends in a tie\n')
        ties += 1
    print('The score is ' + str(wins) + ' win(s), ' + str(losses) + ' loss(es), and ' + str(ties) + ' tie(s).\n')


######

### Main loop ###

while flag:
    computer = comp_selection()
    player = player_selection()
    if player == 'x':
        flag = False
        break
    print('The player has selected ' + output_translation(player))
    print('The computer has selected ' + output_translation(computer))
    compare(player, computer)

print('Thank you for playing.')

######

