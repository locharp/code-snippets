from sortedcontainers import *

class FoodRatings:

    def __init__( self, foods: List[str], cuisines: List[str], ratings: List[int] ):

        self.foods = {}
        self.cuisines = defaultdict( SortedDict )

        for i in range( len( foods ) ):
            self.foods[ foods[i] ] = [ cuisines[i], ratings[i] ]
            
            if ratings[i] not in self.cuisines[ cuisines[i] ]:
                self.cuisines[ cuisines[i] ][ ratings[i] ] = SortedSet()

            self.cuisines[ cuisines[i] ][ ratings[i] ].add( foods[i] )



    def changeRating( self, food: str, newRating: int ) -> None:

        cuisine, rating = self.foods[food]
        self.foods[food][1] = newRating

        if len( self.cuisines[cuisine][rating] ) < 2:
            del self.cuisines[cuisine][rating]
        else:
            self.cuisines[cuisine][rating].remove( food )

        if newRating not in self.cuisines[cuisine]:
            self.cuisines[cuisine][newRating] = SortedSet()
        
        self.cuisines[cuisine][newRating].add( food )
        
        

    def highestRated( self, cuisine: str ) -> str:
        
        rating, foods = self.cuisines[cuisine].peekitem( -1 )

        return self.cuisines[cuisine][rating][0]
