def inverter(n):
    return n[::-1]

nome = input("Qual é seu nome?")
nome_invertido = inverter(nome)

print(f"Seu nome invertido é {nome_invertido}!")