if __name__ == "__main__":
    n = int( input().strip() )
    print( "Weird" if n % 2 == 1 or n > 5 and n < 21 else "Not Weird" )
