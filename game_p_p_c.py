import random

choices = ["rock", "paper", "scissors"]

def who_win(player, bot):
	if player == bot:
		return "Draw 🤝"
	elif (
		(player == "rock" and bot == "scissors") or
		(player == "paper" and bot == "rock") or
		(player == "scissors" and bot == "paper")
	):
		return "You win! 💯🎉"
	else:
		return "Bot win! 😓"
	
while True:
		player = input("Choose rock, paper or scissors (or 'q' to quit ) :").lower()
		if player == 'q':
			print("Thank you for playing!👾")
			break
		if player not in choices:
			print("invalid chose, you suck! 👻")
			continue
		bot = random.choice(choices)
		print("You choise : {}".format(player))
		print("Bot choise: {}".format(bot))
		print(who_win(player, bot))
		print("-" * 40)
