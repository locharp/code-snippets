#include <stdio.h>

int past(int h, int m, int s) {
  return ((h * 60 + m) * 60 + s) * 1000;
}

int main() {
  printf("%i\n", past(8, 37, 28));
}
