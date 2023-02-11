#Swapping Variable
def swap(a,b,c,d):
    temp=a
    a=d
    d=temp
    temp=b
    b=c
    c=temp
    print("After Swapping")
    print(a,b,c,d)
a=input("Value a: ")
b=input("Value b: ")
c=input("Value c: ")
d=input("Value d: ")
print("Before Swapping")
print(a,b,c,d)
swap(a,b,c,d)






