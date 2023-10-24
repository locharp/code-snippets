( defn solution [n]
    ( loop [ area 1 i ( - n 1 ) ]
    	( if ( > i 0 ) 
			( recur
                ( + area ( * 4 i ) )
        	    ( dec i )
            )
            area
        ) 
    )
)
