#decoupling
input_feet_inches = input("Feat and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(input_feet_inches)

# print(feet_inches_tuple)
# print(type(feet_inches_tuple))
result = convert(f, i)

if result < 1:
    print("Kid is to small")
else:
    print("Kid can use slide")