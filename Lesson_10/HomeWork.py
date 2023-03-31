

with open('input.txt') as f:
    lines = [line.strip('\n').split('a', 1)[-1] for line in f.readlines()]

output = [line.capitalize() for line in lines if line != '']
print(output)