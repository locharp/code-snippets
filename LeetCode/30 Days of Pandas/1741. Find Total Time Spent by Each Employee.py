import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.groupby( ["emp_id", "event_day"], as_index = False ).sum()
    employees["out_time"] -= employees["in_time"]
    
    return employees[ [ "event_day", "emp_id", "out_time" ] ].rename( columns = { "event_day": "day", "out_time": "total_time" } )