from calendar import day_name, weekday

m, d, y = map( int, input().split() )

print( day_name[ weekday( y, m, d ) ].upper() )
