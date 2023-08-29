import pandas as pd

def is_valid( email ):
    if len( email ) < 14 or email[ -13 : ] != "@leetcode.com" or email[0].lower() not in ascii_lowercase:
        return False
    
    for ch in email[ 1 : -13 ].lower():
        if ch not in ascii_lowercase + digits + "_-.":
            return False
        
    return True

def valid_emails( users: pd.DataFrame ) -> pd.DataFrame:
    return users[ users["mail"].apply( is_valid ) ]