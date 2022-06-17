
print("Name(s):Riley Kwan and Emmitt Wong")
print("Name of Project: Hangman")


#Write the main part of your program here. Use of the other pages is optional.
import random
import page1
import os

word=str(random.choice(page1.lis))
word_letters = list(word)
print("_"*len(word_letters))
blankword="_"*len(word)
word_progress = list(blankword)

total_fails=0
guessed_letters=[]
alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while total_fails!=6:
  match=0
  guess=str(input("Enter a letter: ")).lower()
  
  for i in range(len(word)):
    if guess==word_letters[i]:
      word_progress[i]=guess
      match=1
  
  os.system('clear')
  if match==1 and guess in guessed_letters:
    print("You've already tried that. Enter another letter")
    print ("Attempts remaining: ", 6-total_fails)
    guessed_letters.remove(guess.lower())
  elif match==1 and guess not in guessed_letters:
      print ("Attempts remaining: ", 6-total_fails)
  elif match==0 and guess.lower() not in guessed_letters:
    print("That's not in the word")
    total_fails+=1
    print ("Attempts remaining: ", 6-total_fails)
  elif match==0 and guess.lower() in guessed_letters:
    print("You've already tried that. Enter another letter")
    print ("Attempts remaining: ", 6-total_fails)
    guessed_letters.remove(guess.lower())
  if total_fails==0:
    print(""""
  +---+
  |   |
      |
      |
      |
      |
=========
""")
  if total_fails==1:
    print(""""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""")
  if total_fails==2:
    print(""""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""")
  if total_fails==3:
    print(""""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""")
  if total_fails==4:
    print(""""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""")
  if total_fails==5:
    print(""""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""")
  if total_fails==6:
    print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

""")
  guessed_letters.append(guess)
  print("Guessed letters: ", guessed_letters)
  if guess not in alphabet:
    print("That's not a valid input. Try something else.")

  x=''.join(word_progress)
  print(x)
 
  if x==word:
    print("That's the word!")
    break
  
if total_fails==6:
  print("That is not the word. The correct word is", word,)
  print("Better luck next time.")

import page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
