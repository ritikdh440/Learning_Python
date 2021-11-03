def reverse(n):
    # number of spaces
    k = 2*n - 2
    # outer loop to handle number of rows
    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

n = 10
reverse(n)
