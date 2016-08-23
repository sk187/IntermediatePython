# Exercise Code

# Write a method called e() that
#      1. Determines what data type the input is
#
#      2. It returns the input and datatype in a string
#      only for strings.
#        " INPUT is a <type DATATYPE>"
#
#        e('hi')
#        => "hi is a <type 'str'>"
#
#      If the input is a int or float return the following
#        e(5)
#        => 'Input cannot be an int'
#
#        e(5.0)
#        => 'Input cannot be a float'

# Starter Code
def e(input):
    datatype = type(input)
    if .... :
    	return "Input cannot be an int"
    elif ... :
    	return "Input cannot be a float"
    else:
    	return "%s is a %s" %(input, datatype)
################################################################################

# s1 = 'What is the air-speed velocity'
# s2 = 'of an unladen swallow?'
#
# 1. Combine s1 and s2 into a new varible called s
#
# 2. Replace "unladen" with "unladen african"
#
# 3. Capitalize "african" by slicing it from s
#
# 4. Count how many spaces there are in s
#
# 5. Get the index of swallow in s
#
# 6. Print a statement with the correct counts so that
# "There are __ spaces and sallow is at the __ index"
#
# With either varible string injection method we learned
#
# Bonus
# 7. Using string slicing, replace, capitalize african in s

################################################################################

# 1. Create a list of the first names
# of your family members.
#
# 2. Print the name of the last person in the list.
#
# 3. Print the length of the name of the first
# person in the list.
#
# 4. Change one of the names from their real name
# to their nickname.
#
# 5. Append a new person to the list.
#
# 6. Change the name of the new person to lowercase
# using the string method 'lower'.
#
# 7. Sort the list in reverse alphabetical order.
#
# 8. Bonus: Sort the list by the length of the names
# (shortest to longest).

################################################################################

# EXERCISE 1:
# Given that: letters = ['a', 'b', 'c']
# Write a list comprehension that returns: ['A', 'B', 'C']
#
# EXERCISE 2 (BONUS):
# Given that: word = 'abc'
# Write a list comprehension that returns: ['A', 'B', 'C']
#
# EXERCISE 3 (BONUS):
# Given that: fruits = ['Apple', 'Banana', 'Cherry']
# Write a list comprehension that returns: ['A', 'B', 'C']

################################################################################

# family = {'dad':'Homer', 'mom':'Marge', 'size':2,
# 'kids': ['bart', 'lisa']}
#
# 1. Print the name of the mom.
# 2. Change the size to 5.
# 3. Add 'Maggie' to the list of kids.
# 4. Fix 'bart' and 'lisa' so that
# the first letter is capitalized.
#
# Bonus: Do this last step using a list comprehension.

################################################################################
