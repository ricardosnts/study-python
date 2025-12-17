investimento = float(input("Qual valor será investido? "))
rentabilidade_mensal = 0.5/100
tempo = 24

valor_final = investimento*(1+rentabilidade_mensal)**tempo

rendimento = valor_final - investimento

print(f"O rendimento após 2 anos será de R${rendimento:.2f}!")