# ============================ Numbers and Methods ============================
# A- What is Numbers in Python?
# ---> Python has three built-in numeric data types: 
# -----> Integers
# -----> Floating-Point Numbers
# -----> Complex Numbers

# ---> int => Integer
print( type( 10 ) )
print( type( -10 ) )
print("=" * 75)

# ---> float => Floating-Point Numbers
print( type( 10.9 ) )
print( type( -10.89 ) )
print("=" * 75)

# ---> comples => Complex Numbers
print( type( 10 + 2j ) )
print( type( -4.8 + 4j ) )
print( type( 4.1 - 8.9j ) )
print("=" * 75)

# ---> We can convert int to float and complex using float() and complex() methods.
i = 15
f = float( i )
print( f )
print( type( f ) )

c = complex( i )
print( c )
print( type( c ) )
print("=" * 75)

# ---> We can convert float to int and complex using int() and complex() methods.
f = 15.9
i = int( f )
print( i )
print( type( i ) )

c = complex( f )
print( c )
print( type( c ) )
print("=" * 75)

# ---> We cannot convert complex to int or float
c = 10 + 2j

real_part = c.real
print( real_part )
print( type( real_part ) )

imaginary_part = c.imag
print( imaginary_part )
print( type( imaginary_part ) )
print("=" * 75)

# B- Arithmetic Operators:
print(10 + 2)
print(10 - 8)
print(20 * 3)
print(100 / 4)
print(103 // 4) 
print(104 // 4)
print(2 ** 4) # 2 * 2 * 2 * 2 
print(5 ** 3) # 5 * 5 * 5
print(10 % 3) # 1
print(26 % 3) # 2
print(4 % 2) # 0
print("=" * 75)

# C- Numbers Methods:
# ---> Python has a few built-in functions that you can use to work with numbers.

# round() => Rounding numbers to some number of decimal places
a = 9.75
b = round(a)
print(b)

a = 7.7
b = round(a)
print(b)

c = 9.226
d = round(c, 2)
d = round(c, 1)
print(d)

# abs() => Getting the absolute value of a number
a = -10
b = abs(a)
print(b)
print("=" * 75)

# pow() => Raising a number to some power
a = pow(2, 3)
print(a)
a = pow(4, 4)
print(a)

a = pow(3, 3, 2)
print(a)
print("=" * 75)

# min() => The min number in a collection of numbers
# max() => The max number in a collection of numbers
print(min(1, 2, -10, 4, -100, 100))
print(max(1, 2, -10, 4, -100, 100))
print("=" * 75)

# sum() => Sum of numbers
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 10))
print(sum((2, 5, 6), 8))
print("=" * 75)

# range() => Range of numbers
print(range(0, 10))
print("=" * 75)

# ================================== End ======================================
