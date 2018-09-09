import re

def get_special_num(file):
    get_empty_line(file)
    get_annotate_line(file)
    get_code_line(file)

def get_empty_line(file):
    empty_line = 0
    try:
        with open(file) as f:
            for line in f:
                if (len(line.strip()) <= 1) and re.search('{|}',line.strip()):
                    empty_line += 1
    except:
        pass
    print('empty:',empty_line)
    return empty_line

def get_code_line(file):
    code_line = 0
    try:
        with open(file) as f:
            for line in f:
                if (len(line.strip()) > 1) and not re.search('//',line.strip()):
                    code_line += 1
    except:
        pass
    code_line -= get_block_annotate_line(file)
    print('code:',code_line)
    return code_line

def get_annotate_line(file):
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
    print('annotate:',annotate_line)
    return annotate_line

def get_block_annotate_line(file):
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