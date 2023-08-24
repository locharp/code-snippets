k = int( input().split()[1] )

arr = tuple( map( int, input().split() ) )
ans = "No"

for i in range( len( arr ) - 1 ):
    if ans == "Yes":
        break
        
    for j in arr[ i + 1 : ]:
        if arr[i] + j == k:
            ans = "Yes"
            break
           
print( ans )