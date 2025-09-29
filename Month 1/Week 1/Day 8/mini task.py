# Create a sample log-like file
lines = ['error:disk full', 'info:started', 'error:timeout', 'info:done', 'error:disk full']
with open('sample.log', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))


# Count error occurences
from collections import Counter
with open('sample.log', 'r', encoding='utf-8') as f:
    cnt = Counter([ln.split(':')[0] for ln in f.read().splitlines()])
print('Counts:', cnt)