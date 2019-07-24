import random
game_on = True

def master():
	print_rules()
	secret_code = get_code()
	while game_on:
		guess_round()
	else:
		print_lost(secret_code)

def print_rules():
	""" This function will print the game header and rule page. """
	print("---[ MASTERMIND ]---")
	rules = """ RULES
	A SECRET CODE WILL BE GENERATED, TRY TO FIND IT BEFORE THE TIME IS UP!
	After each guess, the program will give feedback:
		B: there is one right digit on the right place.
		W: there is one right digit but NOT on the right place.
	e.g.  secret code: 4523
				guess:			 1234	 -> WWW
				guess:			 5423  -> BBWW
				guess:       2322  -> BBB """
	print(rules)

def get_code():
	pass

def guess_round():
	pass

def print_lost():
	pass
