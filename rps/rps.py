# imports
from tkinter import *
import random
from datetime import datetime

# tkinter window initialization and setup
root = Tk()
root.title("Rock, Paper, Scissors! by Sam Girshovich")
root.geometry("400x400")

# list of options
options = ['rock','paper','scissors']

# general variables
of = ("Arial", 16)
sf = ("Arial", 12)
tf = ("Arial", 10)
bw = 17

# button functions
def rock():
    uchoice = 'rock'
    play(uchoice)

def paper():
    uchoice = 'paper'
    play(uchoice)

def scissors():
    uchoice = 'scissors'
    play(uchoice)

# widgets
title = Label(root, font=of, text="Rock, Paper, Scissors!")

rock = Button(root, text="Rock!", width=bw, borderwidth=5, command=rock)
paper = Button(root, text="Paper!", width=bw, borderwidth=5, command=paper)
scissors = Button(root, text="Scissors!", width=bw, borderwidth=5, command=scissors)

# widget placement
title.place(anchor=CENTER, relx=0.5, rely=0.1)

rock.place(anchor=CENTER, relx=0.17, rely=0.5)
paper.place(anchor=CENTER, relx=0.5, rely=0.5)
scissors.place(anchor=CENTER, relx=0.83, rely=0.5)

#user score and computer score
us = 0
cs = 0

def play(u):
    c = random.choice(options)
    #print("User: "+u+"\nComputer: "+c)
    global us
    global cs
    global wi
    global w


    #if statements for game
    #ties
    if all([u == 'rock', c == 'rock']) or all([u == 'paper', c == 'paper']) or all([u == 'scissors', c == 'scissors']):
        print("It is a tie!")
        x = False

    uw_rules = []
    #user wins
    if all([u == 'rock', c == 'scissors']) or all([u == 'scissors', c == 'paper']) or all([u == 'paper', c == 'rock']):
        print('User Wins!')
        w = 'User'
        us += 1
        wi = 'u'
        x = True

    #computer wins
    if all([u == 'scissors', c == 'rock']) or all([u == 'paper', c == 'scissors']) or all([u == 'rock', c == 'paper']):
        print('Computer Wins')
        w = 'Computer'
        cs += 1
        wi = 'c'
        x = True

    print("User Score: {}\nComputer Score: {}".format(us,cs))

    # who won?
    if x:

        winner = Label(root, font=sf, width=100, text="{} won!".format(w)).place(anchor=CENTER, relx=0.5, rely=0.7)
        if wi == 'u':#if the winner is the user
            hw = Label(root, font=tf, width=100, text="{} beats {}!".format(u,c)).place(anchor=CENTER, relx=0.5, rely=0.8)
        if wi == 'c':
            hw = Label(root, font=tf, width=100, text="{} beats {}!".format(c,u)).place(anchor=CENTER, relx=0.5, rely=0.8)
    else:
        winner = Label(root, font=sf, width=100, text="Tie!").place(anchor=CENTER, relx=0.5, rely=0.7)
        hw = Label(root, font=tf, width=100, text="").place(anchor=CENTER, relx=0.5, rely=0.8)

    #scoreboard
    #score.destroy()
    score = Label(root, font=sf, text="User Score: {} - Computer Score: {}".format(us,cs))
    score.place(anchor=CENTER, relx=0.5, rely=0.9)

# mainloop
root.mainloop()

# datetime object containing current date and time
now = datetime.now()

# mm/dd/YY H:M
dt_string = now.strftime("%m/%d/%Y %H:%M")

# conditionals which check for who won
if cs > us: # if computer score is GREATER than user score
    ww = "Computer Won!"
if cs < us: # if computer score is LESS than user score
    ww = "User Won!"
if cs == us: # if computer score is EQUAL to user score
    ww = "It was a tie!"

# opens txt file
with open("scores\scores.txt", "a+") as f:
    # logs data to text file with is assigned to the variable, "f"
    f.write("\n\nDate and Time: {}\nUser Score: {}\nComputer Score: {}\n{}".format(dt_string,us,cs,ww)) # logs date and time of game to text file
