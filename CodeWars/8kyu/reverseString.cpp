#include <string>
using namespace std ; 

string reverseString (string str )
{
  // your Code is Here ... enjoy !!!
  string s = "";
  for (char ch : str)
    s = ch + s;

  return s;
}

int main() {
  std::string s = "Hello, world!";
  std::cout << reverseString(s) << '\n';

  return 0;
}

