from sys import stdin
import re

starts_with = re.compile(r"^[456].*")
is_digits = re.compile(r"^\d{16}$")
is_seperated_digits = re.compile(r"^\d{4}-\d{4}-\d{4}-\d{4}$")
other_sep = re.compile(r"[ ,_]")
repeated_digits = re.compile(r"0000|1111|2222|3333|4444|5555|6666|7777|8888|9999")

def gen_input():
    _ = stdin.readline()
    for line in stdin:
        yield line.strip()

def strip_hyphens(cc):
    return cc.replace('-', '')

def is_valid_cc(cc):
    if is_seperated_digits.search(cc):
        cc = strip_hyphens(cc)
    return (
        starts_with.search(cc)
        and is_digits.search(cc)
        and not other_sep.search(cc)
        and not repeated_digits.search(cc)
    )
            
if __name__ == '__main__':
    for cc in gen_input():
        valid = is_valid_cc(cc)
        if valid:
            print('Valid')
        else:
            print('Invalid')
