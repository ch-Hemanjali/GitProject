'''dict1={}
dict2=dict()
print(dict1,dict2)
'''

#accessing elements in dict
'''dict1={'name':'Akash','sign':'horros'}
print(dict1['name'])
print(dict1.get('name'))
'''

#add or change in dict
dict1={'first':'python','second':'java'}
dict1['first']="c"
dict1['second']='c++'
print(dict1)
dict1["third"]="perl"
print(dict1)

#delet in dict
a=dict1.pop("first")
print(a)
b=dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)


d1={'first':'p','second':'c','third':'j'}
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.get('first'))



