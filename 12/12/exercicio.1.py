nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 21:
    print("Maior de idade")
else:
    print("Responsavel")

texto = "Menor de idade" if idade < 18 else "Maior de idade"

print(texto)
