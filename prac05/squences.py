#1 \d
import re
text = "Order 123, code 45"
print(re.findall(r'\d', text)) #['1', '2', '3', '4', '5']

#2 \w
import re
text = "Hello_123!"
print(re.findall(r'\w', text)) #['H', 'e', 'l', 'l', 'o', '_', '1', '2', '3']

#3 \s
import re
text = "Hello   world"
print(re.findall(r'\s', text)) #[' ', ' ', ' ']

#4 \D
import re
text = "A1B2a3b4"
print(re.findall(r'\D', text)) #['A', 'B', 'a', 'b']

#5 \W
import re
text = "Hello@123!"
print(re.findall(r'\W', text)) #['@', '!']

#6 \S
import re
text = "Hi there"
print(re.findall(r'\S', text)) #['H', 'i', 't', 'h', 'e', 'r', 'e']

#7 \A
import re
text = "Start here"
print(re.findall(r'\AStart', text)) #['Start']

#8 \Z
import re
text = "The end"
print(re.findall(r'end\Z', text)) #['end']