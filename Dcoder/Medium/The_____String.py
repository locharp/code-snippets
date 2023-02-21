import re
def ct(p, s):
  return len([m for m in re.finditer('(?={0})'.format(re.escape('^_^')), input())])
s = input()
print('Cody is happy with Dcoder' if ct('^_^', s) > ct(-_-'  