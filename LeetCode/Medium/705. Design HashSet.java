class MyHashSet
{
    
    boolean[][] set;
    
    
    
    public MyHashSet()
    {
        this.set = new boolean[1001][1000];
    }
    
    
    
    public void add
    ( int key )
    {
        this.set[ key / 1000 ][ key % 1000 ] = true;
    }
    
    
    
    public void remove
    ( int key )
    {
        this.set[ key / 1000 ][ key % 1000 ] = false;
    }
    
    
    
    public boolean contains
    ( int key )
    {
        return this.set[ key / 1000 ][ key % 1000 ];
    }
    
}
