# String Slicing => Create a SubString by extratinct Element from another string.
# indexing[] or slice()
# [start:stop:step]

# name = "ACHAL"
# print(name[0:2])

# name = "ACHAL"
# print(name[1:5])

# # If you skip start it will be assume and defalut = 0
# name = "ACHAL"
# print(name[:4])


# If you skip end it will be assume and defalut = length of string
# name = "ACHAL"
# print(name[2:])


# Using Step
# name = "ACHAL"
# print(name[::2])


# Reverse a String 
# name = "ACHAL"
# print(name[::-1])


# Slicing
website = "https://google.com"
slice = slice(8, -4)
print(website[slice])