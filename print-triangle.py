import sys

def read_input():
    return int(sys.stdin.readline().strip())

def print_triange(n):
    for i in range(1, n):
        print (i * sum(10**k for k in range(i)))

if __name__ == '__main__':
    n = read_input()
    print_triange(n)
