#include <stdio.h>

int soc(int n) {
  if (n < 2)
    return n;
  return n*n*n + soc(n - 1);
}

int sum_of_cube(int n) {
  return n > 0 ? soc(n) : -soc(-n);
}

int main() {
  int n;
  scanf("%i", &n);
  printf("%i\n", sum_of_cube(n));

  return 0;
}
