#Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes
#inputs like height, width and depth from user and then calculate volume of the cube:
#volume = height ∗ width ∗ depth
#After calculating volume of cube, compare it with following ranges and print the relevant label:
#Volume Range Label
#1 cm3 – 10 cm3 Extra Small
#11 cm3 – 25 cm3 Small
#26 cm3 – 75 cm3 Medium
#76 cm3– 100 cm3 Large
#101 cm3– 250 cm3 Extra Large
#251 cm3 and above Extra-Extra Large
def CalculateVolume():
    height=int(input("Enter the height: "))
    width=int(input("Enter the width: "))
    depth=int(input("Enter the depth: "))
    Volume=height*width*depth
    
    if Volume>=1 and Volume<=10:
        print("Extra Small")
    if Volume>=11 and Volume<=25:
        print("Small")
    if Volume>=26 and Volume<=75:
        print("Medium")
    if Volume>=76 and Volume<=100:
        print("Large")
    if Volume>=101 and Volume<=250:
        print("Extra Large")
    if Volume>=251:
        print("Extra-Extra Large")
    return Volume
          

print("Volume: ",CalculateVolume())
