from load_image import ft_load
###
print("Ft load with path not str type")
print(ft_load(2))
###
print("Normal one")
print(ft_load("landscape.jpg"))

###
print("With an error in the path")
print(ft_load("landsca.jpg"))


###
print("With the wrong format")
print(ft_load("gif_test.gif"))