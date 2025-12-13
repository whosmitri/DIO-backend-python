
def my_decorator(function):
    def envelope():
        print('Do something before')
        function()
        print('Do something after')

    return envelope

def hello_world():
    print('Hello World')

test = my_decorator(hello_world)
test()
# Do something before
# Hello World
# Do something after
