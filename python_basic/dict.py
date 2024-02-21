# 创建字典的方法：
# 使用花括号（{}）和键值对（key-value pairs）：
my_dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# 使用内置的dict()函数：
my_dict2 = dict(key1='value1', key2='value2', key3='value3')

# 使用包含键值对的列表和列表解析：
key_value_pairs = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
my_dict3 = {key: value for key, value in key_value_pairs}

# 使用zip()函数结合两个列表来创建字典：
keys = ['key1', 'key2', 'key3']
values = ['value1', 'value2', 'value3']
my_dict4 = dict(zip(keys, values))

#  获取字典的值
# 定义一个字典
my_dict = {'name': 'mufenggrow1', 'age': 19, 'city': 'New York'}

# 获取字典中的值
name = my_dict['name']
age = my_dict['age']
city = my_dict['city']

# 打印获取到的值
print("Name:", name)
print("Age:", age)
print("City:", city)

# 取字典视图的三个方法
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
keys_view = my_dict.keys()
print('==============\nkeys_view:')
for key in keys_view:
    print(key)

values_view = my_dict.values()
print('==============\nvalues_view:')
for value in values_view:
    print(value)

items_view = my_dict.items()
print('==============\nitems_view:')
for key, value in items_view:
    print(key, value)

# 增加元素，修改元素，删除元素
my_dict = {'name': 'mufenggrow', 'age': 19, 'city': 'qingdao'}

# 增加元素
my_dict['gender'] = 'male'
my_dict['country'] = 'China'

# 打印字典
print("字典增加元素后的内容:", my_dict)

# 修改元素
my_dict['age'] = 20
my_dict['city'] = 'Beijing'

# 打印字典
print("字典修改元素后的内容:", my_dict)

# 删除元素
del my_dict['country']

# 打印字典
print("字典删除元素后的内容:", my_dict)

# 字典的遍历
my_dict = {'name': 'mufenggrow', 'age': 19, 'city': 'qingdao'}

# 遍历键
print("遍历键:")
for key in my_dict:
    print(key)

# 遍历值
print("\n遍历值:")
for value in my_dict.values():
    print(value)

# 遍历键值对
print("\n遍历键值对:")
for key, value in my_dict.items():
    print(key, value)

# 字典的常用方法
# fromkeys()方法 fromkeys() 方法用于创建一个新的字典，其中使用指定的键列表作为键，使用给定的默认值作为对应的值。
print('fromkeys()方法\n')
keys = ['name', 'age', 'city', 'gender', 'country']
default_value = 'Unknown'
my_dict = dict.fromkeys(keys, default_value)
print(my_dict)

# get()方法
# get() 方法用于根据给定的键获取字典中对应的值。如果键存在，则返回对应的值；如果键不存在，则返回指定的默认值（如果没有提供默认值，则返回 None）。
print('get()方法\n')
my_dict = {'name': 'mufenggrow', 'age': 19, 'city': 'QD', 'gender': 'Male', 'country': 'China'}

age = my_dict.get('age')
occupation = my_dict.get('occupation', 'Unknown')

print("Age:", age)
print("Occupation:", occupation)

# setdefault() 方法
# setdefault() 方法用于获取字典中给定键的值，如果键存在，则返回对应的值；如果键不存在，则将键插入字典并设置指定的默认值。
my_dict = {'name': 'mufenggrow', 'age': 19, 'city': 'QD'}

hobby = my_dict.setdefault('hobby', 'Unknown')
country = my_dict.setdefault('country', 'China')
print('setdefault() 方法\n')
print(my_dict)
print("Hobby:", hobby)
print("Country:", country)

# pop() 方法
# pop() 方法用于删除并返回字典中给定键的值。
# 在使用pop()方法时，如果找到key，就会删除该键值对；如果找不到key，就会返回defalut设置的值；如果该值没有设置，就会报错。
my_dict = {'name': 'mufenggrow', 'age': 19, 'city': 'QD', 'hobby': 'Unknown', 'country': 'China'}

hobby = my_dict.pop('hobby')
print('pop() 方法 pop(hobby) \n')
print(my_dict)
print("Popped Hobby:", hobby)

my_dict = {'name': 'mufenggrow', 'age': 19, 'city': 'QD'}

# 删除键为 'age' 的键值对，并返回对应的值
age = my_dict.pop('age')
print("Popped Age:", age)
print("Updated Dictionary:", my_dict)

# 尝试删除不存在的键 'country'，返回默认值 'Unknown'
country = my_dict.pop('country', 'Unknown')
print("Popped Country:", country)
print("Updated Dictionary:", my_dict)

# 尝试删除不存在的键 'country'，没有提供默认值，会抛出 KeyError 异常
country = my_dict.pop('country')
