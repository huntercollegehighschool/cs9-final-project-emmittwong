import random
import page2
import os

word=str(random.choice(page2.lis))
word_letters = list(word)
print(word)
print("_"*len(word_letters))
blankword="_"*len(word)
word_progress = list(blankword)

total_fails=0
guessed_letters=[]
i=0



while total_fails!=6:
  match=0
  guess=str(input("Enter a letter: ")).lower()#here
  alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  #have you used alphabetlis
  #we need to, look at it, peopel can input multiple. can we fix that with if len(guess) greater than one? try it out
  if guess in alphabet:
    for i in range(len(word)):
      if guess==word_letters[i]:
        word_progress[i]=guess
        match=1
  if guess not in alphabet:
      print("try again, single letters only")
      print ("Attempts remaining: ", 6-total_fails)
   
  os.system('clear')
  
  if match==1 and guess.lower() in guessed_letters:
    print("You've already tried that. Enter another letter")
    print ("Attempts remaining: ", 6-total_fails)
    guessed_letters.remove(guess.lower())
  elif match==1 and guess.lower() not in guessed_letters:
     print ("Attempts remaining: ", 6-total_fails)
  elif match==0 and guess.lower() not in guessed_letters:
    print("That's not in the word")
    total_fails+=1
    print ("Attempts remaining: ", 6-total_fails)
  elif match==0 and guess.lower() in guessed_letters:
    print("You've already tried that. Enter another letter")
    print ("Attempts remaining: ", 6-total_fails)
    guessed_letters.remove(guess.lower())
 
  guessed_letters.append(guess.lower())
  print("Guessed letters: ", guessed_letters)
  if len(guess)>1:
    print("That's not a valid input. Try something else.")

  x=''.join(word_progress)
  print(x)
  z=x.lower()
 
  if z==word.lower():
    print("That's the word!")
    break
if total_fails==6:
  print("That is not the word. The correct word is", word, ". Better luck next time.")


