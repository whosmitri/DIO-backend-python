
# unlike lists or other iterable types, generators do not store all their values ​​in memory
# they are defined using regular functions, but instead of using "return", they use "yield"

# characteristics:
# - when a generated item is consumed, it is forgotten and cannot be accessed again
# - the internal state of a generator is maintained between calls
# - the execution of a generator is paused at the "yield" statement and resumed the next time it is called

# used for:
# - retrieving API data
# - requesting data per page (pagination)
# - providing one product at a time between calls
# - treating API consumption as a Python list.

###

def my_generator(nums = list[int]):
    for num in nums:
        yield num * 2

# using my_generator:
numbers = my_generator(nums=[4, 2, 18, 19])
for i in numbers:
    print(i)