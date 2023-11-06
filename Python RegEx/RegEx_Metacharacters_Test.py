# Metacharacters
# Metacharacters are characters with a special meaning:
#
# Character	Description	Example	Try it
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or	"falls|stays"
# ()	Capture and group

import re

txt = "The rain in Spain"

# Find all lower case characters alphabetically between "a" and "m"：
x = re.findall("[a-m]", txt)
print(x)

# ==========================

txt = "That will be 59 dollars"

# Find all digit characters:
x = re.findall("\d", txt)
print(x)

# ==========================

txt = "hello planet"

# Search for a sequence that starts with "he", followed by two(any) characters, and an "o"
x = re.findall("he..o", txt)
print(x)

# ==========================

txt = "hello planet"

# Check if the string starts with 'hello':

x = re.findall("^hello", txt)

if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

# ==========================

txt = "hello planet"

# Check if the string ends with "planet":

x = re.findall("planet$", txt)
if x:
    print("Yes, the string ends with 'planet")
else:
    print("No match")

# ==========================

txt = "hello planet"
txt_1 = "heo"
txt_2 = "heeeeeo"

# Search for a sequence that starts with "he", followed by 0 or more(any) characters, and
# an "o":
x = re.findall("he.*o", txt)
y = re.findall("he.*o", txt_1)
z = re.findall("he.*o", txt_2)
print(x)
print(y)
print(z)

# ==========================

import re

txt = "hello planet"
txt_1 = "heo"
txt_2 = "heeeeeo"

# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)
y = re.findall("he.+o", txt_1)  # not raise error, but print without data
z = re.findall("he.+o", txt_2)

print(x)
print(y)
print(z)

# ==========================

import re

txt = "hello planet"

# Search for a sequence that starts with "he", followed by 0 or 1 (any) character, and
# an "o"

x = re.findall("he.?o", txt)
print(x)

# This time we got no match, because there were not zero, not one, but two characters
# between "he" and the "o"

txt_1 = "helo"
txt_2 = "heo"
y = re.findall("he.?o", txt_1)
z = re.findall("he.?o", txt_2)
print(y)
print(z)

# ==========================

txt = "hello planet"

# Search for a sequence that starts with "he", followed exactly 2 (any) characters,
# and an "o":

x = re.findall("he.{2}o", txt)
print(x)
x = re.findall("he.{3}o", txt)
print(x)

# ==========================

txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains either "falls" or “stays":
x = re.findall("fall|stays", txt)

print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below,
# and has a special meaning:
# Try these special sequences at link: https://www.w3schools.com/python/python_regex.asp

# Character	Description	Example	Try it
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
# Set	Description	Try it
# [arn]	Returns a match where one of the specified characters (a, r, or n) is present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


