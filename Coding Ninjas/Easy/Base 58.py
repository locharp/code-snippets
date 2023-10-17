nums = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def encodeBase58(n):
    
    if n > 57:
        return encodeBase58( n // 58 ) + nums[ n % 58 ]
    else:
        return nums[ n % 58 ]
