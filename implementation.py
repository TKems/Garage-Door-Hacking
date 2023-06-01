# Written by Trevor Kems <trevorkems@gmail.com>
# Licensed under GPLv3
# Part of presentations at Bsides Iowa 2022 and SecDSM 6/2023

# THIS CODE IS PROVIDED AS-IS WITH NO WARRANTY.

import secplus

# Each packet is ~40 bits. See the secplus python file for a breakdown of the protocol
# https://github.com/argilo/secplus
code = "0010000001001011010001010000100110010001"
code2 = "0001100010111001101010000100000111001001"

#print(list(code)[:2])

codeList = [int(x) for x in list(code)]
codeList2 = [int(y) for y in list(code2)]

decoded = secplus.decode_v2(codeList+codeList2)
print("Decoded value: \n")
print(decoded)

print("Generating next value: \n")
nextVal = secplus.encode_v2(decoded[0]+1, decoded[1])
print("Raw binary output for next value: \n")
print(nextVal)
#print(''.join(str(e) for e in nextVal))
#Sanity Check
decodedNextVal = secplus.decode_v2(nextVal)
print("Sanity check code the next value: \n")
print(decodedNextVal)
