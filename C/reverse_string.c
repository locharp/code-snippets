#include <stdio.h>
#include <stdlib.h>

char *strrev (char *string)
{
  int endIdx = strlen(string) - 1;
  char s[endIdx + 1];

  for (int i = 0; i <= endIdx; i++)
    s[i] = string[endIdx - i];

  string = malloc(sizeof(char) * (endIdx + 2));
  strcpy(string, s);

  return string;
}

void reverse_string(char str[]) {
  for (int i = 0, end = strlen(str) - 1; i <= end / 2; i++) {
    char ch = str[i];
    str[i] = str[end - i];
    str[end - i] = ch;
  }
}

int main() {
  char *s = "Hello, world!";
  char *s2 = strrev(s);
  printf("%s\n", strrev(s));
}

