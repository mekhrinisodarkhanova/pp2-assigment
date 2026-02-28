""" 
SuperMart Store
Date: 2026-02-28 20:25

Milk            2.50
Bread           1.20
Eggs            3.40
Chocolate       4.75

Total: 11.85
Payment: Card

Thank you for shopping!
"""
#1 Extract all prices from the receipt
import re
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
prices = re.findall(r'\d+\.\d{2}', text)
print(prices)

#2 Find all product names
import re
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
products = re.findall(r'^([A-Za-z]+)\s+\d+\.\d{2}', text, re.MULTILINE)
print(products)

#3 Calculate total amount
import re
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
prices = re.findall(r'\d+\.\d{2}', text)
total = sum(float(p) for p in prices[:-1])  # исключаем Total
print(total)

#4 Extract date and time information
import re
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
datetime = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', text)
print(datetime.group())

#5 Find payment method
import re
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
payment = re.search(r'Payment:\s+(\w+)', text)
print(payment.group(1))

#6 Create a structured output (JSON or formatted text)
import re
import json
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
products = re.findall(r'^([A-Za-z]+)\s+\d+\.\d{2}', text, re.MULTILINE)
prices = [float(p) for p in re.findall(r'\d+\.\d{2}', text)]
total = prices[-1]
data = {
    "products": products,
    "prices": prices[:-1],
    "total": total
}
print(json.dumps(data, indent=4))