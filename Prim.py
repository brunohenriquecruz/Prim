import os

grafo = {'a': [('p',4), ('j',15), ('b',1)],
        'b': [('a',1), ('d',2), ('e',2), ('c',2)],
        'j': [('a',15),('c',6)],
        'p': [('a',4),('d',8)],
        'd': [('b',2), ('g',3),('p',8)],
        'e': [('b',2), ('g',9), ('f',5), ('c',2),('h',4)],
        'c': [('b',2), ('e',2), ('f',5), ('i',20),('j',6)],
        'g': [('d',3), ('e',9), ('h',1)],
        'f': [('h',10), ('e',5), ('c',5),('i',2)],
        'i': [('c',20),('f',2)],
        'h': [('g',1),('e',4),('f',10)] 
		    }


listaVisitados = []
grafoResultante = {}
listaOrdenada = []


#1.- Origem do nó
print(grafo)
ori = input("\nSelecione nó de origem de A a H: ")
#2.- Adiciona como visitado
listaVisitados.append(ori)

#3.- Adicionar adjacente na lista
for dest, peso in grafo[ori]:
  listaOrdenada.append((ori, dest, peso))
'''Ordenar'''
pos=0
act=0
listAux=[]
for i in range(len(listaOrdenada)):
    listAux=listaOrdenada[i]
    act=listaOrdenada[i][2]
    pos=i
    while pos> 0 and listaOrdenada[pos-1][2] > act:
        listaOrdenada[pos] = listaOrdenada[pos-1]
        pos=pos-1
    listaOrdenada[pos]=listAux

while listaOrdenada:
  vertice = listaOrdenada.pop(0)
  d = vertice[1]

  if d not in listaVisitados:
    listaVisitados.append(d)
    for key, lista in grafo[d]:
      if key not in listaVisitados:
        listaOrdenada.append((d, key, lista))
    listaOrdenada = [(c,a,b) for a,b,c in listaOrdenada]
    listaOrdenada.sort()
    listaOrdenada = [(a,b,c) for c,a,b in listaOrdenada]
    ori  = vertice[0]
    dest = vertice[1]
    peso    = vertice[2]

    if ori in grafoResultante:
      if dest in grafoResultante:
        lista = grafoResultante[ori]
        grafoResultante[ori] = lista + [(dest, peso)]
        lista = grafoResultante[dest]
        lista.append((ori, peso))
        grafoResultante[dest] = lista
      else:
        grafoResultante[dest] = [(ori, peso)]
        lista = grafoResultante[ori]
        lista.append((dest, peso))
        grafoResultante[ori] = lista
    elif dest in grafoResultante:
      grafoResultante[ori] = [(dest, peso)]
      lista = grafoResultante [dest]
      lista.append((ori, peso))
      grafoResultante[dest] = lista
    else:
      grafoResultante[dest] = [(ori, peso)]
      grafoResultante[ori] = [(dest, peso)]
      
print("\n\nGrafo final:\n")
for key, lista in grafoResultante.items():
  print(key, grafo[key])
print(lista)
os.system("pause")