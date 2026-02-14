#string : sequence of character enclosed in either single quote , double or triple 

# a='sujan said,"i want to learn django"'
# a="what's up"
'''my name is sujan 
  and i m from pkr'''
# print(type(a))
# print(a)

# a="sujan #"

# print(len(a))

#index : the way of accessing  element by thier position
#syntax : variable_name[position
#slicing : the way of accessing part of element 
#syntax : varaible_name[start:end:step]

# a="my name is sujan" #name
# print(a[3:7:1])
# print(a[3:10]) #nm s
# print(a[6:2:-1]) #eman

# print(a[3:])
# print(a[:4])
# print(a[::])
# print(a[::-1])

# print(a.replace(" ",""))

#string method 
# a="my NAME ß is sujan"
# print(len(a))

# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.capitalize())
# print(a.title())
# print(a.casefold())


# a="welcome sujan my name is sujan"

# print(a.center(70,'-'))
# print(a.count("sujan"))



# a="सुजन"
# # print(a.replace("Sujan","ram"))
# # print(a.startswith("my"))
# # print(a.endswith("an"))
# print(a.isalnum())
# print(a.isascii())


# a="my name is sujan"
# print(a.split())
# print(a.split("a"))

# a="biraj710@gmail.com"
# print(a.split("@")[0])

#strip 
# a="!!!!!welcome!!!!!"
# print(a.strip())
# print(a.strip("!"))
# print(a.rstrip("!"))
# print(a.lstrip("!"))

a="www.hello.com" #sujan
# print(a.lstrip("www.").rstrip(".com"))
print(a.removeprefix("www.").removesuffix(".com"))