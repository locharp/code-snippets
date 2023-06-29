#include <stdlib.h>

char *number_to_string( int number )
{
    int len = 1, worker = number;
    while ( worker / 10 != 0 )
    {
        len++;
        worker /= 10;
    }

    if ( number < 0 )
        len++;

    char *ret = calloc(len, sizeof(char));

    if ( number < 0
    {
        ret[0] = '-';
        number *= -1;
    }

    do
    {
        ret[--len] = '0' + number % 10;
        number /= 10;
    } while ( number != 0 );

    return ret;
}