from src.examples.j_classes.die import Die
from src.examples.j_classes.player import Player


player = Player()
die1 = Die()
die2 = Die()

choice = 'Y'

while(choice == 'Y'):
    roll = player.roll_dice(die1, die2)

    print("Player rolled: ", roll.roll_value())

    choice = input("Enter Y to roll again: ")

player.display_rolls()


