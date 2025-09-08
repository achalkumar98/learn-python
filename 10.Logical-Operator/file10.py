# Logical Operator - (And, Or, Not) => Ussed to check if two or more Conditional Statement

# AND => Both condition will be true
# temperature = int(input("What is the temperature Outside? : "))

# if temperature >= 0 and temperature <= 30:
#     print("Temperature is good today")
#     print("Go Outside")



# OR => any condition will be true
# temperature = int(input("What is the temperature Outside? : "))

# if temperature >= 0 and temperature <= 30:
#     print("Temperature is good today")
#     print("Go Outside")
# elif temperature < 0 or temperature > 30:
#     print("Temperature is bad today")
#     print("Stay inside")




# NOT => any condition will be true
temperature = int(input("What is the temperature Outside? : "))

if not(temperature >= 0 and temperature <= 30):
      print("Temperature is bad today")
      print("Stay inside")

elif not(temperature < 0 or temperature > 30):
          print("Temperature is good today")
          print("Go Outside")
  

