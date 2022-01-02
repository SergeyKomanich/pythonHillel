"""
file = open(file_name, mode, encoding)
...
file.close()
"""

"""
Mode

r       read (default)
w       write
x       exclusive
a       append

b       binary
t       text (default)

rt
wt
xt
at

rb
wb
xb
ab
"""

file = open('file.txt', 'w', encoding='utf-8')
file.write('Hello World!\n')
# file.write('\n')
file.write('Привет Мир!')
file.close()
