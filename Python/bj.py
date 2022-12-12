from random import randint as rd

n=('Banker','You')
hs=('Banker has','You have')
f=['J','Q','K']
vs=['A',2,3,4,5,6,7,8,9,10]+f

def t():
 if len(h[p])==2 and(h[p][0]=='A'and h[p][1]in f or h[p][0]in f and h[p][1]=='A'):
  return -1
 v,a=0,0
 for c in h[p]:
  if c=='A':
   v+=1;a=1
  elif c in f:
   v+=10
  else:
   v+=int(c)
 if v<12 and a:
  v+=10
 return v

def m():
 h[p].append(d.pop(rd(0,len(d)-1)))
 print(f'{n[p]} got a {h[p][-1]}.')
 if t()==-1:
  print(hs[p],'Black Jack!')
 elif t()>21:
  print(n[p],'busted')
 else:
  print(f'{hs[p]} {t()}.')

while input('\nNew game?(y/n)').lower()=='y':
 d=vs*4;h=[[],[]]
 p=0
 m()
 p=1
 h[1].append(d.pop(rd(0,len(d)-1)))
 print(f'{n[p]} got a {h[p][-1]}.')
 m()
 while t()in range(21)and input('More?(y/n)').lower()=='y':
  m()
 p=0
 while t()in range(16):
  m()
 p0=t();p=1;p1=t()
 if p0==-1 and p1!=-1 or p0<22 and(p1>21 or p1<p0 and p1!=-1):
  r='Loss!'
 elif p0==p1 or p0>21 and p1>21:
  r='Draw!'
 else:
  r='Win!'
 print(r)
