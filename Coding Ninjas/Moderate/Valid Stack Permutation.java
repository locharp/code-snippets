import java.util.*;

public class Solution
{

    public static boolean validStackPermutation
    ( ArrayList< Integer > first, ArrayList< Integer > other )
    {
        Stack< Integer > stack =
            new Stack<>();
        Iterator< Integer > itr = first.iterator();

        outter:
        for ( Integer num : other )
        {
            if ( !stack.isEmpty() && stack.peek().equals( num ) )
            {
                stack.pop();
                continue;
            }

            while ( itr.hasNext() )
            {
                Integer next = itr.next();
                
                if ( next.equals( num ) )
                {
                    continue outter;
                }
                else
                {
                    stack.push( next );
                }
            }

            return false;
        }

        return !itr.hasNext() && stack.isEmpty();
    }

}
