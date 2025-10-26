
# used to compare whether the two tested objects occupy the same position in memory

# operators:
# is:
#   returns True if BOTH VARIABLES are the SAME object
# is not:
#   returns True if BOTH VARIABLES are NOT the SAME object

print("### EXAMPLES ###")
course = "Curso de Python"
course_name = course
x, y = 10, 10

print(course is course_name)
# True

print(course is not course_name)
# False

print(x is y)
# True

# difference between "is" and "==":
# "is": checks if both variables point to the same object in memory
# ""==": checks if the values of both variables are equal
