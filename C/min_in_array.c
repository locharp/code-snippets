#include <stdio.h>

int min(int *arr, int len) {
  int min = *arr;
  while (--len)
    min = *++arr < min ? *arr : min;
  return min;
}

int main() {
  int arr[] = { 34, -345, -1, 100, -788 };
  printf("%i\n", min(arr, sizeof(arr) / sizeof(arr[0])));
}
