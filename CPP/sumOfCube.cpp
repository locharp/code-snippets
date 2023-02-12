#include <iostream>

int soc(int n) {
  if (n < 2)
    return n;
  return n*n*n + soc(n - 1);
}

int sumOfCube(int n) {
  return n > 0 ? soc(n) : -soc(-n);
}

int main() {
  int n;
  printf("Input an integer to see the sum of cube from 0 to it: ");
  std::cin >> n;
  printf("%i\n", sumOfCube(n));

  return 0;
}
