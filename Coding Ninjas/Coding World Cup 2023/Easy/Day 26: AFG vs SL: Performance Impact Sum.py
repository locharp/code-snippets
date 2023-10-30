def divisible3( n: int, x: List[int] ) -> int:
    
    return sum( i if i % 3 == 0 else i * i for i in x )
