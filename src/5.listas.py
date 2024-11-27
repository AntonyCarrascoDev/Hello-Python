# LISTAS

my_list = ["apple","banana","cherry","papaya"]
my_other_list = list()
print(my_other_list)

my_other_list = [25, 1.56, "Antony"]

print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[2])
print(my_list.count("cherry"))

my_list[1:3]=["Mango","pineapple","fresa"]
print(my_list)

my_list.insert(3,"mandarina")
print(my_list)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical[0:2])
print(thislist)