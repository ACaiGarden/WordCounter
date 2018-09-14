from tkinter import *
from tkinter.filedialog import askopenfilename
from Base_Function import *
from Expansion_a import get_special_num

class Window():
    def __init__(self):
        self.path = ''
        self.func_list = []
        self.Initialization()
        self.count()

    def Initialization(self):
        window = Tk()
        self.file_path = StringVar()

        #self.liss = []
        self.var_list = []
        #self.liss.append('123')

        window.title('WordCounter')
        window.geometry('800x500')
        Label(window, text ='File Path').grid(row=0, column=0)
        Entry(window, textvariable = self.file_path, width=60).grid(row=0, column=1)
        Button(window, text = 'Select File', command=self.select_file).grid(row=0, column=2)

        self.tex = Text(window, heigh = 10)
        self.tex.grid(row = 6, column = 1)


        self.set_check(window)
        #self.set_func(self.var_dict)

        Button(window, text='Count!', command=self.count).grid(row=5, column=1)
        window.mainloop()


    def select_file(self):
        self.path = askopenfilename()
        self.file_path.set(self.path)


    def set_check(self, window):

        global font_var
        font_var = IntVar()
        word_var = IntVar()
        line_var = IntVar()
        special_var = IntVar()
        #self.var_dict= {'line' : line_var,'word' : word_var,'font' : font_var,'special' : special_var}

        l1 = Label(window)
        l1.grid(row = 1, column = 0)
        l2 = Label(window)
        l2.grid(row = 1, column = 1)
        l3 = Label(window)
        l3.grid(row = 2, column = 0)
        l4 = Label(window)
        l4.grid(row = 2, column = 1)

        '''
        def set_func():
            if font_var.get() == 1:
                self.func_list.append('get_font_num(file)')
            if word_var.get() == 1:
                self.func_list.append('get_word_num(file)')
            if line_var.get() == 1:
                self.func_list.append('get_line_num(file)')
            if font_var.get() == 1:
                self.func_list.append('get_font_num(file)')
        '''
        def set_font():
            if font_var.get() == 1:
                l1.config(text = 'font')
                self.func_list.append('get_font_num(file, self.tex)')
            else:
                l1.config(text='no font')
                self.func_list.remove('get_font_num(file, self.tex)')
        def set_word():
            if word_var.get() == 1:
                l2.config(text = 'word')
                self.func_list.append('get_word_num(file, self.tex)')
            else:
                l2.config(text='no word')
                self.func_list.remove('get_word_num(file, self.tex)')
        def set_line():
            if line_var.get() == 1:
                l3.config(text = 'line')
                self.func_list.append('get_line_num(file, self.tex)')
            else:
                l3.config(text='no line')
                self.func_list.remove('get_line_num(file, self.tex)')
        def set_special():
            if special_var.get() == 1:
                l4.config(text = 'spec')
                self.func_list.append('get_special_num(file, self.tex)')
            else:
                l4.config(text='no spec')
                self.func_list.remove('get_special_num(file, self.tex)')

        check_font = Checkbutton(window, text="Font num", variable = font_var, onvalue = 1,
                                 offvalue = 0,command = set_font).grid(row=3, column=0)
        check_word = Checkbutton(window, text="Word num", variable = word_var, onvalue = 1,
                                 offvalue = 0,command = set_word).grid(row=3, column=1)
        check_line = Checkbutton(window, text="Line num", variable = line_var, onvalue = 1,
                                 offvalue = 0,command = set_line).grid(row=4, column=0)
        check_special = Checkbutton(window, text="Special line num", variable = special_var, onvalue = 1,
                                 offvalue = 0,command = set_special).grid(row=4, column=1)


    '''
    def set_func(self, dict):
        if dict['font'].get() == 1:
            self.func_list.append('get_font_num(file)')
        if dict['word'].get() == 1:
            self.func_list.append('get_word_num(file)')
        if dict['line'].get() == 1:
            self.func_list.append('get_line_num(file)')
        if dict['special'].get() == 1:
            self.func_list.append('Expansion_a.get_special_num(file)')
    '''

    def count(self):
        file = self.path
        filepath = str(file + '\n')
        self.tex.insert('insert', filepath)
        for x in self.func_list:
            exec(x)


if __name__ == '__main__':
    w = Window()