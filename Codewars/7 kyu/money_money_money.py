def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += principal * interest * ( 1 - tax )
        years += 1
        
    return years