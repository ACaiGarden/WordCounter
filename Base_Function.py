def get_line_num(file, aim = None):
    try:
        # print(file)
        with open(file) as f:
            line_num = 0
            for line in f:
                line_num += 1
        strl = ("Line Number:" , line_num , '\n')
        print("Line Number:" , line_num )
        if aim:
            aim.insert('insert', strl)
    except:
        print("Open false")


def get_word_num(file, aim = None):
    try:
        # print(file)
        with open(file) as f:
            word_num = 0

            for line in f:
                word_of_line = line.split()
                word_num += len(word_of_line)
        strw = ("Word Number:", word_num, '\n')
        print("Word Number:", word_num)
        if aim:
            aim.insert('insert', strw)
    except:
        print("Open false")


def get_font_num(file, aim = None):
    try:
        # print(file)
        with open(file) as f:
            font_num = 0
            font_num2 = 0
            for line in f:
                font_num += len(line)
                font_num2 += len(line) - line.count(' ')
        strf1 = ("Font Number(Include space):", font_num , '\n')
        strf2 = ("Font Number(No space):", font_num2, '\n')
        print("Font Number(Include space):", font_num )
        print("Font Number(No space):", font_num2)
        if aim:
            aim.insert('insert', strf1)
            aim.insert('insert', strf2)
    except:
        print("Open false")