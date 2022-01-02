from pprint import pprint as pp

lst = [
    'Максимальное напряжение, B              250',
    'Максимальный ток, А                     6',
    'Тип рабочего тока                       переменный',
    'Высота педали, мм                       43.5',
    'Толщина педали, мм                      18',
    'Количество контактов (без реверса)      6'
]

pp(lst)

file = open('example_file.txt', 'w')
for line in lst:
    file.write(line)
    file.write('\n')

file.close()
print()

# read all
print()
file = open('example_file.txt')
lst = file.read()
file.close()
pp(lst)
print()

# read all
print()
file = open('example_file.txt')
lst = file.readlines()
file.close()
pp(list(map(lambda x: x.strip('\n'), lst)))
print()

# read by 40 symbols
lst = []
pp(lst)
file = open('example_file.txt')
while True:
    line = file.readline(40)
    if line != '':
        lst.append(line.strip('\n'))
    else:
        break
file.close()
print()
pp(lst)

# read by line
lst = []
pp(lst)
file = open('example_file.txt')
for line in file.readlines():
    lst.append(line.strip('\n'))
file.close()
print()
pp(lst)

# read by line
lst = []
pp(lst)
file = open('example_file.txt')
for line in file:
    lst.append(line.strip('\n'))
file.close()
print()
pp(lst)


size_buff = 32
src = open('Image_Cover.jpg', 'rb')
dst = open('Image_Cover_copy.jpg', 'wb')

while True:
    data = src.read(size_buff)
    if data:
        dst.write(data)
    else:
        break

src.close()
dst.close()

if src.closed:
    print('Source file was closed')

with open('Image_Cover.jpg', 'rb') as src, open('Image_Cover_copy_2.jpg', 'wb') as dst:
    if not src.closed:
        print('Source file is open')
    # with open('Image_Cover_copy_2.jpg', 'wb') as dst:
    while True:
        data = src.read(size_buff)
        if data:
            dst.write(data)
        else:
            break

if src.closed:
    print('Source file was closed')