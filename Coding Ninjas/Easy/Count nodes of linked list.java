public class Solution
{
    
    public static int length
    ( Node head )
    {
        return length( head, 0 );
    }
    
    
    
    static int length
    ( Node head, int len )
    {
        if ( head == null )
        {
            return len;
        }
        
        return length( head.next, len + 1);
    }
    
}
