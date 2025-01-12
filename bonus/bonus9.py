password = input("Enter new password: ")

#check conditions
conditions = dict()
conditions['length'] = len(password) >= 8
conditions['digit'] = any(char.isdigit() for char in password)
conditions['upper'] = any(char.isupper() for char in password)
print(conditions)



if all(conditions.values()):
    print("It is strong password")
else:
    print("It is weak password")
