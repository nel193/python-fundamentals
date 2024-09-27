#Comentarios de una linea
'''
Comentarios de bloque
'''

#Variables
#En python no existen los distintos tipos de variables como en Js
#Esta se definen solo llamando el nombre a declara y asignando un valor. Por lo cual intuyo que no se puede inicializar sin asignar un valor
#Ya que no esta el uso de constantes, las variables se pueden reasignar su valor como si fueran var de Js

#Strings
#Los strings se pueden declarar con comillas dobles, simples como en Js, y adicionalmente tambien puede ser con comillas triples
#las cuales nos permiten ejecutar saltos de linea como en los template literals
username = 'Max'
userlastname = 'Max Davizar'
#Consultando el tipo
print(type(username))
#Consultando caracteres por index
print(username[-1])
#Concatenando
print(username + ' ' + userlastname)
#Multiplicando la cant de un mismo string
print((username + ' ' + userlastname) * 3)
#Consultando largo del string
print(len(username))
#Formateando en mayuscula
print(username.upper())
#Contando strings dentro de otro string
print(userlastname.count(username))
#Volviendo mayuscula el primer caracter
username.capitalize()
translation = username.maketrans('Max', 'Rex')
print(username.translate(translation))

#Number
#integer
edad = 2
#float
pi = 3.1416
#Notacion cientifica
longNum= 1.2E6
longNum2 = 1.2E-6
print(longNum)
print(longNum2)
print(edad + pi)

#Boolean
esMayor = True
esMenor = False

#Sobre print
#Permite pasar varios parametros, esto lo imprime anhadiendo un espacio
print(esMayor, esMenor)
#Cuenta con un parametro sep para definir como debe usar el separador
print(esMayor, esMenor, sep=', ')
#Por default los print terminan con un salto de line \n
print(esMayor, esMenor, sep=', ', end='final random')
#Adicionalmente phyton cuenta con un tipo de template literal para el print donde se pueden usar variables dentro de un string a imprimir
print(f'este es un f-string y permite usar variable {esMayor} usando llaves para invocarlas {esMenor}')
#Lo mismo tambien se puede hacer con el metodo format, como suele pasar en C
print('un string con llaves {}, donde se cambiara por una variable'.format(esMayor))

#Para los numeros flotantes se puede controlar el formato a imprimir como se hace en C
#Si uso el . en la cantidad de decimales, se retiran el numero asignado
print('El valor de PI con solo dos decimales {:.2f}'.format(pi))
#Si no uso el . se añaden decimales al final del numero
print('El valor de PI con solo dos decimales {:2f}'.format(pi))

#Se pueden escapar caracteres o añadir combinaciones especiales como \n dentro de la cadena de texto como
print("Hola\nmundo")
print('Hola soy \'Carli\'')
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")

#Operadores matematicos
a = 10
b = 3

print('Suma:', a + b)
print('Resta:', a - b)
print('Multiplicacion:', a * b)
print('Division:', a / b)
#Evitar hacer divisiones por 0

print('Division solo obteniendo el entero del resultado:', a // b)
print('Potencia (Elevado a):', a ** b)
print('Resto (Modulo):', a % b)

#Atajos a la hora de hacer operaciones
# a += 2
# a -= 2
# a *= 2
# a /= 2

#Las operaciones matematicas responden a la convencion PEMDAS, lo cual se ejecuta en el siguiente orden
#Parenthesis
#Exponents
#Multiply
#Divide
#Add
#Substract

#Python utiliza los operadores logicos igual que Js, sin la comparacion estricta
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

#Python tiene una funcion input, con la cual se puede interactuar a traves de la termina
#los valores que ingresan por input siempre son strings, por lo cual el valor debe de ser casteado
# name = input('Ingrese su nombre: ')
# age = input('ingrese su edad: ')

# while(not age.isnumeric()) :
#     age = input('Debes ingresar un numero')


# age = int(age)
# print(f'Tu nombre es {name} y tienes {age} años y age es del tipo {type(age)}')

#Listas
frutas = ['Banana', 'Manzana', 'Coco']
loteria = [3, 4, 5, 6]
#Para consultar el largo de la lista
print(len(frutas))
#Para consultar un indice en especifico, lo mismo aplica para strings
print(frutas[0])
#Adicionalmente las listas cuentan con la posibilida de consultar rangos, 
#indicando como primer parametro el indice de inicio, y segundo parametro la cant de elementos
print(frutas[0:3])
#Una buena practica es que si se quieren iniciar desde el indice cero, se pase vacio este parametro
print(frutas[:3])
#Y si se quiere obtener todos los elementos, se deje vacio el segundo parametro
print(frutas[:])
#Para añadir elementos al final de la lista se usa el metodo append
frutas.append('Sandia')
print(frutas)
#Para añadir elementos en una posicion especifica, se usa el meotod insert, el cual recibe el indice
#donde se debe agrefar, y como segundo parametro el elemento a añadir
frutas.insert(1, 'Melon')
#Para buscar la primer coincidencia con un valor, se usa el metodo index y 
#el parametro es el valor a buscar, si el valor no existe, devuelve un ValueError
print(frutas.index('andia'))
#Para concatenar dos listas
frutas.extend(['Chontaduro', 'Fresa'])
#Las listas permiten sabe el numero maximo y el minimo
max(loteria)
min(loteria)

#Para borrar elementos podemos usar la palabra reservada del y el indice a borrar o un rango
del loteria[0]
del loteria[:2]
#y la misma palabra sirve para borrar la variable
del loteria

loteria = [3, 4, 5, 6]
#Adicionalmente tambien podemos borrar con el metodo .remove() pasando como parametro el valor 
#a buscar dentro de la lista
loteria.remove(4)
#Para borrar un indice especifico con un metodo
loteria.pop(1)
#Para borrar todos los valores de la lista, sin borrar la variable
loteria.clear()

