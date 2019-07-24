import random

def master():
	ROUNDS = 12
	print_rules()
	secret_code = get_code()
	print("DEBUG", secret_code)
	while ROUNDS:
		if guess_round(secret_code, ROUNDS):
			break
		ROUNDS = ROUNDS - 1
	else:
		print_lost(secret_code)

def print_rules():
	""" This function will print the game header and rule page. """
	print("---[ MASTERMIND ]---")
	rules = """ RULES
A SECRET CODE WILL BE GENERATED, TRY TO FIND IT BEFORE THE TIME IS UP!
IT IS A FOUR DIGIT CODE CONTAINING {1, 2, 3, 4, 5, 6}
After each guess, the program will give feedback:
	B: there is one right digit on the right place.
	W: there is one right digit but NOT on the right place.
	e.g.  secret code: 4523
				guess:       1234  -> WWW
				guess:       5423  -> BBWW
				guess:       2322  -> BBB """
	print(rules)

def get_code():
	""" This function returns a random code. """
	code = ""
	for i in range(4):
		code =  code + str(random.randint(1,6))
	return code

def guess_round(secret_code, ROUNDS):
	""" Simulate one guess round: analyze input, give feedback; returns wether the code has been found."""
	guess = input("[{0}] Please enter a guess: ".format(12 - ROUNDS))
	feedback =  analyze_guess(guess, secret_code)
	print("->", feedback)
	if feedback == "BBBB":
		print_victory()
		return True
	else:
		return False

def analyze_guess(guess, secret_code):
	feedback = ""
	deletion = [] # this variable will contain the positions of B marked digits
	guess_lst = list(guess)
	scrt_code_lst = list(secret_code)
	try:
		for i in range(4):
			if guess[i] == secret_code[i]:
				feedback = feedback + "B"
				deletion.append(i)
	except IndexError:
		print("The guess should be a four digit string containing the mentioned numbers.")

	for i in deletion[::-1]: # backwards in order to avoid dynamically cahnging positions etc
		del guess_lst[i]
		del scrt_code_lst[i]
	for i in guess_lst[:]:
		if i in scrt_code_lst:
			scrt_code_lst.remove(i)
			guess_lst.remove(i)
			feedback = feedback + "W"
	return feedback

def print_lost(code):
	print("Ahh, the secret code was {0}; you were quite close.".format(code))

def print_victory():
	print("very nice, you guessed the code!")

master()
