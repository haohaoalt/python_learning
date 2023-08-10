import re
# match 匹配字符串开头位置,返回match对象或None:
test = 'hello world1234'
m = re.match('hel',test) 
print(m.group()) # 'hel'
m = re.match('tel',test) 
print(m) # None

# search 搜索字符串任意位置,返回match对象或None
m = re.search('llo', test)
print(m.group())  # llo

# findall 搜索字符串,返回所有匹配的列表
m = re.findall('\d', test)
print(type(m[0]))
print(m)

# sub 使用正则表达式进行字符串替换:
m = re.sub('\d','c',test)
print(m)

# split() 使用正则表达式进行字符串分割:
m = re.split('\d+',test)
print(m)

# compile() 编译正则表达式,返回pattern对象:
pat = re.compile('\d') 
m = pat.match('123')
print('compile',m.group())

# finditer() 在需要定位每个匹配的位置时,re.finditer()非常有用。
# 在Python的re模块中,re.finditer()是非常有用的一个正则表达式匹配函数。
# re.finditer()的作用是在字符串中找到所有的匹配,并返回一个迭代器。相比re.findall()和re.finditer()有以下区别:
# re.findall():返回一个匹配字符串的列表
# re.finditer():返回一个匹配对象迭代器
s = 'hello 123 456 world'
matches = re.findall('\d+', s)
print(matches) # ['123', '456']
iterator = re.finditer('\d+', s)
print(iterator) # <callable_iterator object at 0x10f5f3b50>
for match in iterator:
    print(match)    
# <re.Match object; span=(6, 9), match='123'>
# <re.Match object; span=(10, 13), match='456'>

# fullmatch 匹配整个字符串,返回match对象或None:
m = re.fullmatch('hello',test)
print(m)

# escape() 将特殊字符转义,可以将字符串转化为正则表达式的字符串形式:
escaped = re.escape('http://example.com')  
print(escaped) # 'http:\/\/example\.com'

# purge() 清除缓存的正则表达式,可以避免重复编译正则表达式:
pat = re.compile(r'\d+')
re.purge() # 清除缓存

# match.expand() 使用匹配到的组内容,替换字符串模板
m = re.match(r'(?P<name>\w+) (\w+)', 'John Doe')
print(m.expand('Hello \g<name>')) # 'Hello John'

# (?P\w+)和 group(“name”) 搭配使用
pattern = r'(?P<first_name>\w+) (?P<last_name>\w+)'

string = 'John Doe'

# 匹配字符串
m = re.match(pattern, string)

# 使用命名组获取匹配
first_name = m.group('first_name') 
last_name = m.group('last_name')

print(first_name) # John
print(last_name) # Doe

# 替换字符串
new_string = re.sub(pattern, r'\g<last_name>, \g<first_name>', string)
print(new_string) # Doe, John
# 在这个例子中,正则表达式模式使用了两个命名捕获组first_name和last_name。然后在获取匹配后,可以直接通过命名引用匹配的内容。在替换字符串时,也可以利用命名组引用,使代码更简洁清晰。所以命名捕获组可以让正则匹配和处理更高效方便。