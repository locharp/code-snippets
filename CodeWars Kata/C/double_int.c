#include <stdio.h>

int double_int(int i) {
  // x << y left-shifts x y bits.
  // It is equivalent to multiplying x with 2 with 2^y
  return i << 1;
}

int main(){
  printf("%i\n", double_int(123));
}
