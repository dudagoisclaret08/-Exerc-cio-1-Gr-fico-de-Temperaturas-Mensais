import matplotlib.pyplot as plt 

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']   ### eixo X
temperatura_cidade_a = [28, 27, 26, 24, 21, 19, 18, 19, 21, 23, 25, 27] ### eixo Y - cidade A
temperatura_cidade_b = [32, 31, 29, 26, 23, 21, 20, 21, 23, 26, 28, 30] ### eixo Y - cidade B

fig, ax = plt.subplots(figsize=(10, 5))  ### cria a figura e os eixos

### desenha uma linha para A e outra para B
ax.plot(meses, temperatura_cidade_a, marker='o', color='tab:blue', label='Cidade A', linewidth=2)
ax.plot(meses, temperatura_cidade_b, marker='s', color='tab:orange', label='Cidade B', linewidth=2)

#### nome dos eixos e título
ax.set_title('Temperatura média mensal — Cidade A vs Cidade B', fontsize=14)
ax.set_xlabel('Mês', fontsize=12)
ax.set_ylabel('Temperatura (°C)', fontsize=12)

#### mostra a legenda e ativa a grade
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()  ## arruma espaço
plt.show()          ## mostra o gráfico
