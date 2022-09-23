# list.append() = Adiciona elementos ao final da lista
# list.clear() = remove todos os elementos da lista
# list.copy() = atribui a uma cópia da lista a uma variável
# list.count() = Retorna o numero de elementos com o valor especificado
# list.extend() = adiciona os elementos de uma lista ao final de outra lista
# list.index() = retorna a posição da indexação do valor especificado
# list.insert() = adiciona elementos a posição especificada
# list.pop() = Remove os elementos de uma posição especifica
# list.remove() = remove o primeiro item correspondente ao valor especificado
# list.reverse() = Inverte os elementos de uma lista
# list.sort() = Organiza os elementos de uma lista, em ordem alfabética ou ordem crescente
# list.sort(reverse=True) organiza os elementos de uma lista, em ordem contraria a alfabética ou ordem decrescente

#----------------------------------------------------------------------------------------------------------------------
# taxas = [1,5.24,6.28,4.98]
# taxas_nome = ['real','euro','libra','dolar']
# print("""
# [0] real
# [1] euro
# [2] libra
# [3] dolar""")
# moeda_entrada = int(input('qual moeda deseja usar'))
# print("""
# [0] real
# [1] euro
# [2] libra
# [3] dolar""")
# moeda_saida  = int(input('qual moeda deseja receber'))
# valor_entrada = float(input('digite o valor para trocar'))
#
# if moeda_entrada == 0:
#   print(f'{valor_entrada / taxas[moeda_saida]:.2f}{taxas[moeda_saida]}')
# else :
#     print(f'{valor_entrada*taxas[moeda_entrada]/taxas[moeda_saida]:.2f}{taxas_nome[moeda_saida]}')

#-------------------------------------------------------------------------------------------------------------

# lista = []
#
# qtd = int(input('Quantida de números que você deseja digitar: '))
#
# for i in range(1, qtd+1):
#     lista.append(int(input(f'Número {i}: ')))
#
# while True:
#     print(30 * '=')
#     print("""
#     [1] - A lista em ordem crescente;
#     [2] -  A lista em ordem decrescente;
#     [3] - A soma de todos os itens;
#     [4] - A média de todos os números.
#     [5] - Parar
#     """)
#
#     print('=' * 30)
#
#     opcao = input('Qual opção você deseja? ')
#
#     if opcao == '1':
#         lista.sort()
#         print(lista)
#     elif opcao == '2':
#         lista.sort(reverse=True)
#         print(lista)
#     elif opcao == '3':
#         print(sum(lista))
#     elif opcao == '4':
#         print(sum(lista) / len(lista))
#     elif opcao == '5':
#         break

#------------------------------------------------------------------------------------------------------------------

# lista1 = []
# while True:
#      lista1.append(int(input('digite aqui ')))
#      OP = input('deseja continuar :[s] ou [n]')
#      if OP != 's':
#          break
#      print(lista1)
# lista1.sort()
# print(lista1)
# lista1.reverse()
# print(lista1)
# somalista = sum(lista1)
# print(somalista)
# medialista = round(sum(lista1)/len(lista1))
# print(medialista)

#---------------------------------------------------------------------------------------------------------------------

# nomes = []
# while True:
#      nomes.append(input('digite aqui seu nome '))
#      OP = input('deseja continuar :[s] ou [n] ')
#      if OP != 's':
#          break
#      print(nomes)
# nomes.sort()
# print(nomes)
# nomes.reverse()
# print(nomes)
# print(len(nomes))
# x = nomes.count(input('digite um nome '))
# print(x)


