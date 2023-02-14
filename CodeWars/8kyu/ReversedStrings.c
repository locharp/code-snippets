// Works for 2 test case on CodeWars
// Doesn't work on my machine
#include <stdio.h>

#include <string.h>
char *reverse_string (char *string)
{
  int endIdx = strlen(string) - 1;
  
  for (int i = 0; i <= endIdx / 2; i++) {
    char ch = string[endIdx - i];
    string[endIdx - i] = string[i];
    string[i] = ch;
  }

  return string; // reverse the string in place and return it
}

int main() {
  char *s = "Hello, world!";
  reverse_string(s);
  printf("%s", s);
}

