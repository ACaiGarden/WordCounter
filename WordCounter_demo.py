import sys,getopt
import re
import Expansion_s

class WordCounter():
    def __init__(self):
        self.File_path = []
        self.func_list = []
        self.get_info()
        self.count()

    def get_info(self):
        try:
            option, arg = getopt.getopt(sys.argv[1:],"scwl",["Count_fonts"])

            for opt, args in option:
                #If the commend includes '-s',get all file with the special suffix.
                if opt in ('-s') and arg:
                    self.File_path = Expansion_s.get_all_file(arg[0])

                #If not,let the arg as the file name which would be counted.
                else :
                    if arg:
                        self.File_path.append(arg[0])
                        print(arg[0])
                    else:
                        print("缺乏文件路径")
        except getopt.error as e:
            print(e)

        for opt,arg in option:
            if opt in ('-s'):
                pass
            if opt in ('-c','--Count_Fonts'):
                self.func_list.append('self.get_font_num()')
            if opt in ('-w', '--Count_Words'):
                self.func_list.append('self.get_word_num()')
            if opt in ('-l', '--Count_Lines'):
                self.func_list.append('self.get_line_num()')

    def count(self):
        print(self.func_list)
        for func in self.func_list:
            exec(func)

    def get_line_num(self):
        try:
            for file in self.File_path:
                print(file)
                with open(file) as f:
                    line_num = 0
                    for line in f:
                        line_num += 1
                print("Line Number:", line_num)
        except:
            print("打开文件失败")

    def get_word_num(self):
        try:
            for file in self.File_path:
                print(file)
                with open(file) as f:
                    word_num = 0

                    for line in f:
                        word_of_line = line.split()
                        word_num += len(word_of_line)
                print("Word Number:", word_num)
        except:
            print("打开文件失败")

    def get_font_num(self):
        try:
            for file in self.File_path:
                print(file)
                with open(file) as f:
                    font_num = 0
                    font_num2 =0
                    for line in f:
                        font_num += len(line)
                        font_num2 += len(line) - line.count(' ')
                print("Font Number(Include space):",font_num)

                print("Font Number(No space):", font_num2)
        except:
            print("打开文件失败")

if __name__ == '__main__':
    Myclass = WordCounter()
    Expansion_s.get_all_file('*.c')
