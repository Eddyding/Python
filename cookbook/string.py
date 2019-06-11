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