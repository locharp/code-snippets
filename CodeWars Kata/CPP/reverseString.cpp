#include <iostream>

std::string reverseString (std::string str )
{
  return std::string(str.rbegin(), str.rend());
}

int main() {
  std::string s = "Hello, world!";
  std::cout << reverseString(s) << '\n';

  return 0;
}

