import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):

    path_list = list(s)

    valley = level = 0
    d = {"U": 1, "D": -1}

    for step in path_list:
        level += d[step]

        if level == 0 and step == "U":
            valley += 1

    return valley


if __name__ == "__main__":
    print(countingValleys(8, "UDDDUDUUUUUUD"))
