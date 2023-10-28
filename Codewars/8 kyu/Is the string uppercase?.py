def is_uppercase( inp ):
  
    inp = "".join( i for i in inp if i.isalpha() )
  
    return inp == "" or inp.isupper()
