#Write a python program to create a data file student.txt and append the message “Now we are
#AI students”
f=open('student.txt', 'a')
f.write("Now We Are AI Students!!!\n")
f.close()
f=open('student.txt', 'r')
print(f.read())
