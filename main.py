def valor_moeda(qtd, venda, realdolar):
   valor_da_moeda = (qtd )*(venda* realdolar)
   return valor_da_moeda
def teste():
   teste = [20, 50, 1000]

   for t in teste:
       print(t*100)

moeda_preco = valor_moeda(102000,0.21,5.10);

print(teste())

if(moeda_preco == 1):
    print('Igual')
else:
    print(moeda_preco)


