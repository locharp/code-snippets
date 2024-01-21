class Solution
{
    
    int f( int n )
    {
        if ( n < 9 )
        {
            return n;
        }
        
        return n + this.f( n - 8 );
    }
    
    
    
    public int minimumPushes( String word ) 
    {
        return this.f( word.length() );
    }
    
}
