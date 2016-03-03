
list_comprehension = [a if a %  else b for a, b in enumerate() if not  ]
l = [a for a in range (1,11)]
list_comprehension=[a if  b ==0 else b for a, b in enumerate("hola") if not a==0]
assert isinstance(list_comprehension, list)
assert len(list_comprehension)
