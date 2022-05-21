import random
import getpass

word_list = ['apples', 'bananas', 'oranges']

print('enter word to be guessed')
word = getpass.getpass('> ')
if word == '':
  word = word_list[random.randint(0, len(word_list) - 1)]
characters = list(word)
show = characters.copy()

for i in range(len(show)):
  if show[i] != ' ':
    show[i] = '_'

lives = 9
won = False
while not won and lives > 0:
  result = ''
  for char in show:
    result += char
  print(f'{result} lives: {lives}')
  print('enter guess')
  guess = input('> ')
  correct = False
  won = True
  for i in range(len(show)):
    if guess in characters[i]:
      correct = True
      show[i] = guess
    if show[i] == '_':
      won = False
  if not correct:
    lives -= 1
if won:
  print('you won! :)')
else:
  print('you lost... :(')
print(f'the word is {word}.')
print('made by martinmimi.')
