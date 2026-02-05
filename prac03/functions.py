#1 Function definition and calling
def my_function():
  print("Hello from a function")

my_function()
#2 Function arguments (positional, default, *args, **kwargs)
def example(a, b=10, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

example(5, 20, 1, 2, 3, name="Aman", score=90)
#3 Return values and statements
def get_greeting():
  return "Hello from a function"

print(get_greeting())
#4 Passing lists and other data types as arguments
def process_data(a, s, lst, d):
    a += 1
    s += "!"
    lst.append(100)
    d["done"] = True

num = 5
text = "Hi"
numbers = [1, 2]
info = {}

process_data(num, text, numbers, info)

print(num)      # 5
print(text)     # Hi
print(numbers)  # [1, 2, 100]
print(info)     # {'done': True}
#5 Function documentation with docstrings
def multiply(x, y):
    """
    Multiply two numbers.

    Args:
        x (int): first number
        y (int): second number

    Returns:
        int: product of x and y
    """
    return x * y

x = int(input())
y = int(input())
print(multiply(x, y))