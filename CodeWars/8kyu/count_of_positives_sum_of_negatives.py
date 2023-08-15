def count_positives_sum_negatives( arr ):
    return [] if arr is None or arr == [] else [ len( [ i for i in arr if i > 0 ] ), sum( i for i in arr if i < 0 ) ]