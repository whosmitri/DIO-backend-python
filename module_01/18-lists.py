
# lists in python are mutable objects (they can change their value after creation) and can store any type of object sequentially; we can create lists using the "list" constructor, the "range" function or by placing values ​​separated by commas inside square brackets

print("### EXAMPLES ###")

print("\n\n#### ONE ####")
fruits = ['starwberry', 'apple', 'lemon']
print(fruits)
# ['starwberry', 'apple', 'lemon']

fruits = []
print(fruits)
# []


print("\n\n#### TWO - LIST METHOD ####")
letters = list('python')
print(letters)
# ['p', 'y', 't', 'h', 'o', 'n']


print("\n\n#### THREE - RANGE METHOD ####")
nums = list(range(10))
print(nums)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print("\n\n#### FUOR ####")
data = ['Dmitri Calle', 20.05, True, 3000, 'Ferrari', "Miguel", 04.02]
print(data)
# data = ['Dmitri Calle', True, 3000, 'Ferrari', 'Miguel']


print("\n\n#### FIVE - FRUIT LIST ####")
fruits = ['strawberry', 'blueberry', 'apple', 'grape', 'banana']

print(fruits[0])
# strawberry
print(fruits[2])
# apple
print(fruits[-1])
# banana
print(fruits[-3])
# apple


print("\n\n#### SIX - MATRIZ ####")
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]
print(matriz)

print(matriz[0])
# [1, 'a', 2]
print(matriz[0][0])
# 1
print(matriz[0][-1])
# 2
print(matriz[-1][-1])
# c


print("\n\n#### SEVEN - LETTERS LIST ####")
my_list = letters
print(my_list)
# ['p', 'y', 't', 'h', 'o', 'n']

print(my_list[::])
# ['p', 'y', 't', 'h', 'o', 'n']

print(my_list[2:])
# ['t', 'h', 'o', 'n']

print(my_list[:2])
# ['p', 'y']

print(my_list[0:3:2])
# ['p', 't']

print(my_list[::-1])
# ['n', 'o', 'h', 't', 'y', 'p']


print("\n\n#### EIGHT - ENUMERATE FUNCTION ####")

formula1 = ['Ferrari HP', 'Red Bull Racing', 'Kick Sauber']

for index, f1 in enumerate(formula1):
    print(f'{index}: {f1}')
    # 0: Ferrari HP
    # 1: Red Bull Racing
    # 2: Kick Sauber


print("\n\n#### NINE - FILTER 1 ####")
numbers1 = [1, 30, 21, 2, 9, 65, 34]
even_nums1 = []
squared_nums1 = []

for number in numbers1:
    if (number % 2 == 0):
        even_nums1.append(number)
print(even_nums1)
# [30, 2, 34]

for number in numbers1:
    squared_nums1.append(number ** 2)
print(squared_nums1)
# [1, 900, 441, 4, 81, 4225, 1156]

print("\n\n#### TEN - FILTER 2 ####")
numbers2 = [1, 30, 21, 2, 9, 65, 34]
even_nums2 = [number for number in numbers2 if number % 2 == 0]
squared_nums2 = [number ** 2 for number in numbers2]
print(even_nums1)
# [30, 2, 34]
print(squared_nums1)
# [1, 900, 441, 4, 81, 4225, 1156]