from tkinter import *
from tkinter.filedialog import askopenfilename

class Window():
    def __init__(self):
        pass


def Initialization():
    window = Tk()

    global file_path
    file_path = StringVar()
    window.title('WordCounter')
    window.geometry('800x500')
    Label(window, text = 'File Path:').grid(row=0, column=0)
    Entry(window, textvariable = file_path, width=60).grid(row=0, column=1)
    Button(window, text='Select File', command=select_file).grid(row=0, column=2)

    window.mainloop()

def select_file():
    path = askopenfilename()
    file_path.set(path)

if __name__ == '__main__' :
    Initialization()