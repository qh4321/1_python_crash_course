for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**3)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value**2 for value in range(1,21,2)]
print(squares)