import pandas
import random
import tkinter
import sys

# Fugly GUI for a random generated password for files
# so I don't have to think about it. 

class StdRedirector():
    def __init__(self, text_widget):
        self.text_space = text_widget
        

    def write(self, string):
        self.text_space.config(state=tkinter.NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=tkinter.DISABLED)

class theGUI():
    def __init__(self, parent):

        text_box = tkinter.Text(parent, state=tkinter.DISABLED)
        infotxt = tkinter.Label(parent, text='Get a new password?')
        text_box.pack()
        infotxt.pack()

        sys.stdout = StdRedirector(text_box)
        sys.stderr = StdRedirector(text_box)

        output_button = tkinter.Button(parent, text='Yes', command=self.main)
        exit_button = tkinter.Button(parent, text='Exit', command=self.goodbye)

        output_button.pack()
        exit_button.pack()


    def main(self):
        # Random selection of cells from the CSV file
        cols = ['colour', 'name', 'regnu', 'regtx']
        df = pandas.read_csv('randomList.csv', names=cols)

        colour = df.colour.tolist()
        name = df.name.tolist()
        regnu = df.regnu.tolist()
        regtx = df.regtx.tolist()

        secure = random.SystemRandom() # Cryptosecure

        print (secure.choice(colour)+secure.choice(name)+secure.choice(regnu)+secure.choice(regtx))


    def goodbye(self):
        root.destroy()
        

root = tkinter.Tk()
root.title('Random Secure Pass Generator')
theGUI(root)
root.mainloop()
