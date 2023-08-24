input()

for i in input().split():
    if i == "0":
        print( "0" )
    elif int( i ) % 6 == 0:
        print( "*" * len( i ), end = " " )
    else:
        print( i, end = " " )