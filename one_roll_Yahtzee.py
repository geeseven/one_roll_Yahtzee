#!/usr/bin/env python
from argparse import ArgumentParser
from random import randint


def dieRoll(sided_die):
    return randint(1, sided_die)


def numberToUnicodeDice(number):
    # convert 1 2 3 4 5 6 to
    # ⚀ ⚁ ⚂ ⚃ ⚄ ⚅
    if number > 6:
        return str(number)
    else:
        number += 5
        result = 9850 + number
        return chr(result)


def showYahtzeeRoll(die, num):
    yahtzee = ""
    for _ in range(num):
        yahtzee += numberToUnicodeDice(die) + " "
    return yahtzee


def yahtzeeRoll(number_of_dice):
    # No need to roll all dice at once.
    # Roll one by one and only keep going if they match.
    roll = []
    first_die = dieRoll(dice_sides)
    roll.append(first_die)
    for other_dice in range(1, number_of_dice):
        die = dieRoll(dice_sides)
        if first_die != die:
            break
        else:
            roll.append(die)
    return roll


parser = ArgumentParser(
    description="test how many rolls it takes to get a one roll Yahtzee "
    + showYahtzeeRoll(dieRoll(6), 5)
)
parser.add_argument(
    "-s",
    "--dice_sides",
    help="number of sides per dice (default: 6)",
    type=int,
    default=6,
)
parser.add_argument(
    "-n",
    "--number_of_dice",
    help="number of dice (default: 5)",
    type=int,
    default=5,
)
args = parser.parse_args()

dice_sides = args.dice_sides
dice_number = args.number_of_dice

print(
    "Attempting to get a one roll Yahtzee with {} {}-sided dice".format(
        dice_number, dice_sides
    )
)
print("rolling...")

count = 0

while True:
    count += 1
    attempt = yahtzeeRoll(dice_number)
    if len(attempt) == dice_number:
        print("after {:,} rolls, this Yahtzee was rolled".format(count))
        print(showYahtzeeRoll(attempt[0], dice_number))
        break
