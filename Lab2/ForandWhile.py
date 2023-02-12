# Can you use for loop inside a while loop
counter = 0
while counter < 5:
    for i in range(2):
        print("Inside for loop:", i)
    print("Inside while loop:", counter)
    counter += 1