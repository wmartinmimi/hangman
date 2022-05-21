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
  if len(guess) != 1:
    print('1 letter guess only!')
    continue
  if guess in used or guess in show:
    print('guessed already!')
    continue
  correct = False
  won = True
  for i in range(len(show)):
    if guess.lower() in characters[i].lower():
      correct = True
      show[i] = characters[i]
    if show[i] == '_':
      won = False
  if not correct:
    lives -= 1
    used.append(guess)
    used = sorted(used)

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
