#include <iostream>
#include <vector>

std::string longestString (std::vector<std::string> strarr) {
  int longest = 0;
  for (int i = 1; i < strarr.size(); i++)
    if (strarr[i].length() > strarr[longest].length())
      longest = i;

  return strarr[longest];
}

int main() {
  const std::vector<std::string> strarr = {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};

  std::cout << longestString(strarr) << '\n';

  return 0;
}
