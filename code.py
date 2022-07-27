from cgitb import text
from faulthandler import disable
from tabnanny import check
from tkinter import *
import tkinter.messagebox 
root = Tk()
root.title('Tic Tac Toe')
playerA = StringVar()
playerB = StringVar()
player1 = Entry(root,textvariable = playerA)
player2 = Entry(root,textvariable = playerB)
player1.grid(row=1,column=1)
player2.grid(row=2,column=1)
bclck = True
flag = 1
def descideturn(b):
    global bclck,flag
    if(bclck == True and b['text'] == ' '):
        b['text'] = 'O'
        checkwhen()
        bclck = False
        flag = flag + 1
    if(bclck == False and b['text'] == ' '):
        b['text'] = 'X'
        checkwhen()
        bclck = True
        flag = flag + 1

def disablefunction():
    button1.configure(state = DISABLED)
    button2.configure(state = DISABLED)
    button3.configure(state = DISABLED)
    button4.configure(state = DISABLED)
    button5.configure(state = DISABLED)
    button6.configure(state = DISABLED)
    button7.configure(state = DISABLED)
    button8.configure(state = DISABLED)
    button9.configure(state = DISABLED) 

def checkwhen():
    if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or 
       button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
       button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
       button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
       button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
       button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
       button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
       button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
            disablefunction()
            tkinter.messagebox.showinfo('Tic-Tac-Toe',playerA.get()+' won the game')
    if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
       button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'or
       button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'or
       button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'or
       button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'or
       button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'or
       button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'or
       button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
            disablefunction()
            tkinter.messagebox.showinfo('Tic-Tac-Toe', playerB.get()+' won the game')
    if( flag == 9):
        disablefunction()
        tkinter.messagebox.showinfo('Tic-Tac-Toe', ' it is a tie')

label1 = Label(root,text = 'Player 1',font = 'Times 20 bold',bg = 'white',fg = 'black', height = 1, width = 8)
label1.grid(row=1,column=0)
label2 = Label(root,text = 'Player 2',font = 'Times 20 bold',bg = 'white',fg = 'black', height = 1, width = 8 )
label2.grid(row=2,column=0)

button1 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button1))
button1.grid(row=3,column = 0)

button2 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button2))
button2.grid(row=3,column = 1)

button3 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button3))
button3.grid(row=3,column = 2)

button4 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button4))
button4.grid(row=4,column = 0)

button5 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button5))
button5.grid(row=4,column = 1)

button6 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button6))
button6.grid(row=4,column = 2)

button7 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button7))
button7.grid(row=5,column = 0)

button8 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button8))
button8.grid(row=5,column = 1)

button9 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button9))
button9.grid(row=5,column = 2)
root.mainloop()