def shakeHands( friends, n, k ):
	
	for i in friends:
		if i == k:
			k *= 2

	return k
