#set -->collection of data item (data structure) which is mutable,unorder,donot allow duplicate value 
# a={"sujan",'Hari',1,2,3}

# print(type(a))
# print(a[0:3])

# print(type(a))
# print(a)
# a.add("manoj")
# a.update({"syam",99})
# a.pop()
# a.remove("biraj")
# a.discard("biraj")
# print(a)


# a={1,2,3,4,5}
# b={2,4,6,8}

# c=a.intersection(b)

# c=a.union(b)
# c=b.difference(a)
# c=a.symmetric_difference(b)

# a.intersection_update(b)
# print(a)

# print(a.isdisjoint(b))
# print(a.issuperset(b))
# print(a.issubset(b))
# print(c)


a=frozenset({1,2,3,4,5})
print(type(a))
b={2,4,6,8}
var=a.intersection(b)
print(a)
print(var)