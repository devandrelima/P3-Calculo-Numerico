import numpy as np

# função √(1-x²)
def F(x):
    return np.sqrt(1 - x**2)

# simpson 1/3
def Simpson1_3(F, a, b, n):
    h = (b - a) / n # tamanho dos passos
    x = np.linspace(a, b, n+1) # array de pontos (de a até b) igualmente espaçados

    y = F(x) # valores da função nos pontos

    integral = h/3 * (y[0] + 4*np.sum(y[1:n:2]) + 2*np.sum(y[2:n-1:2]) + y[n])

    return integral

# simpson 3/8
def Simpson3_8(F, a, b, n):
    h = (b - a) / n # tamanho dos passos
    x = np.linspace(a, b, n+1) # array de pontos (de a até b) igualmente espaçados

    y = F(x) # valores da função nos pontos

    integral = 3*h/8 * (y[0] + 3*np.sum(y[1:n:3]) + 3*np.sum(y[2:n:3]) + 2*np.sum(y[3:n-1:3]) + y[n])

    return integral

# intervalo de integração
a = -1
b = 1

# subintervalos
n1 = 8  # simpson 1/3
n2 = 9  # simpson 3/8

integralSimpson1_3 = Simpson1_3(F, a, b, n1) # letra a
integralSimpson3_8 = Simpson3_8(F, a, b, n2) # letra b

print("Simpson 1/3: ", integralSimpson1_3)
print("Simpson 3/8: ", integralSimpson3_8)