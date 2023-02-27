#You have collected information about cities in your province. You decide to store each city’s
#name, population, and mayor in a file. Write a python program to accept the data for a number of
#cities from the keyboard and store the data in a file in the order in which they’re entered.

f=open('Cities.txt', 'w')        
num_cities = int(input("How many cities do you want to add? "))    
for i in range(num_cities):
    print(f"Enter information for city #{i+1}:")
    city_name = input("Name: ")
    population = int(input("Population: "))
    mayor = input("Mayor: ")   
    f.write(f"{city_name},{population},{mayor}\n")
f.close()
f=open('cities.txt', 'r')
print(f.read())
