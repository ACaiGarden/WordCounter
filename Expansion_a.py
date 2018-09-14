import re

def get_special_num(file, aim = None):
    get_empty_line(file, aim)
    get_annotate_line(file, aim)
    get_code_line(file, aim)

def get_empty_line(file, aim = None):
    empty_line = 0
    try:
        with open(file) as f:
            for line in f:
                if (len(line.strip()) <= 1) and re.search('{|}',line.strip()):
                    empty_line += 1
    except:
        pass
    stre = ('empty:',empty_line, '\n')
    print('empty:',empty_line)
    if aim:
        aim.insert('insert', stre)
    return empty_line

def get_code_line(file, aim = None):
    code_line = 0
    try:
        with open(file) as f:
            for line in f:
                if (len(line.strip()) > 1) and not re.search('//',line.strip()):
                    code_line += 1
    except:
        pass
    code_line -= get_block_annotate_line(file, aim = None)
    strc = ('code:',code_line ,'\n')
    print('code:',code_line )
    if aim:
        aim.insert('insert', strc)
    return code_line

def get_annotate_line(file, aim = None):
    annotate_line = 0
    try:
        with open(file) as f:
            for line in f:
                if re.search('//', line.strip()):
                    annotate_line += 1
        f.close()

        with open(file) as f:
            is_annotate = False
            try:
                for line in f:
                    if re.search('/\*', line.strip()):
                        is_annotate = True
                    if is_annotate == True:
                        annotate_line += 1
                    if re.search('\*/', line.strip()):
                        is_annotate = False
            except:
                print('err')

    except:
        pass
    stra = ('annotate:',annotate_line,'\n')
    print('annotate:',annotate_line)
    if aim:
        aim.insert('insert', stra)
    return annotate_line

def get_block_annotate_line(file, aim = None):
    block_annotate_line = 0

    with open(file) as f:
        is_annotate = False
        for line in f:
            if re.search('/\*', line.strip()):
                is_annotate = True
            if is_annotate == True:
                block_annotate_line += 1
            if re.search('\*/', line.strip()):
                is_annotate = False
    return block_annotate_line


if __name__ == '__main__':
    path = 'D:\BianChenRuanJian\PyCharm\PyCharm Community Edition 2017.3.4\WordCounter\\testfile\\test3.c'
    get_special_num(path)