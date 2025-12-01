import math
radius = [1, 2, 3 ,4]
res = map(lambda r:math.pi*r**2, radius)
for i in res:
    print('The area of circle is:', i)