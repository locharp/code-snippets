def coinGame(x: int, y: int) -> int:
    return min( x // 3, y ) % 2
