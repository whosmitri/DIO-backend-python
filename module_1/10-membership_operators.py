
# used to check if an object is present in a sequence

# operators
# "in": returns True if a sequence with the specified value IS PRESENT in the object
# "not in": returns True if a sequence with the specified value IS NOT PRESENT in the object

print("### EXAMPLES ###")
course = "Curso de Python"
fruits = ["strawberry", "lemon", "apple"]
nums = [1500, 100]

print("Python" in course)
# True

print("grape" not in fruits)
# True

print("lemon" not in fruits)
# False

print(200 in nums)
# False