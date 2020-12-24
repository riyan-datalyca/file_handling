import file_functions as ff
# # import tinydb file extension
# import tinydbfunctions as td

file1 = 'requir.txt'
file2 = 'new_file.txt'

fr = ff.fwrite(file1)
fr.write('hooo')
fr.close()

fa = ff.fappend(file2)
last_line = fa.tell()
print(last_line)
fa.seek(5)
print(fa.tell())

# # Get Json form TinyDB and paste in the file.
# dict_to_string = str(td.show())
# dict_to_string = dict_to_string[1:]
# print(dict_to_string)
# fa.write(' ' + dict_to_string)
fa.close()

fa = ff.fread(file2)
print(fa.read())
fa.close()

fw = ff.fread(file1)
print(fw.read())
fw.close()
