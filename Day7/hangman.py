HANGMANPICS = ['''
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

import random
list_of_words=['apple','book','table']
random_word=random.choice(list_of_words).lower()

lives=6
display=[]
for _ in range(len(random_word)):
    display+="_"   
print(display)

end_of_game= False
while not end_of_game:
    guess=input('enter a letter:').lower()
    for position in range(len(random_word)):
        letter= random_word[position]
        if letter == guess:
            display[position]=letter
    if guess not in random_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print('you lose')
    print(display)
    if "_" not in display:
        end_of_game=True
        print('you win')
        
    print(HANGMANPICS[lives])

        

       


