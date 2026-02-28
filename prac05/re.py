#1 re.search()
import re
text = "My number is 12345"
result = re.search(r'\d+', text)
print(result.group()) #12345

#2 re.findall() 
import re
text = "I have 2 apples and 3 bananas"
result = re.findall(r'\d+', text)
print(result) #['2', '3']

#3 re.split()
import re
text = "apple,banana;orange grape"
result = re.split(r'[;, ]+', text)
print(result) #['apple', 'banana', 'orange', 'grape']

#4 re.sub()
import re
text = "My phone is 12345"
result = re.sub(r'\d+', "XXXXX", text)
print(result) #My phone is XXXXX

#5 re.match()
import re
text = "Hello world"
result = re.match(r'Hello', text)
print(result.group()) #Hello