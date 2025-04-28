import random

a = input('Enter your choice: ')

op = ['scissor', 'stone', 'paper']
print('User:', a)
b = random.choice(op)
print('Computer:', b)

if (a == 'scissor' and b == 'scissor') or (a == 'stone' and b == 'stone') or (a == 'paper' and b == 'paper'):
    print('Tie')
elif (a == 'stone' and b == 'scissor') or (a == 'paper' and b == 'stone') or (a == 'scissor' and b == 'paper'):
    print('User wins')
elif (b == 'stone' and a == 'scissor') or (b == 'paper' and a == 'stone') or (b == 'scissor' and a == 'paper'):
    print('Computer wins')
else:
    print('Invalid input!')