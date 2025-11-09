
# by default, arguments can be passed to a Python function either by position or explicitly by name. for better readability and performance, it makes sense to restrict how arguments can be passed, so a developer only needs to look at the function definition to determine whether items are passed by position only, by position and name, or by name only.

print('### POSITIONAL ONLY ###')

def create_car_positional(model, year, license_plate, /, brand, engine, fuel):
    print(f'{model} / {year} / {license_plate} / {brand} / {engine} / {fuel}')

###

create_car_positional("LaFerrari", 2013, "DMT-2402", brand="Ferrari", engine="V12 Hybrid", fuel="Petrol")
# LaFerrari / 2013 / DMT-2402 / Ferrari / V12 Hybrid / Petrol

# create_car_positional(model="LaFerrari", year=2013, license_plate="XYZ-0001", brand="Ferrari", engine="V12 Hybrid", fuel="Petrol")
# invalid, TypeError

##########

print('\n\n### KEYWORD ONLY ###')
def create_car_keyword(*, model, year, license_plate, brand, engine, fuel):
    print(f'{model} / {year} / {license_plate} / {brand} / {engine} / {fuel}')

###

create_car_keyword(model="LaFerrari", year=2013, license_plate="XYZ-0001", brand="Ferrari", engine="V12 Hybrid", fuel="Petrol")
# LaFerrari / 2013 / DMT-2402 / Ferrari / V12 Hybrid / Petrol

# create_car_keyword("LaFerrari", 2013, "DMT-2402", brand="Ferrari", engine="V12 Hybrid", fuel="Petrol")
# invalid, TypeError

##########

print('\n\n### BOTH ###')

def create_car_both(model, year, license_plate, /, brand, *, engine, fuel):
    print(f'{model} / {year} / {license_plate} / {brand} / {engine} / {fuel}')

###

create_car_both("LaFerrari", 2013, "DMT-2402", "Ferrari", engine="V12 Hybrid", fuel="Petrol")
# LaFerrari / 2013 / DMT-2402 / Ferrari / V12 Hybrid / Petrol

create_car_both("LaFerrari", 2013, "XYZ-0001", brand="Ferrari", engine="V12 Hybrid", fuel="Petrol")
# LaFerrari / 2013 / DMT-2402 / Ferrari / V12 Hybrid / Petrol