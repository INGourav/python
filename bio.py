name = input("Name : ")
color = input("Fav Color : ")
age = int(input("Age : "))

print(name)
print("is" + str(age) + "years old")
print("and loves the color" + color + ".")

print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".")

print(name, "is", age, "yers old and loves color", color + ".", sep=", ")

print(name, "is", age, "yers old and loves color", color + ".", sep=" ")