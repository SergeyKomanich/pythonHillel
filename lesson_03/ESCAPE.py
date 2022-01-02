"""
\                       new line
\n                      new line
\t                      tab
\b                      backspace
\'                      '
\"                      "
\\                      \
"""

s = 'erugihweiougherilughleiruhgeilrughlieurhglieruhgkdlfjhgdfk.jhgdfkj.hgelriu.hkdgileruwkghvpeilrwuk.j' \
    'dhgvnlerku.dj,hgvneilrwu.kdjghvneilrwku.djfghnveilqrku.jdghvneilruwkdfghjvneiprwlukdgjfhveirwluk.jdgh' \
    'vewilruk.jdfghvnpeirulwk.jghnveiruwlkjdfhgnepriuwlkjghnveiprwlukdjh.gnvelrwiuk.hgj'
print(len(s))

print('Hello\nWorld!')
print('Hello\t\tWorld!')
print('Helloo\b World!')

s = 'Hello \'World\'!'
print(s)

s = "Hello \"World\"!"
print(s)

s = "Hello 'World'!"
print(s)

s = 'Hello "World"!'
print(s)

s = 'Hello \\World\\'
print(s)
