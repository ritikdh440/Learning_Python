
def numpat(n):

	num = 1
	for i in range(0, n):
		num = 1
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print("\r")

if __name__ =="__main__":
  n = int(inpit("Enter the value for n : "))
  numpat(n)
