import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.groupby( "salary" ).groups.keys()
    
    return pd.DataFrame( { "SecondHighestSalary": [ None if len( employee ) < 2 else sorted( employee, reverse = True )[1] ] } )