
# used with comparison operators to build a logical expression. When a comparison operator is used, the returned result is a boolean

# operators
# and:
#   returns True if BOTH STATEMENTS are TRUE
#   1 + 1 = 1
#   1 + 0 = 0
#   0 + 0 = 0
# or:
#   returns True if ONE OF THE STATEMENTS are TRUE
#   1 + 1 = 1
#   1 + 0 = 1
#   0 + 0 = 0
# not:
#   REVERSE THE RESULT, returns False if the result is True
#   1 + 1 = 0
#   0 + 0 = 1

###

# AND
print("### AND ###")

print(True and True)
# True

print(True and False)
# False

print(False and False)
# False

# OR
print("### OR ###")

print(True or True)
# True

print(True or False)
# True

print(False or False)
# False

# NOT
print("### NOT ###")

print(not True)
# False

print(not False)
# True

###

print("### EXAMPLES ###")

x = 1000
y = 200
z = 100

# AND
print(x >= y and y <= z)
# False

# OR
print(x >= y or y <= z)
# True

# NOT
print(not y > z)
# False

# using "()" to organize our code
a = 100
b = 25
c = 20
d = True

# a >= b and b <= c or d and a >= b
print( (a >= b and b <= c) or (d and a >= b) )
# True
