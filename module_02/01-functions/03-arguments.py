
def save_car(model, brand, year, license_plate):
    # saves car to the database...
    print(f"Car successfully inserted! \n{brand} / {model} / {year} / {license_plate}")

###

# Ferrari / LaFerrari / 2013 / XYZ-0001
print('1:')
save_car("Ferrari", "LaFerrari", 2013, "XYZ-0001")
# LaFerrari / Ferrari / 2013 / XYZ-0001

print('\n2:')
save_car(brand="Ferrari", model="LaFerrari", year=2013, license_plate="XYZ-0001")
# Ferrari / LaFerrari / 2013 / XYZ-0001

print('\n3:')
save_car(**{"brand": "Ferrari", "model": "LaFerrari", "license_plate": "XYZ-0001", "year": 2013})
# Ferrari / LaFerrari / 2013 / XYZ-0001