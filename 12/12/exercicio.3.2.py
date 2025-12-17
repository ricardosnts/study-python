nome = input("Qual seu nome?")
nome_invertido = ""

for i in range(len(nome), 0, -1):
    nome_invertido += nome[i-1]

print(f"Seu nome invertido é {nome_invertido}!")