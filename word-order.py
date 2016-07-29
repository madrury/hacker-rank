from collections import OrderedDict
import sys


word_count = OrderedDict()

_ = sys.stdin.readline()
for line in sys.stdin:
    word = line.strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(len(word_count))
print(' '.join(str(word_count[key]) for key in word_count))
