
# a function is a block of code identified by a name and can receive a list of parameters; these parameters may or may not have default values. using functions makes the code more readable and allows for code reuse. programming based on functions is the same as saying that we are programming in a structured way.

print('### FIRST FUNCTION ###')

def show_message():
    print('Hello Mitri')

def show_message_2(name):
    print(f'Welcome, {name}')

def show_message_3(name='Anonymous'):
    print(f'Welcome, {name}')

show_message()
# Hello Mitri

show_message_2('Dmitri')
# Welcome, Dmitri

show_message_3()
# Welcome, Anonymous

show_message_3(name='Miguel')
# Welcome, Miguel