public class NumArray
{

	int[] arr;



	// Initialize here
	NumArray
	( int[] arr )
	{
		this.arr = arr;
	}



	// Update operation
	public void update
	( int l, int r, int val )
	{
		for ( int i = l - 1; i < r; i++ )
		{
			arr[i] += val++;
		}
	}



	// Return the sum of subarray arr[l..r]
	public long rangeSum
	( int l, int r )
	{
		long ans = 0L;


		for ( int i = l - 1; i < r; i++ )
		{
			ans += arr[i];
		}


		return ans;
	}

}
