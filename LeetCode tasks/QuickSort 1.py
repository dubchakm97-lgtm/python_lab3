#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    pivot, bfr, afr = arr[0], [], []
    for elem in arr[1:]:
        if elem <= pivot:
            bfr.append(elem)
        else:
            afr.append(elem)
    bfr.append(pivot)
    bfr.extend(afr)
    return bfr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
