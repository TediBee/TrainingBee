import modules

print(modules.nama)
print(modules.list2d)
a=modules.dictionary["umur"]
print(a)


b = lambda x : x * 2
print(b(5))


from functools import reduce
# Example with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# Example with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example with reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

