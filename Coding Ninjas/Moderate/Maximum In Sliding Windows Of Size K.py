from collections import deque

def slidingWindowMaximum( nums:list, k:int ):
	
	a = deque()
	ans = []
	j = 0

	for i in range( k ):
		while len( a ) > 0 and a[-1][1] <= nums[i]:
			a.pop()

		a.append( ( i, nums[i] ) )

	ans.append( a[0][1] )
	
	for i in range( k, len( nums ) ):
		while len( a ) > 0 and a[-1][1] <= nums[i]:
			a.pop()

		while len( a ) > 0 and a[0][0] <= j:
			a.popleft()

		a.append( ( i, nums[i] ) )
		ans.append( a[0][1] )
		j += 1

	return ans
