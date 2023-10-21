def liftStruggle( d: int ) -> int:
  
    n, m = divmod( d, 3 )

    return n + m * 2
