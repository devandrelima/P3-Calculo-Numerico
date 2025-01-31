import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#FONTE DA IDEIA
#DINÂMICA DA COVID-19 DESCRITA PELO MODELO
#SIR: estudo de caso para três cidades brasileiras

# Definição do modelo SIR
def sir_model(t, y, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# PARÂMETROS DO MODELO
# Dados de Varginha/MG
beta = 0.3762  # Taxa de transmissão
gamma = 0.3202  # Taxa de recuperação

# Condições iniciais em %
S0 = 0.99  # Suscetível
I0 = 0.01  # Infectada
R0 = 0.0   # Recuperada

# Intervalo de tempo para a simulação
t_span = (0, 160)
t_eval = np.linspace(*t_span, 1000)

# Resolvendo o sistema de EDOs
sol = solve_ivp(sir_model, t_span, [S0, I0, R0], args=(beta, gamma), t_eval=t_eval)

# Extraindo as soluções
S, I, R = sol.y

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(sol.t, S, label="Suscetíveis (S)", color='blue')
plt.plot(sol.t, I, label="Infectados (I)", color='red')
plt.plot(sol.t, R, label="Recuperados (R)", color='green')
plt.xlabel("Tempo")
plt.ylabel("Proporção da População")
plt.title("Dinâmica da COVID-19 usando o Modelo SIR")
plt.legend()
plt.grid()
plt.show()