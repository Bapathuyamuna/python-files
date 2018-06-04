ython 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s='hello'
>>> s[::-1]
'olleh'
>>> s[1:[2]]

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[1:[2]]
TypeError: slice indices must be integers or None or have an __index__ method
>>> l=[1,2,3,4,5,6,7]
>>> l[l[l[3]]]
6
>>> l[l[3]]
5
>>> l[3]
4
>>> l[l[l[l[3]]]]
7
>>> s='hello word'
>>> s.capitalize()
'Hello word'
>>> s.center(20)
'     hello word     '
>>> s.strip()
'hello word'
>>> s.lstrip()
'hello word'
>>> s='                  hello          '
>>> s.lstrip()
'hello          '
>>> s.rstrip
<built-in method rstrip of str object at 0x027B7330>
>>> s.rstrip()
'                  hello'
>>> s='hello world'
>>> s.count
<built-in method count of str object at 0x027A4F20>
>>> s.count()

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.count()
TypeError: count() takes at least 1 argument (0 given)
>>> s.count(2)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.count(2)
TypeError: expected a string or other character buffer object
>>> s.count('l')
3
>>> s.decode()
u'hello world'
>>> s.encode()
'hello world'
>>> s.endswith()

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
>>> s.endswith(e)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.endswith(e)
NameError: name 'e' is not defined
>>> s.endswith(2)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.endswith(2)
TypeError: endswith first arg must be str, unicode, or tuple, not int
>>> s.endswith('e')
False
>>> s.endswith('d')
True
>>> s.endswith('o')
False
>>> s.find('o')
4
>>> s.find('x')
-1
>>> s.index('d')
10
>>> s.index('x')

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.index('x')
ValueError: substring not found
>>> s.find('y')
-1
>>> s.index('k')

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.index('k')
ValueError: substring not found
>>> s.format()
'hello world'
>>> s.isalnum()
False
>>> s.isalnum('h')

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.isalnum('h')
TypeError: isalnum() takes no arguments (1 given)
>>> s.isalnum('1')

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.isalnum('1')
TypeError: isalnum() takes no arguments (1 given)
>>> s='hello'
>>> s.isalnum()
True
>>> s.isalpha()
True
>>> s='hello123'
>>> s.isalpha()
False
>>> s.split()
['hello123']
>>> list(s)
['h', 'e', 'l', 'l', 'o', '1', '2', '3']
>>> s.isdigit()
False
>>> s.islower()
True
>>> s.upper()
'HELLO123'
>>> s.isspace()
False
>>> s.istitle()
False
>>> s.istitle()
False
>>> s.istitle('hello')

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s.istitle('hello')
TypeError: istitle() takes no arguments (1 given)
>>> s
'hello123'
>>> r='@'
>>> r.join(s)
'h@e@l@l@o@1@2@3'
>>> s
'hello123'
>>> s.ljust(10)
'hello123  '
>>> s.lower()
'hello123'
>>> s.partition()

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.partition()
TypeError: partition() takes exactly one argument (0 given)
>>> s.partition('h')
('', 'h', 'ello123')
>>> s.partition('hello123')
('', 'hello123', '')
>>> s='hello world'
>>> s.replace('world','yamuna')
'hello yamuna'
>>> s='yello world'
>>> list(s)
['y', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> u=list(s)
>>> s=u['w']

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s=u['w']
TypeError: list indices must be integers, not str
>>> 

>>> 
>>> 
>>> s = 'yello'
>>> y = s[1]
>>> list[y]

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    list[y]
TypeError: 'type' object has no attribute '__getitem__'
>>> s.rfind('y')
0
>>> s.rindex('w')

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.rindex('w')
ValueError: substring not found
>>> s.rindex('o')
4
>>> s.rjust(10)
'     yello'
>>> s.rpartition(10)

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s.rpartition(10)
TypeError: expected a string or other character buffer object
>>> s.rpartition('o')
('yell', 'o', '')
>>> s.rsplit()
['yello']
>>> s.rstrip('y')
'yello'
>>> s.rstrip('o')
'yell'
>>> s.rstrip('l')
'yello'
>>> s.rsplit('l')
['ye', '', 'o']
>>> s.splitlines()
['yello']
>>> s= 'hello yamuna'
>>> s.splitlines()
['hello yamuna']
>>> s= 'hello' 'yamuna'
>>> s.splitlines()
['helloyamuna']
>>> s.startswith('a')
False
>>> s.startswith('h')
True
>>> s.title()
'Helloyamuna'
>>> s.translate()

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s.translate()
TypeError: translate expected at least 1 arguments, got 0
>>> s.upper('y')

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.upper('y')
TypeError: upper() takes no arguments (1 given)
>>> s.upper('y')()

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.upper('y')()
TypeError: upper() takes no arguments (1 given)
>>> s.zfill(100)
'00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000helloyamuna'
>>> 
