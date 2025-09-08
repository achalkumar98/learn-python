# Nested Loop => The inner loop will Finish all of it's iteration before finishing on itreations of the outer loop

row = int(input("How many rows? : "))
columns = int(input("How many Columns? : "))
symbol = input("Enter a symbol to use : ")

for i in range(row):
    for j in range(columns):
        print(symbol, end="")
    print()
