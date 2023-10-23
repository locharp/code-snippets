collections import defaultdict

def stock_list( list_of_art, list_of_cat ):
    
    if len( list_of_art ) < 1:
        return ""
    
    d = defaultdict( int )
    
    for i in list_of_art:
        if i[0] in list_of_cat:
            d[ i[0] ] += int( i.split()[1] )
            
    return " - ".join( f"({ i } : { d[i] })" for i in list_of_cat )
