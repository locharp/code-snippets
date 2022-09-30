#include <stdio.h>

char *are_you_playing_banjo(const char *name) {
  char *ret;
  asprintf(&ret, "%s %s banjo", name,
	   (name[0] == 'R' || name[0] == 'r')
	   ? "plays"
	   : "does not play");
  return ret;
}

int main() {
  printf("%s\n", are_you_playing_banjo("Ricky"));
}
