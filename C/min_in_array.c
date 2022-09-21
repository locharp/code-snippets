#include <stdio.h>

int min(int *arr, int len) {
  int min = arr[--len];
  while (len--)
    min = arr[len] < min ? arr[len] : min;
  return min;
}

int main() {
  int arr[] = { 34, -345, -1, 100 };
  printf("%i\n", min(arr, sizeof(arr) / sizeof(arr[0])));
}
