#Color Guess Game
print("Let's Play a Color Guess Game....")
import random
colors=["red","orange","blue","violet","black","brown","white","grey","green","yellow"]
while True:
       mychoise=random.randint(0,9)
       yourguess=input("I'm thinking about one color,Can you guess it??").lower()
       mychoise=colors[mychoise]
       while True:
           if (mychoise==yourguess):
                break
           else:
                yourguess=input("Nope,You are wrong!!Guess Again ") 
       print("Magnificient,I'm thinking about ",mychoise)
       answer=input("Let's Play Again??Type 'no'to quit").lower()
       if answer=='no':
          break
       else:
          print("Let's Start Again")
