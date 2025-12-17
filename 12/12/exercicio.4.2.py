investimento = float(input("Qual valor será investido? "))
rentabilidade = float(input("Qual a rentabilidade mensal (em %)? "))
tempo = int(input("Quantos meses o valor ficará investido? "))

valor_final = investimento
rentabilidade_mensal = rentabilidade/100

# A cada 3 meses é feito um aporte com o dobro do valor investido inicialmente TODO

for periodo in range(1, tempo + 1):
    valor_final += valor_final * rentabilidade_mensal

rendimento = valor_final - investimento

print(f"O rendimento após {tempo} meses será de R${rendimento:.3f}!")
print(f"O valor final será de R${valor_final:.3f}!")