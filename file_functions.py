def fread(fname):
    fw = open(fname, mode='rt')
    return fw


def fwrite(fname):
    fw = open(fname, mode='wt')
    return fw


def fappend(fname):
    fw=open(fname,mode='at')
    return fw

def fcloseAll():
    pass

# try:
#     fw = open('requir.txt', mode='rt+', encoding='utf-8')
#     fw.write("hello\n")
#     fw.write("mosi mossshi")
#     fw.close()
#     # fx=open('new_file.txt', mode='xt',encoding='utf-8')
#     # fx.write("new file")
#     # fa=open('.txt', mode='at',encoding='utf-8')
#
#     fr = open('requir.txt', mode='rt+', encoding='utf-8')
#     print(fr.read())
#     fr.write("\n bakemono")
#     print(fr.read())
# finally:
#     fw.close()
#     fr.close()
