#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* remove_char(char* dst, const char* src)
{
    for (int i = 1; i < strlen(src) - 1; i++)
      dst[i-1] = src[i];
    dst[strlen(src)-2] = '\0';
    return dst;
}

int main() {
  char *s1 = "Hello, world!";
  char *s2 = malloc(strlen(s1) * sizeof(char) - 1);
  printf("%s\n", remove_char(s2, s1));
  printf("%s\n", s2);
}