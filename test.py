<<<<<<< HEAD
# This is a test file
=======
print('A test line')
>>>>>>> ee6dec8dc7b47c86fa9f8cd9ca387e7127387647
print('Hello, world!')
a=1
print('a= ',a)


def my_function(fname):
	file = open('email_address.txt', 'r')
	Lines = file.readlines()
  
	count = 0
	for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line))
	
	
