# ============================ Data Types Overview ============================
# 1- What is Data Type?
# ---> A data type, in programming, is a classification that specifies which type of 
#      value a variable has and what type of mathematical, 
#      relational or logical operations can be 
#      applied to it without causing an error. 

# ---> Data is stored in computer memory.
# ---> We use variables to refer to this data.
name = "Yehya"
print(name)
print("=" * 75)

# 2- What are Data Types in Python?
# ---> We use type(data) to know the type of data.

# ---> int => Integer
print( type(10) )
print( type(-90) )
print("#" * 75)

# ---> float => Float
print( type( 10.9 ) )
print( type( -8.79 ) )
print("#" * 75)

# ---> complex => Complex
print( type( 2 - 2j ) )
print( type( 12 + 90j ) )
print("#" * 75)

# ---> str => String
print( type( "Yehya" ) )
print( type( 'Ahmad' ) )
print("#" * 75)

# ---> list => List
print( type(  [1, 2, 3]  )  )
print("#" * 75)

# ---> tuple => Tuple
print( type(  (1, 2, 3)  )  )
print("#" * 75)

# ---> set => Set
print( type(  {1, 2, 3}  )  )
print("#" * 75)

# ---> dict => Dictionary
print( type(  {"one": 1, "two": 2}  )  )
print("#" * 75)


# ---> bool => Boolean
print( type( True ) )
print( type( False ) )
print( type( 10 == 10 ) )
print("#" * 75)

# ---> None => NoneType
print( type( None ) )
print("#" * 75)