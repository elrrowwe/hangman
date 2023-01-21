# This is the main file to start the game
# You may add any additional modules and other files you wish
import random
import string 
import PySimpleGUI as sg
import pygame

pygame.mixer.init()
Yeah = pygame.mixer.Sound("Yeah.wav")
Loser = pygame.mixer.Sound("WALTER (mp3cut.net).wav")


key = None
is_game_complete = False 
entered_letters = []
mistakes = []
word_dotted = []
letters = string.ascii_letters
game_start = False
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
O   |
 /|\  |
 / \  |
      | 
=========''']

with open('words.txt', 'r') as file:
  word = list(random.choice(file.readlines()))
  if "\n" in word:
    word.remove("\n")

word = [ch.upper() for ch in word]
text = f'Enter a letter: (Current number of mistakes: {len(mistakes)})' 

for ch in word:
    if ch != ".":
        ch = "."
        word_dotted.append(ch)

font = ('Courier19', 20)
sg.theme('LightBrown2')     ###GUI
layout = [[sg.Text('Welcome to Hangman! Do you now the rules of the game?')],
          [sg.Button('Yes')],
          [sg.Button('No')]]
window = sg.Window('HANGMAN', layout,element_justification='c', font = font  )
while True:
  event, values = window.read()
  if event == 'No':
    window.close()
    layout = [[sg.Text('The point is to guess some random word, which will be dotted out. The rules are as follows:\n1. Enter only one character of the English alphabet at a time.\n2. If the letter is not in the secret word, your mistakes counter (with a limit of 6) will go up.\n With each mistake, a new part of the hangman`s body will be added.\n3. If the hangman`s body is fully assembled, the game is over and you lose!')],
              [sg.Text('Ready to start the game now?:)')],
              [sg.Button('Of course!')]]
    window = sg.Window('HANGMAN', layout, size=(1000, 300), element_justification='c', font=font)
    event, values = window.read()
    if event == 'Of course!':
      game_start = True
      break
    elif event == sg.WIN_CLOSED:
      break
  elif event == 'Yes':
    game_start = True
    break 
  elif event == sg.WIN_CLOSED:
    break 

if game_start == True:
  pygame.mixer.music.play()
  while is_game_complete is False: 
    window.close()
    sg.theme('LightBrown2')
    layout = [[sg.Text(f'{text}')], 
              [sg.Text(f'{hangmanpics[len(mistakes)]}')],
              [sg.Text(f'{word_dotted}')],
              [sg.Text(f'The letters, you`ve already entered:{entered_letters}')],
              [sg.Input(key='IN')],
              [sg.Button('Submit')]]
    window = sg.Window('HANGMAN', layout, element_justification='c',font=font)

    event, values = window.read()       
    user_word = str((values['IN']))
    user_word = user_word.upper()

    if event == 'Submit':
      if len(mistakes) == 6:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(Loser)
        layout = [[sg.Text(f'Game over! You`ve reached the maximum number of mistakes! Maybe, try again?:)')], 
                  [sg.Text(f'{hangmanpics[6]}')],
                  [sg.Text(f'{word}')],
                  [sg.Button('Exit')]]
        window = sg.Window('HANGMAN', layout, element_justification='c',font=font) 
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
          is_game_complete = True
      if user_word in entered_letters:
        text = f'This letter has already been entered! (Current number of mistakes: {len(mistakes)})'
        continue
      if len(user_word) != 1:
        text = f'Please, enter just one character: (Current number of mistakes: {len(mistakes)})' 
        continue
      elif user_word not in letters:
        text = f'Please, enter a letter of the English alphabet: (Current number of mistakes: {len(mistakes)})'
        continue
      elif user_word not in word:
        mistakes.append(user_word)
        text = f'You`ve made a mistake! Please, try again: (Current number of mistakes: {len(mistakes)})'
        entered_letters.append(user_word)

        continue
      elif user_word in word:
        text = f'Enter a letter: (Current number of mistakes: {len(mistakes)})' 
        entered_letters.append(user_word)
      for ind, val in enumerate(word):
        if val == user_word:
          word_dotted[ind] = user_word
    elif event == sg.WIN_CLOSED:
      break 

    if word_dotted == word:
      window.close()
      is_game_complete = True
      pygame.mixer.music.stop()
      pygame.mixer.Sound.play(Yeah)
      layout = [[sg.Text(f'Congratulations, you guessed the word correctly! Total number of mistakes: {len(mistakes)}.')], 
                [sg.Text(f'{hangmanpics[len(mistakes)]}')],
                [sg.Text(f'{word_dotted}')],
                [sg.Button('Exit')]]
      window = sg.Window('HANGMAN', layout, element_justification='c', font=font)
      event, values = window.read()
      if event == 'Exit' or event == sg.WIN_CLOSED:
        window.close()
        is_game_complete = True 
        game_start = False




    
###TERMINAL 

        
#         while True:                             
#             event, values = window.read()       
#             user_word = layout[3]
#             if len(mistakes) == 6:
#               layout[0] = "Game over! You've reached the maximum limit of mistakes!" 
#               is_game_complete = True
#             if user_word in entered_letters:
#               layout[0] = f"This letter has already been entered! (Current number of mistakes: {len(mistakes)})"
#               continue 


        
        # print(hangmanpics[len(mistakes)]) 
        # print(word_dotted) 
        # user_word = input(f"Enter a character: (Current number of mistakes: {len(mistakes)})")
        # user_word = user_word.upper()

        # if len(mistakes) == 6:
        #   print("Game over! You've reached the maximum limit of mistakes!") 
        #   is_game_complete = True
        # if user_word in entered_letters:
        #   print(f"This letter has already been entered! (Current number of mistakes: {len(mistakes)})")
        #   continue 
        # entered_letters.append(user_word)

        # if len(user_word) != 1:
        #   print("Please, enter one character:")
        #   user_word = input(f"Enter a character: (Current number of mistakes: {len(mistakes)})")
        # elif user_word not in letters:
        #   print("Please, enter a letter of the English alphabet:")
        #   user_word = input(f"Enter a character: (Current number of mistakes: {len(mistakes)})")
        # elif user_word not in word:
        #   mistakes.append(user_word)
        #   probs += 1
        #   print(f'You made a mistake! Please, try again. (Current number of mistakes: {len(mistakes)})')
        

        # for ind, val in enumerate(word):
        #   if val == user_word:
        #     word_dotted[ind] = user_word

        
        # if word_dotted == word:
        #   print(word_dotted)
        #   print(f"Congratulations! You've guessed the word! Total number of mistakes: {len(mistakes)}")
        #   is_game_complete = True

       

        



          
        
      
         

    
        
    


          
        
      
         

    
        
    
                        







