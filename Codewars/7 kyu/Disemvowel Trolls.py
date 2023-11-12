def disemvowel( string_ ):
  
    for i in "aeiouAEIOU":
        string_ = string_.replace( i, "" )
        
    return string_
