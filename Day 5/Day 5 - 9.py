# Escape sequences

print("This is a \"Python\" class.")
print('This is a "Python" class.')

a, b, c = input().split()
print("First number:", a)
print("Second number:", b)
print("Third number:", c)

print("first num: {2}, second num: {1}, third num: {0}".format(a, b, c))	#reverses
print("first num: {}, second num: {}, third num: {}".format(a, b, c))
print("first num: {1}, second num: {1}, third num: {1}".format(a, b, c))