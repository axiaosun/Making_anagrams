#!/usr/bin/env python3

# Given 2 strings, how many characters must you delete to make the two strings anagrams of each other

import math
import os
import random
import re
import sys
from collections import Counter

def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    count_a.subtract(count_b)
    return sum(abs(i) for i in count_a.values())
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

