#include <stdio.h>
#include <stddef.h>

int find_smallest_int(int *vec, size_t len) {
  int smallest = vec[0];
  for (int i = 1; i < len; i++)
    smallest = smallest > vec[i] ? vec[i] : smallest;
  return smallest;
}

int main() {
  int v[] = { 34, -345, -1, 100 };
  printf("%i\n", find_smallest_int(v, 4));
}
