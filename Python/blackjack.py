from random import shuffle as sf

name = ('Banker','You')
has = ('Banker has','You have')
faces = ('J','Q','K')
 
def pts():
  if len(hand[p]) == 2 and (hand[p][0][2:] == 'A' and hand[p][1][2:] in faces or hand[p][0][2:] in faces and hand[p][1][2:] == 'A'):
    return 31
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
  return points if points < 22 else -1

def deal():
  card=deck.pop()
  hand[p]+=[card]
  print(f"{name[p]} got {'an' if card[2:] == 'A' else 'a'} {card}.")
  
def more():
  deal()
  if pts() > 30:
    print(has[p],'Black Jack!')
  elif pts() < 0:
    print(name[p],'busted!')
  else:
    print(f'{has[p]} {pts()}.')
 
while input('\nNew game? (y/n) ').lower() == 'y':
  deck = [s+str(v) for v in ('A',2,3,4,5,6,7,8,9,10)+faces for s in ('♠️','♥️','♠️','♦️')]
  sf(deck)
  hand = [[],[]]
  p = 0; more()
  p = 1; deal(); more()
  while pts() in range(21) and input('Would you like another card? (y/n) ').lower() == 'y':
    more()
  p = 0
  while pts() in range(16):
    more()
  p0 = pts(); p = 1; p1 = pts()
  if p0 > p1:
    print('You lost!')
  elif p1 > p0:
    print('You won!')
  else:
    print('Draw game!')
