
print('A test line')
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
	
	
