
# a tuple is a collection which is ordered and unchangeable

print("### EXAMPLES ###")

print("\n\n#### ONE ####")
fruits = ('strawberry', 'lemon','orange',)
print(fruits)
# ('strawberry', 'lemon','orange',)

country = ('Brasil',)
print(country)
# ('Brasil',)

# when declaring a tuple with parentheses, it's good practice to put a comma (,) at the end. This allows the Python interpreter to recognize the tuple without confusing it with a precedence rule, especially when declaring a tuple with a single element.


print("\n\n#### TWO - TUPLE METHOD ####")
letters = tuple('python')
print(letters)
# ('p', y', 't', 'h', 'o', 'n')

nums = tuple([1, 2, 3, 4])
print(nums)
# (1, 2, 3, 4)

my_tuple = tuple(['Miguel', 20.05, 'RBR', 'Ferrari'])
print(my_tuple)
# ('Miguel', 20.05, 'RBR', 'Ferrari')


print("\n\n#### THREE ####")
print(fruits)
# ('strawberry', 'lemon','orange',)
print(fruits[0])
# strawberry
print(fruits[2])
# orange
print(fruits[-1])
# orange

print("\n\n#### FOUR ####")
matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (5, 6, 'c')
)
print(matriz)

print(matriz[0])
# (1, 'a', 2)
print(matriz[0][0])
# 1
print(matriz[0][-1])
# 2
print(matriz[-1][-1])
# c


print("\n\n## TUPLE METHODS ##")

print("\n### EXAMPLES ###")

print("\n#### ONE - COUNT ####")
colors = ('blue', 'green', 'red', 'blue',)
print(colors)
print(colors.count('green'))
# 1
print(colors.count('blue'))
# 2

print("\n\n#### TWO - INDEX ####")
languages = ('python', 'js', 'c', 'lua')
print(languages)
print(languages.index('lua'))
# 3
print(languages.index('python'))
# 0

print("\n\n#### THREE - LEN ####")
print(languages)
print(len(languages))
# 4