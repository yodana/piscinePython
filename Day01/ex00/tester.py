from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
#Error type limit value
print(bmi, type(bmi))
print(apply_limit(bmi, "lol"))

#Error values in list bmi
height = [2.71, "lol"]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))

#Normal one
height = [2.71, 1.15]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

#Division by 0
height = [2.71, 0]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
