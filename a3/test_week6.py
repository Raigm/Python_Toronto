
from a3 import *

print(is_valid_word(["hola", "tu"], "t"))

list = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
print(make_str_from_row(list,1))
"""
>>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
"NS"

RBXSATAFCN
"""
word = []
n = 2
for i in range(len(list)):
    word.append(list[i][n])
word_colum = str("".join(word))
print(word_colum)
