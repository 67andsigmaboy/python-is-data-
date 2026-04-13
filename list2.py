my_dict={}
my_dict ={1:'apple', 2:'ball'}
my_dict={'name':'jendell',1:[2,4,3]}
my_dict ={'name':'jendell', 'age': 20}

print(my_dict['name'])
print(my_dict['age'])


my_dict['age']=21
print(my_dict)

my_dict['age']=21
print(my_dict)

my_dict['address']='new york'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address:", my_dict.get('address'))
my_dict.clear()
print(my_dict)
