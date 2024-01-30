class Solution
{

    public int evalRPN
    ( String[] tokens )
    {
        Stack<Integer> stack =
            new Stack<>();
        Integer temp;

        for ( String token : tokens )
        {
            switch ( token )
            {
                case "+":
                    stack.push( stack.pop() + stack.pop() );
                    break;
                case "-":
                    temp = stack.pop();
                    stack.push( stack.pop() - temp );
                    break;
                case "*":
                    stack.push( stack.pop() * stack.pop() );
                    break;
                case "/":
                    temp = stack.pop();
                    stack.push( stack.pop() / temp );
                    break;
                default:
                    stack.push( Integer.parseInt( token ) );
            }
        }

        return stack.pop();
    }

}
