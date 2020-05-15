from tkinter import *
import tkinter.messagebox

class ttt(object):
    def __init__(self, tk):
        self.tk = tk
        self.tk.title("Tic-Tac-Toe")

        self.playera = StringVar()
        self.playerb = StringVar()
        self.p1 = StringVar()
        self.p2 = StringVar()

        self.player1_name = Entry(self.tk, textvariable=self.p1, bd=2)
        self.player1_name.grid(row=1, column=1, columnspan=8)
        self.player2_name = Entry(self.tk, textvariable=self.p2, bd=2)
        self.player2_name.grid(row=2, column=1, columnspan=8)

        self.cross = PhotoImage(file = 'cross.png')
        self.zero = PhotoImage(file = 'zero.png')

        self.bclick = True
        self.flag = 0
        self.buttons = StringVar()

        self.label = Label(self.tk, text="Player 1:", font='Comic 15 bold', fg='black', height=1, width=8)
        self.label.grid(row=1, column=0)

        self.label = Label(self.tk, text="Player 2:", font='Comic 15 bold', fg='black', height=1, width=8)
        self.label.grid(row=2, column=0)

        self.button1 = Button(self.tk, text = ' ', font='Times 20 bold', bg='#00bfff',height=4, width=8, command=lambda: self.btnClick(self.button1))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button2))
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.tk, text=' ',font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button3))
        self.button3.grid(row=3, column=2)

        self.button4 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button4))
        self.button4.grid(row=4, column=0)

        self.button5 = Button(self.tk, text=' ', font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button5))
        self.button5.grid(row=4, column=1)

        self.button6 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button6))
        self.button6.grid(row=4, column=2)

        self.button7 = Button(self.tk, text=' ', font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button7))
        self.button7.grid(row=5, column=0)

        self.button8 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button8))
        self.button8.grid(row=5, column=1)

        self.button9 = Button(self.tk, text=' ', font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button9))
        self.button9.grid(row=5, column=2)


    def disableButton(self):
        self.button1.configure(state=DISABLED)
        self.button2.configure(state=DISABLED)
        self.button3.configure(state=DISABLED)
        self.button4.configure(state=DISABLED)
        self.button5.configure(state=DISABLED)
        self.button6.configure(state=DISABLED)
        self.button7.configure(state=DISABLED)
        self.button8.configure(state=DISABLED)
        self.button9.configure(state=DISABLED)

    def btnClick(self, buttons):
        if buttons['text'] == " " and self.bclick == True:
            buttons['image'] = self.zero
            buttons['text'] = 'X'
            buttons['height'] = 141
            buttons['width'] = 131
            self.bclick = False
            self.playerb = self.p2.get() + " Won!"
            self.playera = self.p1.get() + " Won!"
            self.checkForWin()
            self.flag += 1

        elif buttons['text'] == " " and self.bclick == False:
            buttons['image'] = self.cross
            buttons['text'] = 'O'
            buttons['height'] = 141
            buttons['width'] = 131
            self.bclick = True
            self.checkForWin()
            self.flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already clicked!")

    def checkForWin(self):
        if (self.button1['text'] == 'X' and self.button2['text'] == 'X' and self.button3['text'] == 'X' or
            self.button4['text'] == 'X' and self.button5['text'] == 'X' and self.button6['text'] == 'X' or
            self.button7['text'] == 'X' and self.button8['text'] == 'X' and self.button9['text'] == 'X' or
            self.button1['text'] == 'X' and self.button5['text'] == 'X' and self.button9['text'] == 'X' or
            self.button3['text'] == 'X' and self.button5['text'] == 'X' and self.button7['text'] == 'X' or
            self.button1['text'] == 'X' and self.button2['text'] == 'X' and self.button3['text'] == 'X' or
            self.button1['text'] == 'X' and self.button4['text'] == 'X' and self.button7['text'] == 'X' or
            self.button2['text'] == 'X' and self.button5['text'] == 'X' and self.button8['text'] == 'X' or
            self.button7['text'] == 'X' and self.button6['text'] == 'X' and self.button9['text'] == 'X'):
            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.playera)

        elif(self.flag == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")

        elif(self.button1['text'] == 'O' and self.button2['text'] == 'O' and self.button3['text'] == 'O' or
            self.button4['text'] == 'O' and self.button5['text'] == 'O' and self.button6['text'] == 'O' or
            self.button7['text'] == 'O' and self.button8['text'] == 'O' and self.button9['text'] == 'O' or
            self.button1['text'] == 'O' and self.button5['text'] == 'O' and self.button9['text'] == 'O' or
            self.button3['text'] == 'O' and self.button5['text'] == 'O' and self.button7['text'] == 'O' or
            self.button1['text'] == 'O' and self.button2['text'] == 'O' and self.button3['text'] == 'O' or
            self.button1['text'] == 'O' and self.button4['text'] == 'O' and self.button7['text'] == 'O' or
            self.button2['text'] == 'O' and self.button5['text'] == 'O' and self.button8['text'] == 'O' or
            self.button7['text'] == 'O' and self.button6['text'] == 'O' and self.button9['text'] == 'O'):
            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.playerb)
      
def main():
    tk = Tk()
    p = ttt(tk)
    tk.mainloop()