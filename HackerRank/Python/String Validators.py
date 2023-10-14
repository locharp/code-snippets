if __name__ == "__main__":
    s = input()
    
    ans = [
        any( ch.isalnum() for ch in s ),
        any( ch.isalpha() for ch in s ),
        any( ch.isdigit() for ch in s ),
        any( ch.islower() for ch in s ),
        any( ch.isupper() for ch in s )
    ]

    for a in ans:
        print( a )
