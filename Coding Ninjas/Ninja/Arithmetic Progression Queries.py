class NumArray:
	
	def __init__( self,arr ):
  
		self.arr = arr



	def update( self, l, r, val ):

		for i in range( r - l + 1 ):
			self.arr[ i + l - 1 ] += i + val



	def rangeSum( self, l, r ):

		return sum( self.arr[ l - 1 : r ] )
