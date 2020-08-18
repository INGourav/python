# Normal print command
print("Hello, World!")

# sending string in var
mystr = "Gourav"
print(mystr)

# adding something in var
mystr += " kumar"
print(mystr)

# Changing var type
mystr = 1
print(mystr)

# multi line string
mystr = '''
This is a tripe quoted
multi-line string
'''
print(mystr)

# Adding two string
mystr = "pass" + "word"
print(mystr)

# Adding multiple same thing in string
mystr = 4 * "Ha"
print(mystr)
mystr = "Ha" * 4
print(mystr)

# Fiding place of letter in string
mystr = "Gourav Kumar"
print (mystr.find('G'))
print (mystr.find('ar'))

# Chaning string into BLOCK and small
mystr = "Gourav Kumar"
print (mystr.lower())
print (mystr.upper())

# Play with spaces in string
print ("Gourav\tKumar")
print ("Gourav\nKumar")
print ("Gourav\\nKumar")

# USing quotes in strings
print("'Gourav' Kumar")
print('"Gourav" Kumar')
print("\"Gourav\" Kumar")

# Numeric operator
print (2+2)          # whole
print (2.0+2.0)      # Float
print (4.5e9)        # Using e
print (4.5 *(10**9)) # Using power
print (2 + 2.0)      # will give float
print (5/3)          # entire 
print (5//3)         # only even numner divide
print (5%3)          # whole number reminder
print (6/3)          # float number

# Boolean and number system
print (~1)
a = 0b010
print (a)
g = bin(a)
print(g)
g = ~a
print (g)
g = bin(~a)
print (g)

a = 0b1001
b = 0b1100
print (bin (a|b))  # OR opereator it will check 1 after ob so if anyone has one it is true (1)
print (bin (a&b))  # And operator it will check if both has one then it will give true (1)
print (bin (a^b))  # xor operator it will check if both lines same numner either zero or one then true (1)

# Shifting operator
# Right shift
a = 0b110
print ( bin(a >> 2)) # lets suppose if we have decimal point in the vert last and we want remove numner from right to left
print ( bin(a >> 4)) # If we move very far then it will return zero to us

# Left shift , This will zero in the last (zero padding)
a = 0b110
print ( bin(a << 2))
print ( bin(a << 4))

# Comparison
print (1<2)
print (1>2)
print (1>=2)
print (1<=2)
print (1<=2.0)
print ('a'<'b')
print ('a'>'b')
print ('a'<='b')
print ('a'>='b')
# print ('a' <= 1)  # This will blow up coz both are differ type however
print ('a' == 1) # This will give us False coz it is not comparing here, it is only checking things
print (1 is 1)
print ('a' is 'a')
print (id('a') is id('a'))

# Parenthesis and List/Dictionary/Set literals
# Accessing attributes (subscription, slicing, function/method call, attribute reference)
# Exponentiation (**)
# Positive, Negative, and bitwise complement
# Multiplication *, Division /, Floor Division //, Modulo %
# Addition +, Subtraction -
# Bitwise Shifts << & >>
# Bitwise AND &
# Bitwise XOR ^
# Bitwise OR |
# Comparison operators (in, not in, is, is not, <, >, <=, >=, ==, !=)
# Boolean NOT not
# Boolean AND and
# Boolean OR or
# Conditions if

#Typecating

print (1)
print (float(1))
print (int(1.2))
print (str(1.2))
 
print (1 and 0) # This will return flase value which is 0
print ('This' and 'That') # this will return false value too
print ('This' and 0 and 'That') # But this will return first false valuw which is 0 so it will not consider 'That'
print (0.0 and 1) # if first value is false them it will return false value so make sure we add true first

# Input function

input() # to input anything
favorite = input("Fav Color : ") # use to print message and store value in variable
favorite # use to see fav color

# Immutability, something can't be changed

mystr = 'testing'
print(mystr.capitalize())
print(mystr)
print(id(mystr))
print(id('testing'))
otherstrng = 'testing'
print(id(mystr) == id(otherstrng)) # both have the same id and it will return true as py knows it has already created

# len or length function
'testing'
mystr = 'testing'
print(len(mystr))

# Indexing and Slicing

test_str = 'testing'
test_str[0]
test_str[10]  # it will blow up as we have less length string
test_str[len(test_str) - 1]
test_str[-1]
test_str[-4]
test_str[-8]  # it will blow up as we have less length string

# If we want to get a subsection of our string then we'll do what is called slicing. Slicing allows us to specify the index of the first element that we would like, followed by the index just beyond the last item that we'd like. We separate these indexes by using a colon (:)
test_str[0:2]
test_str[3:5]

# If we'd like to get all of the items after our starting index then we can use the length of the string as our second index, even though it's technically out of range. Or we can simply put nothing after the colon:
test_str[2:len(test_str)]
test_str[2:]

# The last thing to mention about slicing is that there is a third number that we can use: the "step" value. By default, this value is 1 and just means that we'll go one-by-one through the sequence. But we can change this to grab every other item if we'd like by adding a second colon and the step size that we'd like to use:
test_str
test_str[1:5:2]
test_str[1::2]

# One neat thing that we can do with this step option is stepping backward by using a negative step value. We can reverse an entire string by leaving off the start and end indexes and setting the step value to -1:
test_str[::-1]

# List
mylist=[1,2,3] # all are same
newlist=['a',1,1.0,False] # we can use multiple type value in list

# List are mutable so means we can modify, So it is not similar to string and other thing
mylist[0]='g' # to replace a item in list
mylist
mylist+[8,9,10] # to concat something in list
mylist+=[8,9,10] # to add something in list
mylist[1:3]=['b','c'] # this will add b and c in the list at 2nd and 3rd position
newlist[0:]=[] # this will delete everything after zero value so means only we will have 'a' in the list
testlist=['a','b','c','d',5,6,7]
testlist[4:]=[]
testlist
del mylist[0] # del is not a function it is a statment thats why it has no ()
mylist
# if we use {del mylist} then it will delete eberything entire variable.


