from src.examples.j_classes.roll import Roll

class Player:

    __rolls = []

    def roll_dice(self, die1, die2):
        roll = Roll(die1, die2)
        self.__rolls.append(roll)

        return roll

    def display_rolls(self):
        print('Rolls for this player: ')

        for roll in self.__rolls:
            print(roll.roll_value())