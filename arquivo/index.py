import matplotlib.pyplot as plt # type: ignore

y = []
# Entrada dos 10 valores de I
print("Digite I:")
for i in range(1, 11):
    numero = float(input(f"Digite I{i}º: "))
    y.append(numero)
x = list(range(1, 11))

# Criando o gráfico

plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title("Gráfico da Resistencia")
plt.xlabel("E(V)")
plt.ylabel("I(mA)")
plt.grid(True)
plt.show()

#calculo de erro: m: m=I/E -> R=1/m -> R=E/I

r = []
for i in range(10):
    if y[i] != 0:
        r.append(x[i]*(10**3) / y[i])
    else:
        r.append(float('inf'))

print("Tabela de comparaçaõ")
print("E(V) | I(mA) | R(ohm)")
for i in range(10):
    print(f" {i+1} | {y[i]} | {r[i]}")

plt.plot(x, r, marker='s', linestyle='--', color='red')
plt.title("Gráfico de R = X / Y")
plt.xlabel("E(V)")
plt.ylabel("R(ohm)")
plt.grid(True)
plt.show()

# Erro

Resistencia = float(input("Digite a resistência: "))
print("\nErros individuais:")
for i in range(len(r)):
    Porcentagem = ((r[i] - Resistencia) / Resistencia) * 100
    Erro = abs(round(Porcentagem, 4))
    print(f"Erro{i+1} = {Erro}%")

M = sum(r) / len(r)
Porcentagem = ((M - Resistencia) / Resistencia) * 100
Errog = abs(round(Porcentagem, 4))
print(f"\nErro geral = {Errog}%")