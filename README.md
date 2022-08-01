# 15puzzleMDSum
MD sum checker for any size NxN puzzle

Usage example:

check_md("9 4 7 3 5 6/13 1 15 24 21 16/14 19 8 18 23 10/32 20 0 11 22 26/33 27 17 29 28 30/25 31 34 2 35 12")

Return: 71

That example is for 6x6 puzzle, you can also use scrambles with space instead of "/" so just list of all number of the puzzle in order with 0 as blank tile.
The size of the puzzle is parsed by the amount of elements.
No checking for valid or invalid input, check that before using this function.
