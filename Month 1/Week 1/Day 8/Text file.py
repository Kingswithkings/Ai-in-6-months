# Write and read files
# Write
text = 'Hello Kings!\nThis is Day 8 file I\O practice.'
with open('hello.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print('Wrote hello.txt')

# Read it back
with open('hello.text', 'r', encoding='utf-8') as f:
    content = f.read()
print('\nContent of hello.txt\n', content)
