def my_decorator(function):
    # example of use: first check security, 
    # execute the function, 
    # save the result of the execution, 
    # then send it to another service.

    def envelope(*args, **kwargs):
        print('Do something before')
        result = function(*args, **kwargs)
        print('Do something after')
        return result

    return envelope

@my_decorator
def hello_world(name):
    print(f'Hello World, {name}')
    return (name.upper())

my_result = hello_world('Miguel')
print(my_result)