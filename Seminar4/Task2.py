# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python

import math

A = int(input('Enter A> '))
B = int(input('Enter B> '))
C = int(input('Enter C> '))

D = B ** 2 - 4 * A * B
print('discriminant = %.2f' % D)

if D > 0:
    x1 = (- B + math.sqrt(D)) / (2 * A)
    x2 = (- B - math.sqrt(D)) / (2 * A)
    print('x1 = %.2f \n x2 = %.2f' % (x1, x2))
elif D == 0:
    x = - B / (2 * A)
    print('x = %.2f' % x)
else:
    print('No roots')