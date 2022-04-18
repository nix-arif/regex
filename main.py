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
test4 = "abcdefabfhjad"
# res4 = re.sub(r"ab*", "x", test4)
res4 = re.split(r"ab+", test4)
print(res4)
