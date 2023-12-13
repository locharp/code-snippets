from functools import cache

def crossRiver( safe ):
	
	if safe[1] != safe[0] + 1:
		return False

	n = len( safe )

	@cache
	def f( i, x ):

		if i + 1 == n:
			return True
		
		p = safe[i] + x - 2
		q = safe[i] + x + 2

		for j in range( i + 1, n ):
			if safe[j] > p and safe[j] < q:
				if f( j, safe[j] - safe[i] ):
					return True
			elif safe[j] > safe[i] + x + 1:
				return False



		return False



	return f( 1, 1 )
