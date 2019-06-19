>>> line='asdf fjdk; afed, fjek,asdf,     foo'
>>> import re
>>> re.split(r'[;,\s]\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
>>> fields = re.split(r'(;|,|\s)\s*', line)
>>> fields
['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
>>> values = fields[::2]
>>> delimiters=fields[1::2]+['']
>>> values
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
>>> delimiters
[' ', ';', ',', ',', ',', '']
>>> # Reform the line using the same delimiters
>>> ''.join(v+d for v,d in zip(values,delimiters))
'asdf fjdk;afed,fjek,asdf,foo'
>>> re.split(r'(?:,|;|\s)\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']



>>> filename = 'spam.txt'
>>> filename.endswith('.txt')  # str.endswith() 检查字符串结尾
True
>>> filename.startswith('file:')   # str.startswith()  检查字符串开头
False
>>> url='http://www.baidu.com'
>>> url.startswith('http:')
True
>>> import os
>>> filename = os.listdir('.')
>>> filenames = os.listdir('.')
>>> filenames 
['builtin-apply-example-1.py', 'builtin-apply-example-2.py', 'chapter1.py', 'decompose.py', 'oddeven.py', 'string.py']
>>> [name for name in filenames if name.endswith(('.c','.h'))]
[]
>>>  [name for name in filenames if name.endswith(('.c','.py'))]
['builtin-apply-example-1.py', 'builtin-apply-example-2.py', 'chapter1.py', 'decompose.py', 'oddeven.py', 'string.py']
>>> any(name.endswith('.py') for name in filenames)
True
>>> from urllib.request import urlopen
>>> def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
        
        
>>> choices = ['http:','ftp:']
>>> url = 'http://www.python.org'
>>> url.startswith(choices)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: startswith first arg must be str or a tuple of str, not list
>>> url.startswith(tuple(choices))
True

>>> filename='spam.txt'
>>> filename[-4:] == '.txt'
True
>>> filename[-4:] == '.tt'
False

>>> url='http://www.python.org'
>>> url[:5]='http:' or url[:6]='https:' or url[:4]='ftp:'
  File "<pyshell>", line 1
SyntaxError: can't assign to operator
>>> url[:5]=='http:' or url[:6]=='https:' or url[:4]=='ftp:'
True
>>>


>>> import re
>>> url = 'http://wwww.python.org'
>>> re.match('http:|https:|ftp:', url)
<re.Match object; span=(0, 5), match='http:'>
>>> re.match(r'http:|https:|ftp:', url)
<re.Match object; span=(0, 5), match='http:'>
>>> url2 = 'http://wwww.python.org'
>>> url2 = 'https://wwww.python.org'
>>> re.match('http:|https:|ftp:', url)
<re.Match object; span=(0, 5), match='http:'>
>>>  re.match('http:|https:|ftp:', url2)
<re.Match object; span=(0, 6), match='https:'>


>>> if any(name.endswith(('.c','.h')))  for name in listdir(dirname):

>>> from fnmatch import fnmatch,fnmatchcase
>>> fnmatch('foo.txt', '*.txt')
True