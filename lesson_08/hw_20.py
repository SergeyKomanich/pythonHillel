import pprint

input_str = """
Based on extensive market research, competitive analysis, and “Internet 
Business Analysis”, we design the most efficient “unique” marketing system 
for your medical products system business that will achieve your growth goals and 
support all your marketing and sales in the and business.
The medical industry, though manufacturing in nature, demands a very high 
website and related property user system experience. It compares with the top brands 
in the consumer markets. People shopping for system medical products want the very 
best in system everything, the look and feel has to support system that demand for quality.
"""

lst_words = input_str.split()
words_dict = {}
for word in lst_words:
    words_dict[word] = words_dict.get(word, 0) + 1

# pprint.pprint(words_dict)
print(words_dict)
max_cnt = 0
word = ''
for key, value in words_dict.items():
    if value >= max_cnt:
        max_cnt = value
        word = key

print(word, max_cnt)
