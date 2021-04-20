res = ord('M')
bi = bin(res)
print(type(bi))

def binToDec(str):
    res = 0
    cnt = 5
    for i in str:
        if i == 0:
            cnt -= 1
        else:
            res += int(i)*(2**cnt)
            cnt -= 1
    return res

def base64(str):
    #str = 'ABCDEFG'
    sum = ''
    tmp = ''
    for i in str:
        tmp = bin(ord(i)).lstrip('0b')#返回的是去除0b的字符串
        if len(tmp) < 8:
            leng = 8-len(tmp)
            print('Line:54 leng =', leng)
            tmp = '0'*leng + tmp
            print('Line 56 sum =', sum)
        sum += tmp
    res = ''
    #return sum 现在的sum是加了0的，然后每隔6个分开
    print('Line 69 sum =', sum)
    for i in range(0,len(sum),6):
        res += chr(binToDec(sum[i:i+6]))
        print('chr====',binToDec(sum[i:i + 6]))
    return res
print('bin',binToDec('00111111'))

tst = base64('Man')
print(tst)
