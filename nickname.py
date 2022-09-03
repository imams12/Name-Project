## IMAM
from termcolor import colored

# I
thickness = 5
c = 'I'
 
## TOP
for i in range(thickness-3):
  print(colored((c*thickness*2).center(thickness*6), 'cyan'))

## PILLAR
for i in range(thickness+2):
  print(colored((c*thickness+"I").center(thickness*6), 'cyan'))

## BOTTOM
for i in range(thickness-3):
  print(colored((c*thickness*2).center(thickness*6),'cyan'))

print('')
# M
d = 'M'

## TOP
for i in range((thickness+1)//2):
    print(colored((d*(thickness*5-1)).center(thickness*6),'cyan'))  

## BOTTOM
for i in range(thickness+1):
    print(colored((d*(thickness-1)).center(thickness*2)+(d*(thickness-1)).center(thickness*2)+(d*(thickness-1)).center(thickness*2),'cyan'))

print('')
# A
e = 'A'

## TOP
## TOP
for i in range((thickness-1)//2):
    print(colored((e*(thickness*3+1)).center(thickness*6), 'cyan'))

## TOP PILLAR
for i in range(thickness-3):
  print(colored((e*(thickness-1)).center(thickness*2+7)+(e*(thickness-1)).center(thickness*2-2), 'cyan'))

## MIDDLE
for i in range((thickness-1)//2):
  print(colored((e*(thickness*3+1)).center(thickness*6), 'cyan'))

## BOTTOM PILLAR
for i in range(thickness-1):
  print(colored((e*(thickness-1)).center(thickness*2+7)+(e*(thickness-1)).center(thickness*2-2), 'cyan'))

print('')
# M
d = 'M'

## TOP
for i in range((thickness+1)//2):
    print(colored((d*(thickness*5-1)).center(thickness*6),'cyan'))  

## BOTTOM
for i in range(thickness+1):
    print(colored((d*(thickness-1)).center(thickness*2)+(d*(thickness-1)).center(thickness*2)+(d*(thickness-1)).center(thickness*2),'cyan'))
