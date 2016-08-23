# Intermediate Python Cheat Sheet

# Type Function
type(4)

# IsInstance Function
# Is Data X Type Y?
# Returns True or False
isinstance(1, float)

# Injecting Variables into a String
float_num = 5.0
string = 'Apple'
print '%s people to 1 %s' %(float_num,string)
# => 5.0 people to 1 Apple

print '%(language)s has %(number)i quote types.' %{"language": "Python", "number": 2}
# => Python has 2 quote types.

# Concatenate Two Strings
s1 = "What is the air-speed velocity"
s2 = "of an unladen swallow?"
s = s1 + " " + s2
        # OR
s = " ".join([s1, s2])

# Replace a substring with another substring
s = 'What is the air-speed velocity of an unladen swallow?'
s = s.replace("unladen", "unladen African")
# => 'What is the air-speed velocity of
#      an unladen African swallow?'
################################################################################

s = 'What is the air-speed velocity of an unladen African swallow?'

# Return the index of the first instance of a string
s.find("swallow")
# => 53

s[-8:]
# => 'swallow?'

s[s.find("swallow"):]
# => 'swallow?'

"swallow".upper()
# => "SWALLOW"

"SWALLOW".lower()
# => 'swallow'

"swallow".capitalize()
#=> 'Swallow'
################################################################################

s = 'What is the air-speed velocity of an unladen swallow?'
s.count(' ')
# => 9

s.count('swallow')
# => 1

s.count('what')
# => 0

s.count('What')
# => 1

################################################################################
lis = [0,1,2,3,4,5]

lis[1]
# => 1 not 0 as lists indexes start at 0

lis[0:4]
# => [0,1,2,3]

lis[4:]
# => [4,5]

lis[:4]
# => [0,1,2,3]

lis[-1]
# => 5

lis[-3:]
# => [3,4,5]

lis = [0,1,2,3,4,5]

lis[4] = 100
lis[4]
# => 100

lis[0:3] = ["Guido", "Van", "Rossum"]
lis[3:7] = ["created", "python,", "programming", "language,"]

lis
# => ['Guido', 'Van', 'Rossum', 'created', 'python,', 'programming', 'language,']

# Check if an element is in a list
"Van" in lis    # returns True
################################################################################

lis = [0,1,2,3,4,5]

# checking length
len(lis)      # returns 6

# sorting
sorted(lis)               # sorts the list

sorted(lis, reverse=True)
# reverse=True is an 'optional argument'

sorted(lis, True)
# error because optional arguments must be named

################################################################################

lis = [0,1,2,3,4,5]

# appending
lis[6] = 6
# error because you can't assign outside the existing range

list.append(6)     # list method that appends 6 to the end
lis = lis + ['hi']     # use plus sign to combine lists
# => [0, 1, 2, 3, 4, 5,'hi']

# Elements can be removed with the .remove method
lis.remove('hi')
# => [0, 1, 2, 3, 4, 5]

# Elements can be added to the end of a
# list using the .append method
lis.append("in 1991")

# Elements can be inserted into list
# This pushes the first arugment to the right
# Then inserts the second arugment
lis.insert(5,"a")
lis
# => [0, 1, 2, 3, 4, 'a', 5]
################################################################################

lis = [[1,2,3],[4,5,6],[7,8,9]]

# Lets try to access a particular number, say 6
lis[1][2]

numbers = [100, 45, 132.0, 1, 0, 0.3, 0.5, 1, 3]
################################################################################

# Long form using a for loop
lis1 = []
for x in numbers:
    if isinstance(x,int):
        lis1.append(5*x)

# Short form using list comprehension
lis2 = [x * 5 for x in numbers if isinstance(x, int)]

################################################################################

dct = {"Name": "Monty Python and the Flying Circus",
       "Description": "British Comedy Group",
       "Known for": ["Irreverant Comedy",
       "Monty Python and the Holy Grail"],
       "Years Active" : 17,
       "# Members": 6}

# Access an element within the list
dct["Years Active"]

# Add a new item to a list within the dictionary
dct["Known for"].append("Influencing SNL")

# Returns the keys
dct.keys()

# Returns the values
dct.values()

################################################################################

dct["Influence"] =
{ "Asteroids": [13681, 9618, 9619, 9620, 9621, 9622],
  "Technology": ["Spam", "Python", "IDLE (for Eric Idle)"],
  "Food": ["Monty Python's Holy Ale", "Vermonty Python"]}

# Accessing a nested dictionary item
dct["Influence"]["Technology"]

# A dictionary can be turned into a list
# Each key/value pair is an element in the list
dct.items()

# What do the ( ) that enclose each element of the list mean?
# --> Tuple.

################################################################################

# Tuples are denoted by ()
tup = ("Monty Python and the Flying Circus",
1969, "British Comedy Group")

type(tup)

# Elements can be accessed in the same way as lists
tup[0]

# You can't change an element within a tuple
tup[0] = "Monty Python"

# Tuples can be "unpacked" by the following
name, year, description = tup

# Tuples can be nested within one another
tup = ("Monty Python and the Flying Circus",
(1969, "British Comedy Group"))

################################################################################
# 
