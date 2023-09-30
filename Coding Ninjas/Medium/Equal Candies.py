from statistics import median

def equalCandies( candies, n ):
    m = round( median( candies ) )
    
    return sum( map( lambda x: abs( x - m ), candies ) )
