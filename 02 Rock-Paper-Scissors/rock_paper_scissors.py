import random

def play():
	user_input = input('"r" for rock , "P" for paper, "s" for scissors\n -->  ')
	computer = random.choice(['r','s','p'])

	if user_input == computer:
		return 'It\'s a tie.'

	if is_win(user_input,computer):
		return 'You won!'
	return 'You Lost.'
 

def is_win(player,opponent):
		#r > s, s>p, p>r
	if (player == 'r' and opponent == 's') or (player=='s'and opponent=='p') or (player=='p' and opponent=='r'):
		return True

print(play())