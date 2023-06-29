#include <stdlib.h>

char *double_char (const char *string, char *doubled)
{
  char *d = doubled;
  while (*string) {
    *d++ = *string;
    *d++ = *string++;
  }
  *d = '\0';

  return doubled; // return it
}

int main() {
  char* s1 = "Hello, world!";
  char* s2 = malloc(strlen(s1) * 2 + 1);
  double_char(s1, s2);

  printf("%s\n%s\n", s1, s2);
}
  
  
