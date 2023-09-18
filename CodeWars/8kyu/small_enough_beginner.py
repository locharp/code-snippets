def small_enough(array, limit):
    for i in array:
        if i > limit:
            return False
        
    return True