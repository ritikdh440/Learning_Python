
def triangle(n):
	# spaces
	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
if __name__ == "main" :				
	n = int(input("Enter the value of n : "))
	triangle(n)
