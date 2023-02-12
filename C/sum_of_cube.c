#include <stdio.h>

int soc(int n) {
  n = n * (n + 1) / 2.0;
    return n * n;
}

int sum_of_cube(int n) {
  return n < 0 ? -soc(-n) : soc(n);
}

int main() {
  int n;
  scanf("%i", &n);
  printf("%i\n", sum_of_cube(n));

  return 0;
}
