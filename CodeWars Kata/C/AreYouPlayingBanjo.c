#include <stdlib.h>

char *are_you_playing_banjo(const char *name) {
  char *ret;
  if (name[0] == 'R' || name[0] == 'r') {
    ret = malloc((strlen(name) + 13) * sizeof(char));
    strcpy(ret, name);
    strcat(ret, " plays banjo");
  } else {
    ret = malloc((strlen(name) + 21) * sizeof(char));
    strcpy(ret, name);
    strcat(ret, " does not play banjo");
  }
  
  return ret; // memory will be freed
}

int main() {
  printf("%s\n", are_you_playing_banjo("Ricky"));
}
