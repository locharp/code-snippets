from os import *
from sys import *
from collections import *
from math import *

def longestMountain(arr, n):

    i = m = 0
    j = 1
    p = q = False

    while j < n:
        while j < n and arr[j] > arr[ j - 1 ]:
            j += 1
            p = True
            
        while p and j < n and arr[j] < arr[ j - 1 ]:
            j += 1
            q = True

        if p and q:
            m = max( m, j - i )
            j -= 1

        p = q = False
        i = j
        j += 1

    if p and q:
        m = max( m, j - i )

    return m
