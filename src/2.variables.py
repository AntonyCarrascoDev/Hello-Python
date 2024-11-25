#VARIABLES

my_first_variable="My String Variable"
print(my_first_variable)

my_variable_entero=3
my_variable_bool=True
my_variable_float=3.5

first_name="Antony"
last_name='Carrasco'
age=28

print(f"Hi, my name is {first_name} {last_name}, y mi edad es  {age} ")

#Casting de variable

my_variable_int_to_str =str(my_variable_entero)
print(type(my_variable_entero)) #Devuelve <class 'int'>
print(type(my_variable_int_to_str)) #Devuelve <class 'str'>

#Concatenación de variables

name_complet = first_name + ' ' + last_name
print(name_complet)

#Funcion reservada en el sistema len()

print(len(first_name))

#Función input()

nombre = input('Cual es tu nombre?')
print(f"Hola {nombre}")

# Forzar el tipo de variable?

address:str = "La Victoria"
address = 32
print(address)

