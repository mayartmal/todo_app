import glob

myfiles = glob.glob("../files/*.txt")

print(myfiles)

for filepath in myfiles:
    print(filepath + " content is:")
    with open(filepath, 'r') as file:
        print((file.read()))