# STRINGS

my_string = "Mi String"
my_other_string = "Mi otro String"

print(my_string)
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de linea"
print(my_new_line_string)
my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

#Formateo de String
my_name = 'Antony'
my_lastname = 'Carrasco'
my_age = 28

print("Mi nombre es {} {} y mi edad es {:.1f}".format(my_name,my_lastname,my_age))
print("Mi nombre es %s %s y mi edad es %d" %(my_name,my_lastname,my_age))
print(f"Mi nombres es {my_name} {my_lastname} y mi edad es {my_age:.1f}")

#Desempaquetado de caracteres
language = "Python"
a,b,c,d,e,f = language
print(a,b,c,d,e,f)

#Division de String
language_slice = language[1:3] #Del 1 al 3 sin contar el ultimo
language_slice = language[1] # Del 1 al final
language_slice = language[:3] # Del inicio hasta el 3 sin contar el ultimo
language_slice = language[1:6:2] # Del 1 al 6 de dos en dos
language_slice = language[::-1] #del 1 al ultimo pero al reves
print(language_slice)

#Metodos con STRING

challenge = 'thirty days of python'
print(challenge.capitalize())

print(challenge.count('y'))
print(challenge.count('y',7,14))
print(challenge.count('th'))

print(challenge.endswith('on')) #True
print(challenge.endswith('tion')) #False

