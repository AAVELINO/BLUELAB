filmes = ['Os Vingadores', 'HP','Forrest Gump', 'A Procura da Felicidade', 'Como eu era antes de você']
print(filmes)
filmes.append('Lagoa azul') #.append adiciona 
print(filmes)
print()
#a = input('Digite um filme:')
#filmes.append(a)
#print(filmes)
print()
filmes_novos = ['Histórias Cruzadas', 'Poderoso chefão', 'Desventuras em série', 'De volta para o futuro']
filmes.extend(filmes_novos) #adiciono varias coisas
print(filmes)
print()
filmes.sort() #comando para ordenar str e int 
print(filmes)
print()
#filmes.reverse() #tras pra frente
#print(filmes)

print()
filmes.insert(1,'Pianista') #método de inserção
print(filmes)
print()
filmes.sort()
for filme in filmes: #laço de repetição for. filme é uma variavel de unidade de filmes.
    print(filme)

print()
filmes.remove('HP') #para remover str, nomenclaturas
print(filmes)
print()
filmes.pop() #para remover o índice e seu elemento

#del filmes[1] apaga o indice
#del filmes[:] apaga a lista toda
del filmes[0:2] # aqui apaga o intervalo entre os números, exceto o número à direita, mas ate ele apaga todos os anteriores

print(filmes)

for filme in filmes: #laço de repetição for. filme é uma variavel de unidade de filmes.
    print(filme)
print(len(filmes))
print()
print("Pianista" in filmes)