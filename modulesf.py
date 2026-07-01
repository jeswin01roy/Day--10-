import math
print(math.sqrt(81))
print(math.factorial(5))
# area of a circle
r= int(input("enter the radious of circle:"))

area=lambda r: math.pi * (r**2)

print(area(r))
