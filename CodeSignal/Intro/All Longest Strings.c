// Arrays are already defined with this interface:
// typedef struct arr_##name {
//   int size;
//   type *arr;
// } arr_##name;
//
// arr_##name alloc_arr_##name(int len) {
//   arr_##name a = {len, len > 0 ? malloc(sizeof(type) * len) : NULL};
//   return a;
// }
//
//
arr_string solution( arr_string inputArray ) {
    int len = 0;
    int count = 0;
    
    for ( int i = 0; i < inputArray.size; i++ )
    {
        int curr = strlen( inputArray.arr[i] );
        if ( curr > len )
        {
            len = curr;
            count = 1;
        }
        else if ( curr == len )
        {
            count++;
        }
    }
    
    arr_string longests = alloc_arr_string( count );
    int idx = 0;
    
    for ( int i = 0; i < inputArray.size; i++ )
    {
        if ( strlen( inputArray.arr[i] ) == len )
        {
            longests.arr[idx++] = inputArray.arr[i];
        }
    }
    
    return longests;
}
