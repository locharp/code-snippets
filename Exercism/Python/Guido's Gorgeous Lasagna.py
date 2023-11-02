EXPECTED_BAKE_TIME = 40

def bake_time_remaining( minutes_in_oven ):
    
    return EXPECTED_BAKE_TIME - minutes_in_oven



def preparation_time_in_minutes( number_of_layers ):
    
    return 2 * number_of_layers



def elapsed_time_in_minutes( number_of_layers, elapsed_bake_time ):
    
    return preparation_time_in_minutes( number_of_layers ) + elapsed_bake_time
