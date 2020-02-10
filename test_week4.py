print ("Hello world!")
from a2 import *


print(get_length("GATTACA"))
print(is_longer("GATTACA","GATTCA"))
print(is_longer('ATCG', 'AT'))
print(is_longer('ATCG', 'ATCGGA'))
print(count_nucleotides('ATCGGC', 'G'))
print(contains_sequence('ATCGGC', 'GT'))
print(is_valid_sequence("GATTACA"))
print(insert_sequence("CCGG", "AT", 2))
print(get_complement("F"))
print(get_complementary_sequence("AT"))

