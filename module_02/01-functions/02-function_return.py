
def calc_total(numbers):
    return sum(numbers)

def get_predecessor_and_successor(number):
    predecessor = number - 1
    successor = number + 1

    return predecessor, successor

def func_3():
    print('Hello world!')

###

print(calc_total([10, 20, 34]))
# 64
print(get_predecessor_and_successor(10))
# (9, 11)
print(func_3())
# None