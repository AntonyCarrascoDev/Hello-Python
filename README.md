# Hello-Python

Este repositorio llevará mi aprendizaje en python

## Comentarios y hola mundo

Los comentarios es algo que todo programador debe de conocer ya que permitira dejar una pequeña descripcion de la funcionalidad que tendra una sección en especifico de nuestro codigo.

```
# Comentario de una linea

''' Comentario
de varias
lineas'''
```

> Todo string que no este asignado a una variable python lo toma como un comentario

## Tipos de Datos

Dentro de python tenemos diversos tipos de datos que vienen nativos con el lenguaje de programación.

Tipos numéricos - Tenemos 3 tipos de Datos numericos con los cuales podemos trabajar con python.

- int -> Llamados enteros, seran numeros sin coma decimal

```
1 2 3
```

- float -> Numeros flotantes, es decir con coma decimal

```
23.3 45.1
```

- complex -> Numeros complejos que se utilizaran en su mayoria de casos para temas estadisticos

```
3 +2j
```

Tipos caracteres - Los caracteres son cadenas de textos que podemos manipular.

- str -> String, tipo de texto al cual le podemos aplicar algunas funciones, las cuales se veran más adelante.

```
'Hola mundo'
"Hi wolrd"
```

Tipo de Secuencia - Son aquellos que pueden almacenar más de un elemento a la vez.

-lista-> list:Se utilizan para almacenar varios elementos en una sola variable

```
my_list =[1,2,4]
```

-tupla -> tuple: Son similares a las listas, pero a diferencia de las listas, son inmutables, es decir no pueden ser modificadas.

```
my_tuple = (1,4,24)
```

-rango -> range(): Representan una secuencia inmutable de numeros enteros. Utilizado comunmente para generar una secuencia de numeros enterios para su uso en un bucle for.

```
range(0,10,1) - numeros del 0 al 10 de 1 en 1
range(0,10) - numeros del 0 al 10 por defecto de 1 en 1
range(1,11,2) - numeros del 1 al 11 de 2 en 2
```

Tipos Booleanos

- bool -> Son aquellos que representan valores de verdad. Es decir Verdaderos o Falsos

```
True or False
```

Tipos de Mapeo

- diccionarios -> dict: Estructura de datos que permite almacenar un conjunto de datos como pares clave-valor, cada valor es accesible a través de una clave unica.

```
my_dict = {
    'nombre':'Juan',
    'edad':16,
    'ciudad':'Chiclayo'
}

print(my_dict['nombre'])
>>> Juan
```

Tipos de Conjunto

- set -> Coleccion de elementos unicos e inmutables; es decir, no debe haber duplicados en un conjunto y no se pueden cambiar despues de ser creados.

```
my_set = {1,3,4,}
set([1,3,4,3])
```

- frozenset -> Similares a los tipos de datos set, pero son inmutables

```
my_frozenset=frozenset([1,3,5,3])
```

Funcion **type()** permitira poder identificar el tipo de dato que tenemos

```
print(type(3)) -> int
print(type('hi')) -> str
```

## Variables

Una variable es un espacio reservado en memoria a la cual se le asignara un valor.
Python no tiene una palabra reservada para la creación de una variable, ni debemos especificar el tipo de dato que esta variable va a contener.

Reglas para la creación de variables:

- Un nombre de variable debe comenzar con una letra o el caracter de guión bajo.
- Un nombre de variable no puede comenzar con un número.
- Un nombre de variable solo puede contener caracteres alfanumericos y guiones bajos(Az,0-9 y \_)
- Los nombres de las variables distinguen entre mayusculas y minusculas.
- Un nombre de variable no puede ser ninguna de las palabras clave de python.

```
my_variable_entero=3
my_variable_bool=True
my_variable_float=3.5
```

### Casting de variable

En Python podemos forzar el cambio de una tipo de una variable, siempre y cuando la información lo permita.

```
my_variable_int_to_str =str(my_variable_entero)
print(type(my_variable_entero)) #Devuelve <class 'int'>
print(type(my_variable_int_to_str)) #Devuelve <class 'str'>
```

### Concatenación de variables

Podemos juntar variables de tipo str.

```
name_complet = first_name + ' ' + last_name
print(name_complet)
```

### Función reservada de python len()

La función reservada en el lenguaje de programación python tiene una función len(), la cual devolvera el numero de caracteres que un string tiene.

```
print(len(first_name))
```

### Asignación de variables en una sola linea

```
name, surname = 'Antony','Alarcon'
```

> Cuidado con abusar con esta sintaxis ya que puede generar problemas en el mantenimiento del aplicativo.

### Ingresar el valor por teclado

Con la función input() pedimos que el ingreso del valor se realice por teclado

```
nombre = input('Ingresa tu nombre: ')
print(f"Hola {nombre}")
```

> Cuando pedimos un valor con el metodo input() siempre se va a recibir un valor en tipo str.
