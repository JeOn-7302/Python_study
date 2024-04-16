#이진수
string = '1 0 0 1 0 1'

binary = string[::2]
num = int(binary, 2)

print(f'Number found: {num}')