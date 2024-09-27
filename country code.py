print("\033c")

country_code = {
    'India' : '0091',
    'Australia' : '0025',
    'Bangladesh' : '00880',
    'Nepal' : '00977',
}


print("Country code for India -")
print(country_code.get('India' , 'Not found'))

print("Country code for Aistralia -")
print(country_code.get('Australia' , 'Not found'))

print("Country code for Bangladesh -")
print(country_code.get('Bangladesh' , 'Not found'))

print("Country code for Nepal -")
print(country_code.get('Nepal' , 'Not found'))

print("Country code for Japan -")
print(country_code.get('Japan' , 'Not found'))