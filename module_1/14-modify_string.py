
# 'string' is the same as "hello"

print("### MODIFY STRINGS WITH METHODS ###\n")

course = "pYtHon"
print("course =", course)

print("\n#### UPPER CASE ####")
print(course.upper())
# PYTHON

print("\n#### LOWER CASE ####")
print(course.lower())
# python

print("\n#### TITLE CASE ####")
print(course.title())
# Python

course = "   Python "
print("\n\ncourse =", course)

print("\n#### REMOVE WHITESPACE ####")
print("course =", course)
print(course.strip())
# "Python"

print("\n#### REMOVE START WHITESPACE ####")
print(course.lstrip())
# "Python "

print("\n#### REMOVE END WHITESPACE ####")
print(course.rstrip())
# "   Python"

course = "Python"
print("\n\ncourse =", course)

print("\n\n#### CENTER ####")
print(course.center(10, "#"))
# "##Python##"

print("\n#### JOIN ####")
print(".".join(course))
# "P.y.t.h.o.n"