# Function => A Function is a block of code Which is Executed Only When its Called

# Lets Seen an Example =>

# Example - 1
# def hello():
#     print("Hello!")
# hello()


# If we want to Call 3 times
# Example - 2
# def hello():
#     print("Hello!")
# hello()
# hello()
# hello()



# Parameters & Arguments
# Example - 3
# def hello(name):
#     print("Hello " +name)
# hello("Achal")



# Example - 4
# def hello(first_name, last_name):
#     print("Hello " +first_name + " " + last_name)
# hello("Achal", "Kumar")




# Example - 5
def hello(first_name, last_name, age):
    print("Hello " +first_name + " " + last_name)
    print("You are "+str(age)+" Years Old!")
hello("Achal", "Kumar", 27)