def rental_car_cost( d ):
    ans = d * 40
    
    if d > 6:
        ans -= 50
    elif d > 2:
        ans -= 20
        
    return ans
