# Operator Bitwise, Operasi biner, binary

a = 10
b = 5

# bitwise OR (|)
c = a | b
print("\n======OR=====")
print("nilai :",a," , binary :",format(a,"08b"))
print("nilai :",b," , binary :",format(b,"08b"))
print("____________________________(|)")
print("nilai :",c," , binary :",format(c,"08b"))

# bitwise AND (&)
c = a & b
print("\n======AND=====")
print("nilai :",a," , binary :",format(a,"08b"))
print("nilai :",b," , binary :",format(b,"08b"))
print("____________________________(&)")
print("nilai :",c," , binary :",format(c,"08b"))

# bitwise XOR (^)
c = a ^ b
print("\n======XOR=====")
print("nilai :",a," , binary :",format(a,"08b"))
print("nilai :",b," , binary :",format(b,"08b"))
print("____________________________(^)")
print("nilai :",c," , binary :",format(c,"08b"))

# bitwise NOT (~)
c = ~a
print("\n======NOT=====")
print("nilai :",a," , binary :",format(a,"08b"))
print("____________________________(~)")
print("nilai :",c," , binary :",format(c,"08b"))
c = ~b
print("nilai :",b," , binary :",format(b,"08b"))
print("____________________________(~)")
print("nilai :",c," , binary :",format(c,"08b"))
