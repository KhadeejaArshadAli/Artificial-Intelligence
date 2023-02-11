#Program to convert temperature to and from Celsius and Fahrenheit

def Conversion(temperature):
  Option= input("Press 1 for Celsius to Fahrenheit OR Press 2 for Fahrenheit to Celsius ")
  if (Option=="1"):
    f=9*(temperature/5)+32
    print("Temperature in Fahrenheit: ",f)
  else:
    c=5*((temperature-32)/9)
    print("Temperature in Celsius: ",c)


temperature= int(input("Enter the temerature: "))
Conversion(temperature)