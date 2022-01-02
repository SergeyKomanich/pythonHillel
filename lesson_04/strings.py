s1 = 'dkf.jfhdkljghs;dkjgfhds;kfn;sdknsd;knfs;dk;;jf;dsfn'
s2 = "ksjhdvlknfdslknvdskjnvcds,fnsd\nlknvdsln,v"
# s3 = 'kjhglkjfwelfjwejnfw"
s4 = """
;efhigs;djfw[ejf
e;fgjodspofjkwdepfk
elkgjvsdljfsd
            peoirjgsfmlw
    ewlkhfglksjnfslkedjf
"""
# print(s4)

s5 = '''
lkejrgds
fwg:DFLbvdsf  ed'bdf
    d;lmd;kmgd
'''
# print(s5)

s = '\u26bd'

print('\u26bd')
print(s)
x = chr(0x26bd)
print(x)
print(chr(0x26bd))
print(chr(9917))

s = '\U0001f6a3'
print(s)

s = 0x1f6a3
print(chr(s))

x1 = ord('⚽')
print(x1, hex(x1))
x2 = ord('🚣')
print(x2, hex(x2))
print(chr(128675), chr(0x0001f6a3))

#    0   1   2   3   4
#   'H   E   L   L   O'
#   -5  -4  -3  -2  -1

s = 'Hello World!'
x = len(s) - 1
print(x)

# str[index]
print(s[2])
print(s[-2])
print(s[len(s) - 2])
# print(s[12])
# print(s[-14])

# slices
# range(start, stop, step)
#   str[start: stop: step]
s = 'Process finished with exit code 0'
s1 = s[:]
print(id(s))
print(id(s1))
print(s[:])
print(s[0: 7])
print(s[: 7])
print(s[8: 16])
print(s[27: 33])
print(s[-34785648327548734: 33078463529746597843659348])
print(s[::2])
print(s[::-1])

s = 'Process finished with exit code 0'
# len(str)
print(len(s))

# int(str), float(str), str(int)
print(str(12.34), type(str(12.34)))

# str.find(sub, start, stop), str.rfind(sub, start, stop)
print(s.find('with1'))
print(s.find('e'))
print(s.find('e', 5))
print(s.find('e', 15))
print(s.find('e', 23))
print(s.find('e', 31))

# str.replace(old, new, count)
s1 = s.replace('e', 'E', 2)
print(s)
print(s1)

# str.count(sub)
print(s.count('it'))

vasia = 'r r r r r rProcess finished with exit code 0aaaaaaaa'
# str.strip(sub)
print('"' + vasia + '"')
print('"' + vasia.strip('r a') + '"')
