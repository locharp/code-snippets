class MyQueue
{
    
    Stack<Integer> stack;
    
    
    
    public MyQueue()
    {
        this.stack = new Stack<Integer>();
    }
    
    
    
    public void push( int x )
    {
        Stack<Integer> stack = new Stack<>();
        
        while( !this.stack.isEmpty() )
        {
            stack.push( this.stack.pop() );
        }
        
        this.stack.push( x );
        
        while ( !stack.isEmpty() )
        {
            this.stack.push( stack.pop() );
        }
    }
    
    
    
    public int pop()
    {
        return this.stack.pop();
    }
    
    
    
    public int peek()
    {
        return this.stack.peek();
    }
    
    
    
    public boolean empty()
    {
        return this.stack.isEmpty();
    }
    
}
