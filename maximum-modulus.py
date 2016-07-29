import sys
import itertools

def parse_input():
    k, m = [int(n) for n in sys.stdin.readline().strip().split(' ')]
    lists = []
    for i in range(k):
        lists.append([int(n) for n in sys.stdin.readline().strip().split(' ')][1:])
    return k, m, lists

def sum_mod(xs, mod):
    s = 0
    for n in xs:
        s += (n*n) % mod
    return s % mod

def maximize_modular_sum(lists, mod):
    M = 0
    for xs in itertools.product(*lists):
        M = max(M, sum_mod(xs, mod))
        print(M)
    return M


if __name__ == '__main__':
    _, m, lists = parse_input()
    print(lists)
    M = maximize_modular_sum(lists, m)
    print(M)
