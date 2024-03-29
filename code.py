# imports
from asyncio import constants
from calendar import c
import time
import random
#scores
p1p = []
p2p = []
#words
p1w = []
p2w = []
#letters and their values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
cots = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vowles = ["A","E","I","O","U"]
letter_to_points = {key:value for key,value in zip(letters,points)}
letter_to_points[" "] = 0

#returns the score of a word
def score_word(word):
  point_total = 0
  for x in word:
    point_total += letter_to_points.get(x,0)
  return point_total

#introducing players
player_1 = input("Enter your name Player 1: ")
player_2 = input("Now for player two, please enter your name:")

#explaining the game
print("Hello", player_1 +" and ", player_2 + ". You are going to play a game of scrabbel. ")
def answer(question1,ans1,ans2,action1,action2):
    reply = None
    while reply not in (ans1,ans2):
        rules = input(question1)
        if rules == ans1:
            print(action1)
            break
        elif rules == ans2:
            print(action2)
            break
        else:
            print("Please enter", ans1 +" or", ans2)
answer("Would you like to know the rules?(yes or no)","yes","no","There are three rounds. Each round you will be given 7 Random letters and you will have to submit a word. Each letter has a certain amount of points.","No worries, lets move on!")

#timer to start
def countdown(t,message):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print(message)
answer("Are you ready?! (yes or YES)","yes","YES","Lets Go","LETS GO!")
# function call
countdown(5, player_1+" your 1st set of letters are below")
#first set of letters
def gen7():
    sevenl = (random.choices(cots,k=5)) + (random.choices(vowles,k=2))
    print(sevenl)

#round 1 
gen7()
p1_1word = input(player_1+ " enter your first word:")
print(player_2," your first set of letters are below")
gen7()
p2_1word = input(player_2+" enter your first word:")
#storing results 
p1w.append(p1_1word.upper())
p2w.append(p2_1word.upper())
p1p.append(score_word(p1_1word))
p2p.append(score_word(p2_1word))

#round 2 
print("Time for round two!")
countdown(5, player_1+" your second set of letters are below")
gen7()
p1_2word = input(player_1+ " enter your second word:")
print(player_2," your second set of letters are below")
gen7()
p2_2word = input(player_2+" enter your second word:")
#storing results 
p1w.append(p1_2word.upper())
p2w.append(p2_2word.upper())
p1p.append(score_word(p1_2word.upper()))
p2p.append(score_word(p2_2word.upper()))

#round 3 
print("Time for round three!")
countdown(5, player_1+" your third set of letters are below")
gen7()
p1_3word = input(player_1+ " enter your third word:")
print(player_2," your third set of letters are below")
gen7()
p2_3word = input(player_2+" enter your third word:")
#storing results 
p1w.append(p1_3word.upper())
p2w.append(p2_3word.upper())
p1p.append(score_word(p1_3word.upper()))
p2p.append(score_word(p2_3word.upper()))

#totals
t1 = 0
for x in p1p:
    t1 += x
t2= 0
for x in p2p:
    t2 += x

#winner
if t1>t2:
    winner = player_1
elif t2>t1:
    winner = player_2
else:
    winner = "No one, its a draw!"

countdown(3,"The winner is: " +winner)
#results1

reply2 = input("Do you want to see the results?")
if reply2 == "yes":
    words_points1 = {key:value for key,value in zip(p1w,p1p)}
    print(player_1 +" Results:")
    for x,yu in words_points1.items():
        print(x + ":" + str(yu))

    #results2
    words_points2 = {key:value for key,value in zip(p2w,p2p)}
    print(player_2 +" Results:")
    for x,yu in words_points2.items():
        print(x + ":" + str(yu))
else:
    print("No Problem!")
print("Thanks for playing!!!")
