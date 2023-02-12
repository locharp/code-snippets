// https://gcc.gnu.org/onlinedocs/cpp/Standard-Predefined-Macros.html
// https://gcc.gnu.org/onlinedocs/cpp/Standard-Predefined-Macros.html
#include <stdio.h>

int main() {
  printf("Current function: %s\n", __func__);
  printf("System Date: %s\n", __DATE__);
  printf("System Time: %s\n", __TIME__);
  printf("Line number of this statement: %i\n", __LINE__);
  printf("Name of current input file: %s\n", __FILE__);
  printf("Conforms to ISO standard C: %i\n", __STDC__);
  printf("Version of standard C: %li\n", __STDC_VERSION__);
  printf("Is hosted: %i\n", __STDC_HOSTED__);
  // printf("C++ compiler version: %li\n", __cplusplus);
  // printf("Is Objective C compiler: %i\n", __OBJC__);
  // printf("Is processing assembly language": %i\n", __ASSEMBLER__);
}