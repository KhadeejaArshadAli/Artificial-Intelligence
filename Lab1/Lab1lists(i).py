#Play with some of the list functions. You can find the methods you can call on an object via the dir
#and get information about them via the help command: 
lst= ['a','b','c']
lst.reverse()
print(lst)
lst.append('d')
print(lst)
lst.extend('e')
print(lst)
lst.pop(1)
print(lst)
lst.insert(1,'f')
print(lst)
lst.remove('f')
print(lst)
lst.clear()
print(lst)
lst=['a','b','c','d']
print(lst.count('a'))
