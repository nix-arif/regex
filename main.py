import re

test1 = "The matches any string that starts with 'The'."

res1 = re.sub(r"^The", "", test1)
print(res1)

test2 = "matches a string that ends in with of despair"
res2 = re.sub(r"of despair$", "", test2)
print(res2)


test3 = "abc ad"
res3 = re.sub(r"^abc$", "", test3)
print(res3)

###############################################################################
test4 = "cdefabfhjab"
# res4 = re.sub(r"ab*", "x", test4)
res4 = re.split(r"ab+", test4)
print(res4)

target_string = "My name is maximums and my luck numbers are 12 45 78"
# split on white-space
word_list = re.split(r"\s+", target_string)
print(word_list)
