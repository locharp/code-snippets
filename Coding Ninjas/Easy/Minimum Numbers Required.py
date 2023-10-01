rom math import *

def findMinNumbers( arr, total, maxVal ):
    return ceil( abs( total - sum( arr ) ) / maxVal )
