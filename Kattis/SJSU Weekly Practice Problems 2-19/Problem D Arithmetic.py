import math
from random import randint
# octal = input().rstrip()
octalToBinary = ['000', '001', '010', '011','100','101','110' ,'111']
binary = []


octal = []
for i in range(200000):
    octal.append(str(randint(0,7)))
octal = ''.join(octal)
print(octal)

for ch in octal:
    binary.append(octalToBinary[int(ch)])
binary = ''.join(binary)


while len(binary) % 4 != 0:
    binary = '0' + binary

ans = []
encodedBinary = {'0000' : '0','0001': '1','0010' : '2' ,'0011': '3','0100': '4','0101': '5','0110': '6','0111': '7','1000' :'8','1001': '9','1010':'A','1011': 'B','1100':'C','1101':'D','1110':'E','1111':'F'}
for i in range(0,len(binary), 4):
    ans.append(encodedBinary[binary[i:i+4]])
print(''.join(ans).lstrip('0'))