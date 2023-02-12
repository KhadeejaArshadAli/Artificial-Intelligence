#. Make a multiplication table using a loop
def MultiplicationTable():
    Number= int(input("Enter the number you want the table for: "))
    for i in range (1,11):
        print(Number, "x", i, "=", Number*i)
    
MultiplicationTable()

