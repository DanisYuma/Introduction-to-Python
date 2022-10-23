# Вычислить число c заданной точностью d

# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

A = float(input('Enter number A> '))
d = input('Enter precision d> ')
prec = d.count('0')
print()
print(f'Number {A} with a precision {d} is {round(A, prec)}')