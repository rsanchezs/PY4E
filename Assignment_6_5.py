import re


text = "X-DSPAM-Confidence:    0.8475"

semicolon_pos = text.find(" ",0,text.__len__())
str = text[semicolon_pos:]
str_without_spaces = re.sub('\s+',' ', str)
print (str_without_spaces)