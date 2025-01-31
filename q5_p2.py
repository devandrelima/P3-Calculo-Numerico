#Dados de Varginha-MGimport numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

#E se... Pudermos simular o impacto de doeças na sociedade apartir de uma pequena
#variação do modelo SIR, que também leve em conta a taxa de mortalidade?

# Definição do modelo SIR com fatalidades
def pandemic_model(t, y, beta, gamma, delta):
    S, I, R, D = y  # Suscetíveis, Infectados, Recuperados, Mortos
    dSdt = -beta * S * I  # Novos infectados
    dIdt = beta * S * I - gamma * I - delta * I  # Infectados que se recuperam ou morrem
    dRdt = gamma * I  # Recuperados
    dDdt = delta * I  # Mortes
    return [dSdt, dIdt, dRdt, dDdt]

# IBGE, senso de 2024
total_population_brazil = 212.6e6  # 212,6 milhões de habitantes

# AJUSTES DA DOENÇA
beta = 0.3  # Taxa de infecção (probabilidade de transmissão)
gamma = 0.1  # Taxa de recuperação
delta = 0.02  # Taxa de mortalidade dos infectados

#Peste de Atenas (430-427 a.C.)
# beta = 0.03
# gamma = 0.65
# delta = 0.35

#Mortes estimadas: 25% a 35% da população de Atenas.

#Peste Negra (1347-1353)
# beta = 0.05
# gamma = 0.10
# delta = 0.90

# Europa, Ásia e Norte da África
#Mortes estimadas:  30% a 60% da população europeia.

#Gripe espanhola (1918-1919)
# beta = 0.03
# gamma = 0.20
# delta = 0.80

# Nivel Mundial
# Taxa de mortalidade: No pior cenário, a taxa de mortalidade foi de 10% a 20% entre os infectados, dependendo da região e das condições de saúde.

#Ebola (2013-2016)
# beta = 0.025
# gamma = 0.34
# delta = 0.66

# África Ocidental, como Guiné, Libéria e Serra Leoa
# Taxa de mortalidade: 40% a 50% (chegando a 90% em algumas áreas).


# Condições iniciais em %
S0 = (total_population_brazil - 1000) / total_population_brazil  # População suscetível inicial
I0 = 1000 / total_population_brazil  # 1000 infectados iniciais
R0 = 0.0  # Nenhum recuperado no início
D0 = 0.0  # Nenhuma morte inicial

# Intervalo de tempo
t_span = (0, 730)  # Simulação de até 2 anos (730 dias)
t_eval = np.linspace(*t_span, 1000)  # Tempo de avaliação

# Resolvendo o sistema de EDOs
sol = solve_ivp(
    pandemic_model, t_span, [S0, I0, R0, D0], args=(beta, gamma, delta),
    t_eval=t_eval
)

# Extraindo as soluções
S, I, R, D = sol.y

# Plotando os resultados
plt.figure(figsize=(12, 7))
plt.plot(sol.t, S, label="Suscetíveis (S)", color='blue')
plt.plot(sol.t, I, label="Infectados (I)", color='red')
plt.plot(sol.t, R, label="Recuperados (R)", color='green')
plt.plot(sol.t, D, label="Mortos (D)", color='black', linestyle='dashed')
plt.xlabel("Tempo (dias)")
plt.ylabel("Proporção da População do Brasil (4,9 milhões)")
plt.title("Simulação de Epidemia no Brasil usando Modelo SIRD")
plt.legend()
plt.grid()
plt.show()

# Exibir tempo final da pandemia
sol.t[-1]
