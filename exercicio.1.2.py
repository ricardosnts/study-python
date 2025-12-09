precos = {'arroz': 20, 'feijao': 18, 'leite': 4}

produto = input('Digite o seu produto (arroz, feijao e leite): ').lower().strip()
forma_pagamento = input('Digite a forma de pagamento (dinheiro ou cartao): ').lower().strip()

preco = precos.get(produto)

if forma_pagamento == 'dinheiro':
    preco_final = preco * 0.9
else:
    preco_final = preco
print(f'Sua compra foi de {preco_final} reais!')

