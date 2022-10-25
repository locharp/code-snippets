#include <stdio.h>

const char* int_to_string(int num) {
    char *s;
    asprintf(&s, "%i", num);
    return s;
}

int main() {
  printf("%s\n", int_to_string(123321));
  printf("%s\n", int_to_string(-123321));
  printf("%s\n", int_to_string(0));
}
