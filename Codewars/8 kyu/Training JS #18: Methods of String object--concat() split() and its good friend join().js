function splitAndMerge( string, separator )
{
    let words = string.split( " " );
    
    for ( let i = 0; i < words.length; i ++ )
    {
        words[i] = words[i].split( "" ).join( separator );
    }
    
    return words.join( " " );
}
