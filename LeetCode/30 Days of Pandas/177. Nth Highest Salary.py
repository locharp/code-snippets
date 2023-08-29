import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = sorted( employee.groupby( "salary" ).groups.keys(), reverse = True )
    
    return pd.DataFrame( { f"getNthHighestSalary({ N })": [ None if len( employee ) < N else employee[ N - 1 ] ] } )