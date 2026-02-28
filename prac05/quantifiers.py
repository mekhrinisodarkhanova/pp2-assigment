#1 {n}
import re
text = "111 11 1111"
print(re.findall(r'\d{3}', text)) #['111', '111']

#2 {n,}
import re
text = "1 22 333 4444"
print(re.findall(r'\d{2,}', text)) #['22', '333', '4444']

#3 {n, m}
import re
text = "1 22 333 4444 55555"
print(re.findall(r'\d{2,4}', text)) #['22', '333', '4444', '5555']