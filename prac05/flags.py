#1 re.ASCII
import re
text = "Hello Привет"
result = re.findall(r'\w+', text, re.ASCII)
print(result) #['Hello']

#2 re.DEBUG
import re
re.compile(r'\d+', re.DEBUG) 

#3 re.DOTALL
import re
text = "Hello\nWorld"
result = re.findall(r'Hello.*World', text, re.DOTALL)
print(result) #['Hello\nWorld']

#4 re.IGNORECASE
import re
text = "Hello hello HeLLo"
result = re.findall(r'hello', text, re.IGNORECASE)
print(result) #['Hello', 'hello', 'HeLLo']

#5 re.MULTILINE
import re
text = "cat\ndog\ncat"
result = re.findall(r'^cat', text, re.MULTILINE)
print(result) #['cat', 'cat']

#6 re.NOFLAG
import re
text = "Hello\nWorld"
result = re.findall(r'Hello.*World', text, re.NOFLAG)
print(result) #[]

#7 re.UNICODE
import re
text = "Hello Привет"
result = re.findall(r'\w+', text, re.UNICODE)
print(result) #['Hello', 'Привет']

#8 re.VERBOSE
import re
pattern = re.compile(r"""
    \d{3}   # первые 3 цифры
    -       # дефис
    \d{2}   # 2 цифры
""", re.VERBOSE)
print(pattern.findall("123-45")) #['123-45']