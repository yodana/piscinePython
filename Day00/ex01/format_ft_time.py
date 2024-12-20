import time
seconds = time.time()
print("Seconds since January 1, 1970 : ", end="")
print("{:,.3f}".format(seconds), end="")
print(" or ", end="")
print("{:.2e}".format(seconds), end="")
print(" in scientific notation")
print(time.strftime("%b %d %Y", time.gmtime()))