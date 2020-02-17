
from a3 import *

list = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

# #testing functions
# print(is_valid_word(["ALSE", "TU"], "TU"))
# "True"
#
# print(make_str_from_row(list,1))
# "XSOB"
#
# print(make_str_from_column(list,1))
# "NS"
#
#
# print(board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'XSOB'))
# "TRUE"

print(board_contains_word_in_column(list, "AX"))


