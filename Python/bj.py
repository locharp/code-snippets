from random import randint as rd

n=('Banker','You')
s=('Banker has','You have')
f=['J','Q','K']

def t():
 if len(h[p])==2 and'A'in h[p][:2]and(h[p][0]in f or h[p][1]in f):
  return 31
 t,a=0,0
 for c in h[p]:
  if c=='A':
   t+=10
  else:
   t+=int(c)
 if t<12 and a:
  t+=10
 return t if t<22 else -1

def r():
 h[p]+=[c:=d.pop(rd(0,len(d)-1))]
 print(f"{n[p]} got {'an'if c=='A'else'a'} {c}.")
 
def m():
 r()
 print(f'{s[p]} Black Jack!'if t()>30 else f'{n[p]} busted!'if t()<0 else f'{s[p]} {t()}.')

while input('\nNew game?(y)').lower()=='y':
 d=['A',2,3,4,5,6,7,8,9,10]*4;h=[[],[]]
 p=0;m()
 p=1;r();m()
 while t()in range(21)and input('More?(y)').lower()=='y':
  m()
 p=0
 while t()in range(16):
  m()
 b=t();p=1;a=t()
 print('Loss'if b>a else'Win'if a>b else'Draw')
