# Dictionary => A changable, unordered collections of unique key value pairs fast beacuse they use hashing, 
# allow us to access a value quickly

# let's see some example

# Example 1 -
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# print(capitails['Russia'])


# Example 2 -
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# print(capitails['Germany']) # It will Print An Error

# To handle this error
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# print(capitails.get('Germany'))
   

# Example 3 - For print Keys
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# print(capitails.keys())



# Example 4 - For print Values
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# print(capitails.values())


# Example 5 - For print entire dictinory
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# print(capitails.items())




# Example 6 - Another way to print key value pairs using for loop
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}

# for key,value in capitails.items():
#     print(key,value)



# Methods in Dictionay
# 1. Update
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# capitails.update({'Germany':'Berlin'})

# for key,value in capitails.items():
#     print(key,value)




# Suppose we want to Updates in USA 
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# capitails.update({'USA':'Las Veges'})

# for key,value in capitails.items():
#     print(key,value)



# Remove from Dictionary
# capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
# capitails.pop('China')

# for key,value in capitails.items():
#     print(key,value)



# Clear from Dictionary
capitails = {'USA':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}
capitails.clear()

for key,value in capitails.items():
    print(key,value)