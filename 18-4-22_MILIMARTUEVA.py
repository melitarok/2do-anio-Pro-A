#Ordenar lista de numeros
numeros = [3,2,6,1,7,4]

numeros.sort()
print (numeros)

#ordenar lista de caracteres
nombres = ['Eva', 'Martina', 'Milagros', 'Antonia', 'Justina', 'Rafael', 'Esmeralda', 'Luna', 'Jose', 'Cami']

nombres.sort()
print (nombres)


#Determinar si algunos elementos se encuentran en la lista
catalogo = ['yogurt', 'manzana', 'naranja', 'leche', 'queso', 'banana']
print('bananas' in catalogo)   #True


producto = 'limon'
print(producto in catalogo)  #False
print(producto not in catalogo)  #True

bebidas = ['agua', 'coca-cola', 'Jugo', 'Sprite']

producto = 'vino'
print(producto in bebidas) #false
print(producto not in bebidas) #True

producto2 = 'Jugo'
print(producto2 in bebidas) #True
print(producto2 not in bebidas) #false


