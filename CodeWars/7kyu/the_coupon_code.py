MONTHS = { "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12 }

def split_date( date ):
    
    month, day, year = date.split()
    
    return ( int( year ), MONTHS[month], int( day[ : -1 ] ) )
    
    
    
def check_coupon( entered_code, correct_code, current_date, expiration_date ):
    
    return type( entered_code ) == str and split_date( expiration_date ) >= split_date( current_date ) and correct_code == entered_code
