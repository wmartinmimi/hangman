import random
import getpass

# images
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

# some default words
word_list = ['apples', 'bananas', 'oranges']

# word prompt
print('enter word to be guessed')
print('empty for online random word')
word = getpass.getpass('> ')
if word == '':
  print('using online service...')
  print('service at https://random-word-api.herokuapp.com/word')
  print('released under DWTFYW license')
  print('homepage for service: https://random-word-api.herokuapp.com/home')
  print('*DISCAMER: I do not own the service.*')
  import requests
  response = requests.get('https://random-word-api.herokuapp.com/word')
  if response.status_code == 200:
    word = response.json()[0]
  else:
    print('failed to connect to service.')
    print('using default list')
    word = word_list[random.randint(0, len(word_list) - 1)]


# game setup
characters = list(word)
show = characters.copy()
used = []

for i in range(len(show)):
  if show[i] != ' ':
    show[i] = '_'

# game logic
lives = 9
won = False
while not won and lives > 0:
  # output hangman image
  print(hangman[lives])
  result = ''
  for char in show:
    result += char
  print(f'{result} lives: {lives}')

  # output used characters
  result = ''
  for char in used:
    result += char + ' '
  print(result)

  # prompt for guess
  print('enter guess')
  guess = input('> ')

  if len(guess) != 1:
    print('1 letter guess only!')
    continue
  if guess in used or guess in show:
    print('guessed already!')
    continue

  # guess logic
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

# ui
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

# credits
print('made by martinmimi.')
