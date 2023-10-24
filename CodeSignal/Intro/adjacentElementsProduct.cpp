int solution( vector<int> inputArray )
{
    int max = inputArray.back();
    inputArray.pop_back();
    int i = inputArray.back();
    inputArray.pop_back();
    max = max * i;
    
    while ( inputArray.size() > 0 )
    {
        int j = inputArray.back();
        inputArray.pop_back();
        int p = i * j;
        
        if ( max < p )
        {
            max = p;
        }
        
        i = j;
    }
    
    return max;
}
