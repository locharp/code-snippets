#include <stdlib.h>

char *are_you_playing_banjo(const char *name) {
  char *ret;
  asprintf(&ret, "%s%s", name,
	   (name[0] == 'R' || name[0] == 'r')
	   ? " plays banjo"
	   : " does not play banjo");
  return ret;
}

int main() {
  printf("%s\n", are_you_playing_banjo("Ricky"));
}
