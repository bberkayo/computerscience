print "Hello user. You don't know me, but I know you. I want to play a game."
print "To start the game please first select the difficulty you want to play on."
print "Enter 1 for EASY; Enter 2 for MEDIUM; Enter 3 for INSANE."
number=input()
import random

if number==1:
    print "You chose the easy way."  
    num=random.randint(0,10)
if number==2:
    print "Congratulations you are not a coward!"
    num=random.randint(0,50)
if number==3:
    print "It will be like finding a needle in a haystack :)"
    num=random.randint(0,100)

print "Guess a number (Live or Die, make your choice)!" 
guess=input()
print "My number is" , num
if guess==num:
    print "Congratulations, you are still alive. Most people are so ungrateful to be alive... But not you, not anymore."
else:
    print "GAME OVER!!!"
