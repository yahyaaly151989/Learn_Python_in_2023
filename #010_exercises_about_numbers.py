# ============================ Exercises About Numbers =============================
# 1. What is the type of the following variable
x = -5j
print(x)
print(type(x))
# int
# complex
# real
# imaginary
print("########################################################")

# 2. What is the output of print(abs(-45.300))
print(abs(-45.300))
print("########################################################")

# 3. What is the output of the following number conversion
z = complex(1.25)
print(z)
print("########################################################")

# 4. What is the output of the following round() function call
print(round(100.2567, 3))
print(int(round(100.756)))
print(round(100.000556, 3))
print("########################################################")

# 5. What is the output of the following code
print(int(2.999))
print("########################################################")

# 6. What is the output of the following code
a = 10 + 3j
print(float( a.imag ))
print("########################################################")

# 7. What is the output of the following code
a = 10 + 3j
# print( int( complex( a.imag ) ) ) # error
print("########################################################")

# 8. What is the output of the following code
a = 10.9
print( int(  complex(a).imag  ) )
print("########################################################")

# 9. What is the output of the following code
a = 5 - 3j
print( pow( int(a.real), int(abs(a.imag)), int(a.real) ) )

print(pow(5, 3, 5))
print("########################################################")

# 10. What is the output of the following code
a = 5 - 3j
print(type(a.real))
print("########################################################")

# ==================================== End ==========================================
