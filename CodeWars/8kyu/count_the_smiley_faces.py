from re import fullmatch

def count_smileys(arr ):
    return len( [ face for face in arr if fullmatch( "[:;][-~]?[)D]", face ) ] )
