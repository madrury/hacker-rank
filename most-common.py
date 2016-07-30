from sys import stdin
from collections import Counter

counts = Counter(stdin.readline().strip())
most_common = counts.most_common(3)
# If we have ties, we may have gotten arbitrary elements.
most_common_counts = set([y for x, y in most_common])

most_common = [(letter, counts[letter]) for letter in counts
                                       if counts[letter] in most_common_counts]

# Ok, now we need to make sure that ties are sorted lexographically!
most_common = sorted(most_common, key=lambda x: (-x[1], x[0]))[:3]

for letter, count in most_common:
    print(' '.join([letter, str(count)]))
