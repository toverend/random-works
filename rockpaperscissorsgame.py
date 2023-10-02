# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 08:45:26 2023

@author: Tom
"Rock Paper Scissors"
"""
import random as ran
# define a two player game, this is part 1 where the names are defined
def game2p1():
    global np1
    np1 = input("Name Player 1: ") # Name for first player
    global np2
    np2 = input("Name Player 2: ") # Name for second player
    game2p2()
# define the main part of the two player game, this allows the function to be looped without entering names each time.
def game2p2():
    # Define potential outcomes of a two player game and the result message
    winmat2p = ["picked rock, it's a draw!", "picked paper, " + str(np2) + " wins!", "picked scissors, " + str(np1) + " wins!","picked rock, " + str(np1) + " wins!", "picked paper, it's a draw!", "picked scissors, " + str(np2) + " wins!","picked rock, " + str(np2) + " wins!", "picked paper, " + str(np1) + " wins!", "picked scissors, it's a draw!"]
    p1 = input(np1 + ", rock, paper or scissors?: ")
    global loopno
    loopno = 1
    fill() # Print text so that the first player's choice can't be seen in the window
    p2 = input(np2 + ", rock, paper or scissors?: ")
    # Convert the players choices into easier to use integers
    p1ind = choices.index(p1) + 1
    p2ind = choices.index(p2) + 1
    global result
    result = int(str(p1ind) + str(p2ind)) # Combine the choices into one, so that it can be indexed in the winmat
    score()
    again = input(np1 + " picked " + p1 + ", " + np2 + " " + winmat2p[winmatind.index(result)] + ", play again? (y/n): ")
    if again == "y":
        print("The score is: " + str(p1score) + " to " + np1 + ", and " + str(p2score) + " to " + np2 + ".")
        game2p2()
    else: # To finish the game, we must print the final scores and winner
        if p1score > p2score: 
           input("The final scores are: " + str(p1score) + " to " + np1 + ", and " + str(p2score) + " to " + np2 +", " + np1 + " Wins!")
        elif p2score > p1score:
           input("The final scores are: " + str(p1score) + " to " + np1 + ", and " + str(p2score) + " to " + np2 +", " + np2 + " Wins!")
        else:
           input("The final scores are: " + str(p1score) + " to " + np1 + ", and " + str(p2score) + " to " + np2 +", it's a draw!")
# define a one player game, the computer simply randomizes it's choice.    
def game1p():
    global p1
    p1 = input("rock, paper or scissors?: ")
    winmat = ["picked rock, it's a draw!","picked paper, you lose!", "picked scissors, you win!","picked rock, you win!","picked paper, it's a draw!", "picked scissors, you lose!","picked rock, you lose!","picked paper, you win!", "picked scissors, it's a draw!"]
    p1ind = choices.index(p1) + 1
    global result
    result = int(str(p1ind) + str(ran.randint(1,3)))
    score()
    again = input("you picked " + p1 + ", I " + winmat[winmatind.index(result)] + ", play again? (y/n): ")
    if again == "y":
        print("The score is: "+ str(p1score) + " to you, " + str(p2score) + " to me!")
        game1p()
    else: # To finish the game, we must print the final scores and winner
        if p1score > p2score: 
           input("The final scores are: " + str(p1score) + " to you, " + str(p2score) + " to me, You won, but I'll get you next time!" )
        elif p2score > p1score:
           input("The final scores are: " + str(p1score) + " to you, " + str(p2score) + " to me, I win! better luck next time!" )
        else:
           input("The final scores are: " + str(p1score) + " to you, " + str(p2score) + " to me, It's a draw!")
#The score functions recalls from the score mat as a pose to using if statements
def score():
    global p1score 
    p1score = p1score + scoremat1[winmatind.index(result)]
    global p2score
    p2score = p2score + scoremat2[winmatind.index(result)]

# create a loop so the second player can't see the first players choice (without scrolling!)   
def fill():
    global loopno
    if loopno < 60:
        print("%%%%%%")
        loopno = loopno + 1
        fill()
# define a basic function to establish the lists used in both singleplayer and multiplayer
def run():
    global winmatind
    winmatind = [11, 12, 13,21, 22, 23,31, 32, 33] # create a list of potential combinations of rock, paper or scissors.
    global scoremat1
    scoremat1 = [0, 0, 1, 1, 0, 0, 0, 1 ,0]
    global scoremat2
    scoremat2 = [0, 1, 0, 0, 0, 1, 1, 0, 0]
    global choices
    choices = ["rock", "paper", "scissors"] # create a list of potential choices, so that the index of each choice can be easily worked with.
    global p1score
    p1score = 0
    global p2score
    p2score = 0
    gametype = int(input("2 or 1 players? (1/2): "))
    if gametype == 2:
       game2p1()
    elif gametype == 1:
       game1p()
    else:
       input("error")
       run() # loop in the event that a number that isn't one or two is used

run() # start the game!