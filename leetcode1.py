#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_elements = sorted(arr)
    temp1 = []
    temp2 = []
    for i in range(len(sorted_elements)):
        if (i == 0):
            temp1.append(sorted_elements[i])
        elif (i == len(sorted_elements)-1):
            temp2.append(sorted_elements[i])
        else:
            temp1.append(sorted_elements[i])
            temp2.append(sorted_elements[i])
    result1 = sum(temp1)
    result2 = sum(temp2)
    print(result1, result2)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
