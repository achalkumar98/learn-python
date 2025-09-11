# Set => A set is collections which is unordered, unindexed. No Duplicate Values.
# A set is accutally Faster than List.

# Lets see some Example.


# Example - 1
# utensils = {"fork", "spoon", "knife"}
# for x in utensils:
#     print(x)   # The order of output will not be same



# Example - 2
# utensils = {"fork", "spoon", "knife", "knife"}
# for x in utensils:
#     print(x)    # it will not print the duplicate value




# Method in sets
# 1. Add
# utensils = {"fork", "spoon", "knife"}
# utensils.add("napkins")
# for x in utensils:
#     print(x)


# 2. Remove
# utensils = {"fork", "spoon", "knife"}
# utensils.remove("fork")
# for x in utensils:
#     print(x)



# 3. Clear
# utensils = {"fork", "spoon", "knife"}
# utensils.clear()
# for x in utensils:
#     print(x)



# 4. Update
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup"}
# utensils.update(dishes)
# for x in utensils:
#     print(x)

# OR

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup"}
# dishes.update(utensils)
# for x in dishes:
#     print(x)



# 5. Union 
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup"}
# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)



# 5. Compare 
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
# print(dishes.difference(utensils))

# OR

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "Knife"}
# print(utensils.difference(dishes))


# 7. Intersections
# utensils = {"fork", "spoon", "knife", "bowl"}
# dishes = {"bowl", "plate", "cup", "Knife"}
# print(utensils.intersection(dishes))