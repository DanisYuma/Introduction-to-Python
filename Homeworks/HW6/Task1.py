# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

import re

eq = '12 + 2 * 8 - (2 * 14) / 9 + 7'

sol = eval(eq)
print("%.2f" % sol)