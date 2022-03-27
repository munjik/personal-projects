# import numpy as np
# def powerup(i):
#     if i == 1:
#         return 1
#     else:
#         return np.square(i) + powerup(i - 1)
# print(powerup(4))

# def great(a,b):
#     while a!= 0 and b != 0:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return max(a,b)
# print(great(21,35))

strings = ['a', 'bc', 'def', 'ghij']
output = ""
for x in strings:
    if len(x) % 2 == 0:
        continue
    output += x
print(output)
