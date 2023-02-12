#include<stdio.h>
 
int main()
{
   char n, c;
   long double first = 0, second = 1, next;
   printf("Enter the number of terms\n");
   scanf("%i",&n);
 
   printf("First %i terms of Fibonacci series are :-\n",n);
 
   for ( c = 0 ; c < n ; c++ )
   {
      if ( c <= 1 )
         next = c;
      else
      {
         next = first + second;
         first = second;
         second = next;
      }
      printf("%.0Lf\n",next);
   }
 
   return 0;
}
