vocales = ['a','i']
vocales.append('e')
print(vocales)
vocales.extend(['o','u'])
vocales
print(vocales)


numeros_hasta_cuatro = [0,1,2,3,4]
numeros_desde_cinco = [5,6,7,8,9]
numeros = numeros_hasta_cuatro + numeros_desde_cinco
print(numeros)

patron=['a','b','c']
patrones=patron * 3
print(patrones)

vocales=['e','e','e','e','u']
vocales[0]='a'
print(vocales)


vocales = ['a','e','i','o','u']
del vocales[1]
print(vocales)

vocales=['a','e','i','o','u']
del vocales[2:4]
print(vocales)

del vocales[:]
print(vocales)

letras = ["a","b","c","d"]
letras.remove("a")

letras.pop()

print(letras)
