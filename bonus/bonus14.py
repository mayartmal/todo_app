#decoupling
from bonus14mods import convert
from bonus14mods import parse

input_feet_inches = input("Feat and inches: ")

parsed = parse(input_feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed["feet"]} feet "
      f"and {parsed["inches"]} "
      f"is equal to {result} meters")



if result < 1:
    print("Kid is to small")
else:
    print("Kid can use slide")