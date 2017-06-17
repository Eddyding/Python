#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

import os.path, glob

files= glob.glob("*.py")
for f in files:
	print(os.path.abspath(f))

files= glob.glob("jj") # do not recursive 
print(files) 


