
print("\n\n#### APPEND() ####")

my_list = []
print(my_list)
# []

my_list.append(1)
my_list.append('python')
my_list.append(['Miguel', 20.05, 'blue', 'Formula 1'])
print(my_list)
# [1, 'python', ['Miguel', 20.05, 'blue', 'Formula 1']]


print("\n\n#### CLEAR() ####")
print(my_list)
# [1, 'python', ['Miguel', 20.05, 'blue', 'Formula 1']]

my_list.clear()
print(my_list)
# []


print("\n\n#### COPY() ####")
my_list = ['Miguel', 20.05, 'blue', 'Formula 1']
print(my_list)
# ['Miguel', 20.05, 'blue', 'Formula 1']

list_backup = my_list.copy()
print(list_backup)
# ['Miguel', 20.05, 'blue', 'Formula 1']

print(id(my_list),'\n', id(list_backup))


print("\n\n#### COUNT() ####")
colors = ['blue', 'green', 'red', 'blue', 'gray', 'black', 'blue']
print(colors.count('red'))
# 1
print(colors.count('blue'))
# 3


print("\n\n#### EXTEND() ####")
languages = ['python', 'js', 'c']
print(languages)
# ['python', 'js', 'c']

languages.extend(['java', 'lua'])
print(languages)
# ['python', 'js', 'c', 'java', 'lua']


print("\n\n#### INDEX() ####")
print(languages)
# ['python', 'js', 'c', 'java', 'lua']

print(languages.index('lua'))
# 4
print(languages.index('python'))
# 0


print("\n\n#### POP() ####")
print(languages)
# ['python', 'js', 'c', 'java', 'lua']

print(languages.pop())
# lua

print(languages.pop())
# java

print(languages.pop(1))
# js

print(languages)
# ['python', 'c']


print("\n\n#### REMOVE() ####")
languages = ['python', 'js', 'c', 'java', 'lua']
print(languages)
# ['python', 'js', 'c', 'java', 'lua']

languages.remove('c')
print(languages)
# ['python', 'js', 'java', 'lua']


print("\n\n#### REVERSE() ####")
languages = ['python', 'js', 'c', 'java', 'lua']
print(languages)
# ['python', 'js', 'c', 'java', 'lua']

languages.reverse()
print(languages)
# ['lua', 'java', 'c', 'js', 'python']


print("\n\n#### SORT() ####")
languages = ['python', 'js', 'c', 'java', 'lua']
print(languages)
# ['python', 'js', 'c', 'java', 'lua']

l2 = languages.copy()
l2.sort()
print(l2)
# ['c', 'java', 'js', 'lua', 'python']

l2.sort(reverse=True)
print(l2)
# ['python', 'lua', 'js', 'java', 'c']

l2.sort(key=lambda x:len(x))
print(l2)
# ['c', 'js', 'lua', 'java', 'python']

l2.sort(key=lambda x: len(x), reverse=True)
print(l2)
# ['python', 'java', 'lua', 'js', 'c']