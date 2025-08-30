# Basic lambda
add = lambda x, y: x + y
print("Add:", add(2, 3))

# Lambda with map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print("Squared with map:", squared)

# Lambda with filter
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers with filter:", even)

# Lambda with sorted (custom key)
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: len(x))
print("Sorted by length:", sorted_words)

# Lambda in list comprehensions
pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("Pairs sorted by second element:", sorted_pairs)

# Lambda as argument to functions
def apply_func(f, x, y):
    return f(x, y)
print("Apply lambda as argument:", apply_func(lambda a, b: a * b, 4, 5))

# Lambda with default arguments
inc = lambda x, step=1: x + step
print("Increment with default:", inc(10))
print("Increment with custom step:", inc(10, 5))

# Lambda for conditional expressions
max_func = lambda a, b: a if a > b else b
print("Max using lambda:", max_func(7, 3))
