#exercitando contador usando if / elif /else
# ------------------------------------------------------------------------------------------------------------------------------------------------
# split = cira uma lista
# join = ' '.join  para estabelecer espaços entre os numeros
# filter= A função integrada filter() do Python pode ser usada para criar um novo iterador a partir de um iterável existente (como uma list a ou um dicionário) que irá filtrar de forma eficiente os elementos usando uma função que fornecemos.
# srt isalnum -  isalnum () para detectar sequências de letras e números.

# totala = 0
# totalb= 0
# cont = 0
# b = 10
# a = 0
# cpf = input("Digite seu cpf: ")
# cpf = ' '.join(filter(str.isalnum, cpf))
# cpf = cpf.split()
#
# while cont < 9:
#     totala = totala + int(cpf[a]) * b
#     a += 1
#     b -= 1
#     cont += 1
# cont = 0
# b = 11
# a = 0
# while cont < 10:
#     totalb = totalb + int(cpf[a]) * b
#     a += 1
#     b -= 1
#     cont += 1
#
# p1 = (totala * 10)%11
# p2 = (totalb * 10)%11
#
# if p1 == int(cpf[9]) and p2 == int(cpf[10]):
#     print("O cpf é válido")
# else:
#     print("O cpf é inválido")
#
# if cpf[8] == "1":
#     print("Seus possíveis estados são : Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins")
# elif cpf[8] =="2":
#     print("Seus possíveis estados são : Pará, Amazonas, Acre, Amapá, Rondônia e Roraima")
# elif cpf[8] == "3":
#     print("Seus possíveis estados são : Ceará, Maranhão e Piauí")
# elif cpf[8] == "4":
#     print("Seus possíveis estados são: Pernambuco, Rio Grande do Norte, Paraíba e Alagoas")
# elif cpf[8] == "5":
#     print("Seus possíveis estados são : Bahia ou Sergipe")
# elif cpf[8] == "6":
#     print("Você é de: Minas Gerais ")
# elif cpf[8] == "7":
#     print("Seus possíveis estados são: Rio de Janeiro ou Espírito Santo")
# elif cpf[8] == "8":
#     print("Você é de: São Paulo")
# elif cpf[8] == "9":
#     print("Seus possíveis estados são: Paraná e Santa Catarina")
# else:
#     print("Você é do rio grande do Sul")


# ------------------------------------------------------------------------------------------------------------------------------------------------

# cont = 0
# i = 6
# resposta_user = 0
# resposta_certa = 'BURRO'
# print("JOGO: ADIVINHE A PALAVRA DO DIA")
# print("REGRA: A PALAVRA TEM 5 LETRAS\n"
#       "VOCÊ TEM 6 TENTATIVAS PARA ACERTAR!")
# while cont <= 6:
#     resposta_user = input("Digite a palavra: ").upper()
#     if resposta_user == resposta_certa:
#         print(f'Parabéns você acertou a palabra do dia: {resposta_certa}')
#         break
#     elif resposta_user != resposta_certa:
#         cont += 1
#         i -= 1
#         print(f'Você errou!! Restam: {i} tentativas...')
#         if i < 1:
#             print(f'Infelizmente você não conseguiu, a resposta do dia é: {resposta_certa}!')
#             break

# ----------------------------------------------------------------------------------------------------------------------------

#i = 0
# palavraFinal = list("fazer")
# palavra = list(input(""))
# if len(palavra) > 5:
#     print("Palavra Invalida")
# else:
#     print(palavra)
#     while i < len(palavra):
#         letraPalavraDigitada = palavraFinal[i]
#         letraPalavraCerta = palavra[i]
#         i += 1
#         if letraPalavraCerta == letraPalavraDigitada:
#             print(f"\033[1;32m{letraPalavraCerta}", end="")
#         elif letraPalavraCerta != letraPalavraDigitada:
#             print(f"\033[1;32m{letraPalavraCerta}", end="")
#--------------------------------------------------------------------------------------------------------------------------------