def title_case( title, minor_words='' ):
    if title == "":
        return title
    
    words = title.lower().split()
    
    for i in range( 1, len( words ) ):
        if words[i] not in minor_words.lower().split():
            words[i] = words[i].capitalize()
            
    words[0] = words[0].capitalize()
    
    return " ".join( words )