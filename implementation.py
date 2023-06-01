import secplus


code = "0010000001001011010001010000100110010001"
code2 = "0001100010111001101010000100000111001001"

#print(list(code)[:2])


codeList = [int(x) for x in list(code)]
codeList2 = [int(y) for y in list(code2)]

decoded = secplus.decode_v2(codeList+codeList2)
print(decoded)

nextVal = secplus.encode_v2(decoded[0]+1, decoded[1])
print(nextVal)
print(''.join(str(e) for e in nextVal))
#Sanity Check
decodedNextVal = secplus.decode_v2(nextVal)
print(decodedNextVal)
