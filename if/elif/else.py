#exercitando-if/elif/else
#------------------------


# nome = input("Digite seu nome: ")
# cargo = input("Digite seu cargo: ")
# salario = float(input("Digite seu salário: "))
#
# if salario > 5000:
#     aumento = "5%"
#     salarionovo = salario*1.05
# elif salario >= 3000:
#     aumento = "7%"
#     salarionovo = salario*1.07
# else:
#     aumento = "10%"
#     salarionovo = salario*1.1
#
# print(f'Nome: {nome.title()}')
# print(f'Cargo: {cargo.title()}')
# print(f'Salário Antigo: {salario:.2f}')
# print(f'Salário novo:{salarionovo:.2f}')
# print(f'Aumento aplicado: {aumento}')
# print(f'Valor de aumento:{salarionovo - salario:.2f}')

#-------------------------------------------------------------------------------------

# nome= input("digite seu nome")
# idade= float(input("digite sua idade"))
# altura= float(input("digite sua altura em cm"))
# peso= float(input("digite seu peso em kg"))
# alturacerta= altura/100
# imc= peso / ((altura/100)**2)
#
# if imc>=40:
#     print(f"{nome},com altura de {alturacerta} e {peso},tem imc de {imc}, portanto esta na categoria de obsidade morbida")
#
# elif imc<18.5:
#    print(f"{nome}, com altura de {alturacerta} e {peso}, tem imc de {imc}, portando esta abaixo do peso normal")
#
# elif imc<=24.9:
#     print(f"{nome}, com altura de {alturacerta} e {peso}, tem imc de {imc}, está com o peso normal ")
#
# elif imc<=29.9:
#     print(f"{nome}, com altura de {alturacerta} e {peso}, tem imc de {imc}, está sobrepeso")
#
# elif imc <=34.9:
#     print(f"{nome}, com altura de {alturacerta} e {peso}, tem imc de {imc}, clasificado obesidade grau 1")
#
# else:
#     print(f"{nome}, com altura de {alturacerta} e {peso}, tem imc de {imc} , obesidade grau 2")

#--------------------------------------------------------------------------------------------------------------------

# lado1 = float(input("digite o valor do lado 1"))
# lado2 = float(input("digite o valor do lado2"))
# lado3 = float(input("digite o valor do lado 3"))
#
# if lado2+lado3 < lado1 or lado1+lado3 < lado2 or lado2+lado1 < lado3 :
#     print("este triangulo não é possivel")
#
# elif lado1 == lado2 == lado3:
#         print("isto é um triangulo equilatero")
#
# elif lado1 != lado2 == lado3 or lado1==lado2!=lado3 or lado1==lado3!=lado2:
#     print("isto é um triangulo isoceles ")
#
# else:
#     print("isto é um trianguo escaleno")lado1 = float(input("digite o valor do lado 1"))
# lado2 = float(input("digite o valor do lado2"))
# lado3 = float(input("digite o valor do lado 3"))
#
# if lado2+lado3 < lado1 or lado1+lado3 < lado2 or lado2+lado1 < lado3 :
#     print("este triangulo não é possivel")
#
# elif lado1 == lado2 == lado3:
#         print("isto é um triangulo equilatero")
#
# elif lado1 != lado2 == lado3 or lado1==lado2!=lado3 or lado1==lado3!=lado2:
#     print("isto é um triangulo isoceles ")
#
# else:
#     print("isto é um trianguo escaleno")

#---------------------------------------------------------------------------------------------------

# nome1=input("digite seu nome ").__len__()
# nome2=input("digite o segundo nome ").__len__()
#
# if nome1 > nome2:
#     print("nome 1 com mais caracteres ")
# elif nome2 > nome1:
#     print("nome 2 com mais caracteres ")
#
# else:
#  print("nomes com mesmo numero de caracteres ")

# nota= int(input("digite a nota da prova "))
# if nota >= 7:
#   print ("você foi aprovado ")
# else:
#    print('você foi reprovado estude mais')

#-----------------------------------------------------------------------------------------------

# aluno=input("digite seu nome ")
# nota1=int(input("digite sua nota1 "))
# nota2=int(input("digite sua nota2 "))
# nota3=int(input("digite sua nota3 "))
# nota4=int(input("digite sua nota4 "))
# nome= (aluno.upper())
# media = (nota1+nota2+nota3+nota4) / 4
# if media >= 7:
#     print(f"{nome},você foi aprovado ")
# else:
#     print(f"{nome},não foi dessa vez ")

#--------------------------------------------------------------



