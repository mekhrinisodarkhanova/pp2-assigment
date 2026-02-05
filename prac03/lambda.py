#1 Lambda syntax and basic usage
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#2 Using lambda with for transformation map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#3 Using lambda with for selection filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#4 Using lambda with for custom sortingsorted()
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
#5 Anonymous functions vs regular functions
students = [("Alice", 85), ("Bob", 90), ("Charlie", 80)]

students.sort(key=lambda x: x[1])
print(students)