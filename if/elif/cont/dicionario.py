#exercitando dicionario
# aluno = input('digite seu nome ')
# media = float(input('digite sua nota '))
#
# def aluno_media():
#     if media < 7 :
#        resultado = " você está reprovado"
#     else:
#        resultado = 'você está aprovado'
#
#     dic = {'aluno': aluno,
#             'media':media,
#             'situação': resultado}
#
#     return dic
#
# print(aluno_media())

#------------------------------------------------------------------------------

# import random
# from operator import itemgetter
# dic = {
#     'jogador1': random.randint(1,6),
#     'jogador2': random.randint(1,6),
#     'jogador3': random.randint(1,6),
#     'jogador4': random.randint(1,6)}
#
# print(dic)
#
# dicn = sorted(dic.items(), key=itemgetter(1), reverse=True)
# print(dicn)
#
# for i , dic in enumerate(dicn):
#     print(f"{i+1}-{dic[0]}-{dic[1]}")
