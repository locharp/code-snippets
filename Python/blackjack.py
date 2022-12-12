from random import randint as rd

name=('Banker','You')
has=('Banker has','You have')
faces=('J','Q','K')
values=('A',2,3,4,5,6,7,8,9,10)+faces

def pts(p):
  if len(hand[p]) == 2 and (hand[p][0][2:] == 'A' and hand[p][1][2:] in faces or hand[p][0][2:] in faces and hand[p][1][2:] == 'A'):
    return -1
  points, a = 0, 0
  for card in hand[p]:
    if card[2:] == 'A':
      a = 1
      points += 1
    elif card[2:] in faces:
      points += 10
    else:
      points += int(card[2:])
  if points < 12 and a:
    points += 10
  return points

def deal():
  hand[p].append(deck.pop(rd(0,len(deck)-1)))
  print(f'{name[p]} got a {hand[p][-1]}.')
  if pts(p) == -1:
    print(has[p],'Black Jack!')
  elif pts(p)>21:
    print(name[p],'busted')
  else:
    print(f'{has[p]} {pts(p)}.')

while input('\nNew game? (y/n) ').lower() == 'y':
  deck = ['♠️'+str(i) for i in values] + ['♥️'+str(i) for i in values] + ['♣️'+str(i) for i in values] + ['♦️'+str(i) for i in values]
  hand = [[],[]]
  p = 0
  deal()
  p = 1
  hand[1].append(deck.pop(rd(0,len(deck)-1)))
  print(f'{name[p]} got a {hand[p][-1]}.')
  deal()
  while pts(1) < 21 and input('Would you like another card? (y/n) ').lower() == 'y':
    deal()
  p=0
  while pts(0) < 16 and pts(0) != -1:
    deal()
  p0, p1 = pts(0), pts(1)
  if p0 == -1 and p1 != -1 or p0 < 22 and (p1 > 21 or p1 < p0 and p1 != -1):
    print('You lost!')
  elif p0 == p1 or p0 > 21 and p1 > 21:
    print('Draw game!')
  else:
    print('You won!')
