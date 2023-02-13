#include <stdio.h>

int main()
{
  int a, b, p, q, x;
  scanf("%d%d%d%d%d", &a, &b, &p, &q,  &x); 
  printf("%d\n%d\n%d\n%d\n%d\n%d", a&b, a|b, a^b, p<<q, p>>q,~x);
}