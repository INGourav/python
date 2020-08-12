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
print ('a' <= 1)  # This will blow up coz both are differ type however
print ('a' == 1) # This will give us False coz it is not comparing here, it is only checking things
print (1 is 1)
print ('a' is 'a')
print (id('a') is id('a'))


