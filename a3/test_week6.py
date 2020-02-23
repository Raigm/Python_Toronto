
from a3 import *

list = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
word = "123456"

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
print(board_contains_word_in_row(list, 'XSOB'))
# "True"

print(board_contains_word_in_column(list, "AX"))
# "True"

print(board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANTa'))
# "True"

word = "ANT"
print(word_score(word))
"1"

player_info = ['Jonathan', 4]

print(update_score(player_info, word))
"""
>> > update_score(['Jonathan', 4], 'ANT')
"""
