
# local scope: within the block, changes made will be lost when the object finishes executing.

# global scope: global variables are available from within any scope, global and local

# to use global objects, the reserved word "global" is used, which informs the interpreter that the variable is global, but this is NOT a good practice and should be avoided.

salary = 2000

def salary_bonus(bonus=0):
    global salary
    salary += bonus
    return salary

###

print(salary_bonus())
# 2000

print(salary_bonus(500))
# 2500

print(salary_bonus())
# 2500