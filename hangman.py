import random
import getpass

hangman = [
  """
  ----
  |  o
  | /|\\
  | / \\
  -----
  """,
  """
  ----
  |  o
  | /|\\
  | /
  -----
  """,
  """
  ----
  |  o
  | /|\\
  |
  -----
  """,
  """
  ----
  |  o
  | /|
  |
  -----
  """,
  """
  ----
  |  o
  |  |
  |
  -----
  """,
  """
  ----
  |  o
  |
  |
  -----
  """,
  """
  ----
  |
  |
  |
  -----
  """,
  """
  
  |
  |
  |
  -----
  """,
  """
  
  
  
  
  -----
  """,
  """
  
  
  
  
  
  """
]

word_list = ['apples', 'bananas', 'oranges']

print('enter word to be guessed')
word = getpass.getpass('> ')
if word == '':
  word = word_list[random.randint(0, len(word_list) - 1)]
characters = list(word)
show = characters.copy()
used = []

for i in range(len(show)):
  if show[i] != ' ':
    show[i] = '_'

lives = 9
won = False
while not won and lives > 0:
  print(hangman[lives])
  result = ''
  for char in show:
    result += char
  print(f'{result} lives: {lives}')
  result = ''
  for char in used:
    result += char + ' '
  print(result)
  print('enter guess')
  guess = input('> ')
  if guess == '':
    continue
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
    used.append(guess)

print()
if won:
  print('congraduations,')
  print('you won! :)')
else:
  print('oh no,')
  print('you lost... :(')
print(hangman[lives])
print(f'incorrect guesses: {len(used)}')
print(f'the word is {word}.')
print('made by martinmimi.')
