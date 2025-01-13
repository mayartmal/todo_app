try:
    width = float(input("Width: "))
    length = float(input("Length: "))
    if width == length:
        exit("It is a square")
    area = width * length

    print(area)
except ValueError:
    print("Provide a numeric value")

