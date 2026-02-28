#1
import re
text = "cat bat rat"
print(re.findall(r'[cbr]at', text)) #['cat', 'bat', 'rat']

#2
import re
text = "a1 b2 c3"
print(re.findall(r'[a-c]', text)) #['a', 'b', 'c']

#3
import re
text = "A1 b2 C3"
print(re.findall(r'[A-Za-z]', text)) #['A', 'b', 'C']

#4
import re
text = "abc123"
print(re.findall(r'[^0-9]', text)) #['a', 'b', 'c']

import re
text = "abc123"
print(re.findall(r'[0-9]', text)) #['1', '2', '3']

#5
import re
text = "Year 2025"
print(re.findall(r'\d+', text)) #['2025']

#6
import re
text = "Hello_123!"
print(re.findall(r'\w+', text)) #['Hello_123']

#7
import re
text = "Hi   there"
print(re.findall(r'\s+', text)) #['   ']

#8
import re
text = "User_01, User-02"
print(re.findall(r'[A-Za-z_]\w+', text)) #['User_01', 'User']