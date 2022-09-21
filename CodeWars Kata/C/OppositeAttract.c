#include <stdio.h>
#include <stdbool.h>

bool lovefunc(int flower1, int flower2) {
  return (flower1 + flower2) % 2;
}

int main() {
  int n1, n2;
  scanf("%i%i", &n1, &n2);

  if (lovefunc(n1, n2))
    printf("true\n");
}
