def get_average():
    with open("files/data", 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(v.strip('\n')) for v in values]
    average = sum(values) / len(values)
    return average


average = get_average()
print(average)