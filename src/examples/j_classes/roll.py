class Roll:
    __die1 = 0
    __die2 = 0
    __rolled_value = 0 #value of the two die 1-12

    def __init__(self, die1, die2):
        self.__die1 = die1
        self.__die2 = die2
        self.__rolled_value = self.__die1.roll() + self.__die2.roll()

    def roll_value(self):
        return self.__rolled_value

        