name = 'IGOR'
age = 52
print('Hi World')
print('My name is Igor.\n', "I'm", age, 'years old')
print('Hi.\'How are you')

print(name+ ' is a male')
print(name+ ' is ', age)
print(name+ ' is from Macedonia')
print(name.isupper())
name_leight = len(name)
name1 = 'Igor'
print(name1.index('r'))

# 
my_list = [1,2,3,4,5]
print(len(my_list)) # same as double varibles
my_list_leight = len(my_list)
print(my_list_leight)


# The replace() method in Python is used to create a new string by replacing all occurrences of a specified substring with another substring. It takes two arguments: the substring to be replaced and the substring to replace it with. It returns a new string with the replacements made.

# Here's how you can use the replace() method:
first_text = 'Hellow Igor'
replaced_text = first_text.replace('Igor', 'World')
print(replaced_text)

#
def example_function(arg1, **kwargs):
    print("arg1:", arg1)
    print("kwargs:", kwargs)

example_function(arg1=1, key1="value1", key2="value2")
