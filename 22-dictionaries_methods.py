
print("#### COPY() ####")
my_data = {
    'dmitri.calle@mail.com': {
        'name': 'Dmitri',
        'phone': '1234-5678'
    },
    'miguel.souza@mail.com': {
        'name': 'Miguel',
        'phone': '8765-4321'
    }
}
print('my_data')
print(my_data)
# {dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'}, miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

print('*' * 20)

my_data_bkp = my_data.copy()
print('my_data_backup')
print(my_data_bkp)
# {dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'}, miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}


print("\n\n#### CLEAR() ####")
print(my_data)
# {dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'}, miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

my_data.clear()
print(my_data)
# {}


print("\n\n#### FROMKEYS() ####")
data = dict.fromkeys(['name', 'email'])
print(data)
# {'name',: None, 'email': None}
print('*' * 20)
data.fromkeys(['name', 'email'], 'empty')
# {'name',: 'empty', 'email': 'empty'}
print(data)


print("\n\n#### GET() ####")

print(my_data_bkp)
# {dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'}, miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

# print(my_data_bkp['key'])
# keyError

print(my_data_bkp.get('key'))
# None
print(my_data_bkp.get('key', {}))
# {}
print(my_data_bkp.get('miguel.souza@mail.com', {}))
# {'name': 'Miguel', 'phone': '8765-4321'}


print("\n\n#### ITEMS() ####")
my_data = {
    'miguel.souza@mail.com': {'name': 'Miguel', 'phone': '8765-4321'}
}

print(my_data)
# {miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

print('*' * 20)

print(my_data.items())
# dict_items([(miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'})])


print("\n\n#### KEYS() ####")
print(my_data)
# {miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

print(my_data.keys())
# dict_items([miguel.souza@mail.com])

print(my_data.pop('miguel.souza@mail.com'))
# {'name': 'Miguel', 'phone': '8765-4321'}

print(my_data.pop('miguel.souza@mail.com', {}))
# {}


print("\n\n#### POPITEM() ####")
my_data = {
    'miguel.souza@mail.com': {'name': 'Miguel', 'phone': '8765-4321'}
}

print(my_data)
# {miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

print(my_data.popitem())
# (miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'})

# print(my_data.popitem())
# KeyError

print("\n\n#### SETDEFAULT() ####")
my_data = {
    'name': 'Miguel', 'phone': '8765-4321'
}

print(my_data)
# {'name': 'Miguel', 'phone': '8765-4321'}

print(my_data.setdefault('name', 'Miu'))
# Miguel

print(my_data.setdefault('age', 18))
# 18

print(my_data)
# {'name': 'Miguel', 'phone': '8765-4321', 'age': 18}

print("\n\n#### UPDATE() ####")
my_data = {
    'miguel.souza@mail.com': {'name': 'Miguel', 'phone': '8765-4321'}
}

print(my_data)
# {miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

my_data.update({'miguel.souza@mail.com': {'name': 'Miu'}})

print(my_data)
# {miguel.souza@mail.com: {'name': 'Miu', 'phone': '8765-4321'}}

print("\n\n#### VALUES() ####")

print(my_data_bkp)
# {dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'}, miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

print('*' * 20)

print(my_data_bkp.values())
# dict_values([{'name': 'Dmitri', 'phone': '1234-5678'}, {'name': 'Miguel', 'phone': '8765-4321'}])


print("\n\n#### IN() ####")
print(my_data_bkp)
# {dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'}, miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}

print('miguel.souza@mail.com' in my_data_bkp)
# True

print('age' in my_data_bkp['dmitri.calle@mail.com'])
# False

print('phone' in my_data_bkp['miguel.souza@mail.com'])
# True


print("\n\n#### DEL() ####")
print(my_data_bkp)
# {dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'}, miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}}
print('*' * 20)

del my_data_bkp['dmitri.calle@mail.com']
del my_data_bkp['miguel.souza@mail.com']['phone']

print(my_data_bkp)
# {miguel.souza@mail.com: {'name': 'Miguel'}}