#include<stdio.h>

long double fib(int n) {
  long double p = 0, q = 1;
  if (n == 0)
    return 0;
  else if (n > 0) {
    for (int i = 1; i < n; i++) {
      q += p;
      p = q - p;
    }
    return q;
  } else
    for (int i = n; i < -1; i++) {
      p = q - p;
      q -= p;
    }
  return q - p;
}
    

int main()
{
  int m, n;
  //long double first = 0, second = 1, next;
  printf("Enter the lower range of the Fibonacci series: ");
  scanf("%i",&m);
  printf("Enter the higher range of the Fibonacci series: ");
  scanf("%i",&n);
 
  printf("The Fibonacci series between %i and %i are:\n", m, n);
 
  for (; m <= n ; m++)
    printf("%.0Lf\n",fib(m));

  return 0;
}
