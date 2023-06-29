#include <stdio.h>

int double_int( int i )
{
    return i << 1;
}

int main()
{
    printf( "%i\n", double_int( 123 ) );
}
