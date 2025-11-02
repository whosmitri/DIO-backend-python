
# a dictionary is an unordered set of key:value pairs, where the keys are unique within a given instance of the dictionary
# dictionaries are delimited by curly braces: {}, and contain a comma-separated list of key:value pairs.

print("### EXAMPLES ###")

print("\n#### ONE ####")

data1 = {
    'name': 'Miguel',
    'age': 18
}
print(data1)
# {'name': 'Miguel', 'age': 18}

print("\n\n#### TWO ####")

data2 = dict(name='Dmitri', age=19)
print(data2)
# {'name': 'Dmitri', 'age': 19}

print("\n\n#### THREE ####")

data2['phone'] = '1234-5678'
print(data2)
# {'name': 'Dmitri', 'age': 19, 'phone': '1234-5678'}

print("\n\n#### FOUR - ACCESSING DATA ####")
data = data2.copy()
print(data)
# {'name': 'Dmitri', 'age': 19, 'phone': '1234-5678'}

print(data['name'])
# Dmitri
print(data['age'])
# 19

data['name'] = 'Mary'
data['age'] = '28'
data['phone'] = '8765-4321'

print(data)
# {'name': 'Mary', 'age': 28, 'phone': '8765-4321'}

print("\n\n#### FIVE - NESTED DICTIONARIES ####")

contacts = {
    'dmitri.calle@mail.com': {
        'name': 'Dmitri',
        'phone': '1234-5678'
    },
    'miguel.souza@mail.com': {
        'name': 'Miguel',
        'phone': '8765-4321'
    }
}
print(contacts)

phone = contacts['miguel.souza@mail.com']['phone']

print(phone)
# 8765-4321


print("\n\n#### SIX - LOOP ####")
print(contacts)
print('*' * 20)

for key in contacts:
    print(key, contacts[key])
# dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'},
# miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}

print('*' * 20)

for key, value in contacts.items():
    print(key, value)
# dmitri.calle@mail.com: {'name': 'Dmitri', 'phone': '1234-5678'},
# miguel.souza@mail.com: {'name': 'Miguel', 'phone': '8765-4321'}