#include <stdlib.h>
#include <stdio.h>

char *string_trim_spaces(const char *str_in) {
  char *s = malloc((strlen(str_in) + 1) * sizeof(char));
  int j = 0;
  
  for (int i = 0; i < strlen(str_in); i++)
    if (str_in[i] != ' ')
      s[j++] = str_in[i];
  
  s[j] = '\0';
  return s;
}

int main() {
  char *s = "Hello, world";
  printf("%s\n", string_trim_spaces(s));
}
