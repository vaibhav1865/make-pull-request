#Function to generate and print all the binary numbers from 1 to n, given n, using the inbuilt bin() function.
def to_Binary(n):
	for i in range(1,n+1):
		print(bin(i)[2:])
		
# Driver program to test the above function 
n=input("Enter Value of n")
to_Binary(n)
