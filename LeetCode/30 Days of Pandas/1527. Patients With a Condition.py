import pandas as pd

def diab1( conditions ):
    for condition in conditions.split():
        if condition[ : 5 ] == "DIAB1":
            return True
        
    return False
def find_patients( patients: pd.DataFrame ) -> pd.DataFrame:
    return patients[ patients["conditions"].apply( diab1 ) ]