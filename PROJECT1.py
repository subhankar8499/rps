 # we imported two libraries into our code, which are tkinter and random
import tkinter as tk
import random

#let's create a window for our game, and name it as Rock Paper Scissors Game
window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

#Next, we are going to define global variables that we are going to use in our program.
#We have four of them for storing the user's score, computer's score, user's choice, and computer's choice
#Initially, we set the computer's score and the user's score into zero
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

#then we are going to define two methods for converting the user's choice to a number and vice versa
def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps = {0:'rock',1:'paper',2:'scissor'}
    return rps[number]

#now let's create a function to get the computer's choice
#we use the random library here. The computer selects a random choice from either rock,paper and scissors
def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

# it's the result function, that determines the winner
#this function evaluates both user's and compueter's choices, and based on the comparisons, it picks a winner and updates the scores

# also let's create a text area for displaying the current choices and current scores of both the user and the computer
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        USER_SCORE+=1
    else:
        print("Comp wins")
        COMP_SCORE+=1

    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \n Computer's Choice: {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END,answer)

# then we are going to define three methods for three different user choices.
# These methods take the user's choice, generate a computer's random choice,and pass them into the result function,which we created previously
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissor'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

# now let's build three buttons so that the user can click them to play the game
button1 = tk.Button(text="\t Rock \t",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="\t Paper \t",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="\t Scissor \t",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)

#finally,let's run everything inside the window using the mainloop() method
window.mainloop()
