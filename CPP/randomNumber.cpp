#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main ()
{
  srand (time(NULL));
  for (int i = 0; i < 9; i++)
    printf("%i\n", rand());
  return 0;
}