def f( i, j ):

	if j is None:
		return i

	if i.val < j.val:
		if i.right is None:
			i.right = j
		else:
			f( i.right, j )
	else:
		if i.left is None:
			i.left = j
		else:
			f( i.left, j )

	return i



def removeNode( root, X ):
	
	if root.val > X:
		root.left = removeNode( root.left, X )
	elif root.val < X:
		root.right = removeNode( root.right, X )
	else:
		if root.left is None:
			return root.right
		else:
			return f( root.left, root.right )
	
	return root
