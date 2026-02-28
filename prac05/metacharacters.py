#1 "."
import re
text = "cat cake cut"
print(re.findall(r'c.t', text)) #['cat', 'cut']

#2 "*"
import re
text = "ab acbb abbb cbab"
print(re.findall(r'ab*', text)) #['ab', 'a', 'abbb', 'ab']

#3 "+"
import re
text = "ab abbc ac cab"
print(re.findall(r'ab+', text)) #['ab', 'abb', 'ab']

#4 "?"
import re
text = "color colour colouur colourr"
print(re.findall(r'colou?r', text)) #['color', 'colour', 'colour']

#5 "^"
import re
text = "Hello world"
print(re.findall(r'^Hello', text)) #['Hello']

#6 "$"
import re
text = "Hello world"
print(re.findall(r'world$', text)) #['world']

#7 "[]"
import re
text = "cat bat rat"
print(re.findall(r'[cbr]at', text)) #['cat', 'bat', 'rat']

#8 "|"
import re
text = "cat dog bird"
print(re.findall(r'cat|dog', text)) #['cat', 'dog']

#9 "()"
import re
text = "abab ab abc cab cba"
print(re.findall(r'(ab)+', text)) #['ab', 'ab', 'ab', 'ab']

#10 "\"
import re
text = "3.14 2.71"
print(re.findall(r'\d+\.\d+', text)) #['3.14', '2.71']