from sys import stdin
from collections import deque


def iter_test_cases():
    n_tests = int(stdin.readline().strip())
    for _ in range(n_tests):
        _ = stdin.readline()  # Number of elements in array, don't need
        yield deque(int(x) for x in stdin.readline().strip().split(' '))

def can_do_it(test_case):
    largest = pop_largest(test_case)
    while(test_case):
        on_top = largest
        largest = pop_largest(test_case)
        if largest > on_top:
            return False
    return True

def pop_largest(test_case):
    front, back = test_case[0], test_case[-1]
    if front >= back:
        return test_case.popleft()
    else:
        return test_case.pop()


if __name__ == '__main__':
    for case in iter_test_cases():
        if can_do_it(case):
            print("Yes")
        else:
            print("No")
