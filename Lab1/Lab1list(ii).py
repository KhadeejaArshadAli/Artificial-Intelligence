#)Write a Python program to count the number of strings where the string length is 2 or more and the
#first and last character are same from a given list of strings. 
def Counting(lst):
    count=0
    for lst in  lst:
        if len(lst)>1 and lst[0]==lst[-1]:
         count+=1
    return count
lst=['abc','xyz','aba','1221']
print(Counting(lst))