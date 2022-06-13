#mutabilityInPython
# mutable default parameters in Python (BAD idea!)

from typing import List

a =  []
b = a
 
print(id(a))
print(id(b))
# output is exactly the same. Same objects exactly.

a.append(35)

print(a)
print(b)

# a and b are references to the same object
# a list is "mutable"... tuples are IMMUTABLE

myTuple = ()
# myTuple.append() # tuple has no attribute "append".

a = 8598
print(f" value of a is {a}")


