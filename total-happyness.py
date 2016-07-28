import sys

def calculate_happyness(my_list, happy_set, sad_set):
    # Could do one iteration, but probably better to do everything in C?
    return (
        sum(x in happy_set for x in my_list)
        - sum(x in sad_set for x in my_list)
    )

def read_int_array_from_line():
    return [int(x) for x in sys.stdin.readline().strip().split(' ')]

def read_int_set_from_line():
    return {int(x) for x in sys.stdin.readline().strip().split(' ')}

def parse_input():
    n, m = read_int_array_from_line()   
    my_array = read_int_array_from_line() 
    happy_set = read_int_set_from_line()
    sad_set = read_int_set_from_line()
    return my_array, happy_set, sad_set

if __name__ == '__main__':
    my_list, happy_set, sad_set = parse_input()
    total_happyness = calculate_happyness(my_list, happy_set, sad_set)
    print(str(total_happyness))

