#include <stdio.h>
#include <stdlib.h>

char *string_reverse (char *string)
{
  int endIdx = strlen(string) - 1;
  char s[endIdx + 1];

  for (int i = 0; i <= endIdx; i++)
    s[i] = string[endIdx - i];

  string = malloc(sizeof(char) * (endIdx + 2));
  strcpy(string, s);

  return string;
}

int main() {
  char *s = "Hello, world!";
  printf("%s\n", string_reverse(s));
}

