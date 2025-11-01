
print("### FORMAT STRINGS ###\n")

name = "Dmitri"
age = 19

print("#### OLD STYLE (%) ####")
print("Hi, my name is %s and I am %d years old!" % (name, age))
# "Hi, my name is Dmitri and I am 19 years old!"

print("\n#### FORMAT 1 ({\}\) ####")
print("Hi, my name is {} and I am {} years old!".format(name, age))
# "Hi, my name is Dmitri and I am 19 years old!"
print("Hi, my name is {1} and I am {0} years old!".format(age, name))
# "Hi, my name is Dmitri and I am 19 years old!"

print("\n#### FORMAT 2 ({\}\) ####")
print("Hi, my name is {name} and I am {age} years old!".format(name=name, age=age))
# "Hi, my name is Dmitri and I am 19 years old!"

data = {"name": "Dmitri", "age": 19}
print("Hi, my name is {name} and I am {age} years old!".format(**data))
# "Hi, my name is Dmitri and I am 19 years old!"

print("\n#### F-STRING (f{\}\) ####")
print("Hi, my name is {name} and I am {age} years old!")
# "Hi, my name is Dmitri and I am 19 years old!"

PI = 3.14159
print(f"\n{PI}")

print(f"The Pi is: {PI:2f}")
# The Pi is: 3.14

print(f"The Pi is: {PI:10.2f}")
# The Pi is:           3.14