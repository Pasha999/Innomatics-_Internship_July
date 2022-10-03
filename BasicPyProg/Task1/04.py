# The included code stub will read an integer,n , from STDIN.
# Without using any string methods, try to print the following:
# 1,2,3,4,..n
# Note that "..." represents the consecutive values in between.

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i+1, end="")  