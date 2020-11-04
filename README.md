# one_roll_Yahtzee

Several years ago, Numberphile had a series of videos about [one roll Yahtzee][0] and this my take.

```console
$ python one_roll_Yahtzee.py 
Attempting to get a one roll Yahtzee with 5 6-sided dice
rolling...
after 1,212 rolls, this Yahtzee was rolled
⚅ ⚅ ⚅ ⚅ ⚅ 

$ python one_roll_Yahtzee.py --help
usage: one_roll_Yahtzee.py [-h] [-s DICE_SIDES] [-n NUMBER_OF_DICE]

test how many rolls it takes to get a one roll Yahtzee ⚁ ⚁ ⚁ ⚁ ⚁

optional arguments:
  -h, --help            show this help message and exit
  -s DICE_SIDES, --dice_sides DICE_SIDES
                        number of sides per dice (default: 6)
  -n NUMBER_OF_DICE, --number_of_dice NUMBER_OF_DICE
                        number of dice (default: 5)
 
$ python one_roll_Yahtzee.py --dice_sides 7 --number_of_dice 9
Attempting to get a one roll Yahtzee with 9 7-sided dice
rolling...
after 5,622,174 rolls, this Yahtzee was rolled
⚀ ⚀ ⚀ ⚀ ⚀ ⚀ ⚀ ⚀ ⚀ 
```

[0]: https://www.youtube.com/watch?v=fiTwar7mFws&list=PL8D3EA4DDD533BEE5
