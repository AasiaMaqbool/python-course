my_file=open('D:/test.txt')

print(my_file)
print(my_file.read())
my_file.seek(0)
print(my_file.readlines())
my_file.close()