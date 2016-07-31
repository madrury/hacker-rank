from sys import stdin

def read_integer_line():
    return list(map(int, stdin.readline().strip().split(' ')))

def read_input():
    n, _ = read_integer_line()
    table = []
    for _ in range(n):
        row = read_integer_line()
        table.append(row)
    k = read_integer_line()[0]
    return table, k

def sort_table(table, k):
    return sorted(table, key=lambda row: row[k])

def print_table(table):
    for row in table:
        print(' '.join([str(x) for x in row]))

if __name__ == '__main__':
    table, k = read_input()
    table = sort_table(table, k)
    print_table(table)
    
