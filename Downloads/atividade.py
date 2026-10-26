valor_total = 0 
qtd_total = 0
while True: 


    print("----Bem-vindo ao sistema de cantina escolar----\n") 

    print("Opções, escolha o número para cada produto, s\n")

    print("1 -- Suco -- R$ 5,00")

    print("2 -- Salgado -- R$ 7,00")

    print("3 -- Sanduíche -- R$ 10,00")

    print("4 -- Finalizar compra --")

    escolha = int(input("Escolha o número da (s) opção (s) dejesejada (s) "))

    if escolha == 1:
        qtd_total += 1 
        valor_total += 5

    elif escolha == 2:
        qtd_total += 1
        valor_total += 7

    elif escolha == 3: 
        qtd_total += 1
        valor_total += 10

    elif escolha == 4:
        break 

    else: 
        print("Opção inválida! Escolha novamente!\n")

print (f"A quantidade total de itens escolhidos foi: {qtd_total}\n") 
print (f"O valor total gasto foi de {valor_total}R$")




