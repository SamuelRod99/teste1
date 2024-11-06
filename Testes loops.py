'''line = '*'
max_length = 10

while len(line) < max_length:
    print(line)
    line += "*"
    
while len(line) > 0:
    print(line)
    if line == '***':
        print('Magic number 3 reached! Stopping execution..')
        break
    line = line[:-1]'''

i = 1
result = 1

while i < 20:
    i += 1
    if i % 2 == 0:
        print('Skipping {}'.format(i))
        continue
    print('Multiplying with {}'.format(i))
    result = result * 4
    
print('i:', i)
print('result:', result)