# code for printing star pattern
def pyramid(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
if __name__ == "__main__":
    n = 10
    pyramid(n)
