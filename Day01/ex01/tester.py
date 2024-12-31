from array2D import slice_me
family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# With start not a int value
print("With a start not an int value")
print(slice_me(family, "lol", 2))

###
print("With an end not an int value")
print(slice_me(family, 0, "lol"))

###
print("With a family not an list value")
print(slice_me("lol", 0, 2))

###
print("With a family list not the same size")
family = [[1.80],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))

###
print("Normal one")

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))

###
print("An other normal one")

print(slice_me(family, 1, -2))

###
print("An other other normal one")

print(slice_me(family, 1, -2))
