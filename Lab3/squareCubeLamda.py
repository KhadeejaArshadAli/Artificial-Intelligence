#a Python program to square and cube every number in a given list of integers using Lambda. 
def Square():
    x=0
    a=int(input ("Enter the number you want to square: "))
    x=lambda a: pow(a,2)
    print(x(a))
    
def Cube():
    x=0
    a=int(input ("Enter the number you want to cube: "))
    x=lambda a: pow(a,3)
    print(x(a))
    

Square()
Cube()


