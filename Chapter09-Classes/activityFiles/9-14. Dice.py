from random import randint

class Dice():
	def __init__ (self, sides=6):
		self.sides = sides
		
	def roll_dice(self):
		x = randint(1, self.sides)
		print(x)
		
roll = Dice(6)
roll.roll_dice()

roll = Dice(10)
roll.roll_dice()

roll = Dice(20)
roll.roll_dice()



		
		
