# Hello-Python

Este rositorio llevará mi aprendizaje en python

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
