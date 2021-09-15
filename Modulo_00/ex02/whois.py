import sys

phrase = sys.argv
if (len(phrase) > 2):
	print("ERROR")
elif (len(phrase) == 1) :
	exit
elif(phrase[1].isnumeric()) :
	num = int(phrase[1])
	if (num == 0):
		print("I'm Zero")
	elif (num % 2 ):
		print("I'm Odd")
	else:
		print("I'm Even")
else:
	print("ERROR")



