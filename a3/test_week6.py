
from a3 import *

list = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
word = "DRUDGERY"

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


print(word_score(word))
"1"


if len(word) >= 10:
    print (len(word)* 3)
elif len(word) >= 6 and len(word) < 9 :
    print(len (word) * 2)
elif len(word) < 6 and len(word) >= 3:
    print(len(word) * 1 )
else:
    print(0)

    # Word length: < 3: 0 points
    #              3-6: 1 point per character for all characters in word
    #              7-9: 2 points per character for all characters in word
    #              10+: 3 points per character for all characters in word
    #
    # >>> word_score('DRUDGERY')
    # 16
    # """
