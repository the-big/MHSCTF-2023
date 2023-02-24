from base64 import b64encode

extendedb64a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\\='"

enc = "WU]Wipuk\cYAvtEXHsRlP_YlPs[UMtVmkcOjupFCVGU"

first_part=bytes("valentine{","utf-8")

a = b64encode(first_part)

a = list(map(ord, list(str(a))))

b=[]

#(enc[i]-65) - a[i] % 58 = b[i] % 58

for i in range(len(a)):
    b.append(((ord(enc[i])-65) - a[i])%58)

for i in b:
    if(chr(i) not in extendedb64a):
        if(chr(i+58) not in extendedb64a):
            if(chr(i+116) not in extendedb64a):
                print('&')
            else:
                print(chr(i+116),end='')
        else:
            print(chr(i+58),end='')
    else:
        print(chr(i),end='')

#after decoding + experiments
#run 1
extendedb64a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\\='_"
first_part="valentine{"
last_part = "_w1nky_f4ce}"

def encode(valentine):
    valentine = bytes(valentine,"utf-8")
    a = b64encode(valentine)
    b = b64encode(valentine[::-1])
    a = list(map(ord, list(str(a))))
    b = list(map(ord, list(str(b))))
    txt=''
    for j in range(len(a)):
      txt += (chr((a[j] + b[j]) % 58 + 65))
    return txt
'''
for i1 in extendedb64a:
    for i2 in extendedb64a:
        for i3 in extendedb64a:
            tx = encode(first_part+i1+i2+'aaaa'+i3+last_part)
            if("WU]Wipuk\cYAvtEXH" in tx):
                print(tx, i1, i2, i3)'''
#run 2
first_part="valentine{t"
last_part = "_w1nky_f4ce}"
for i1 in extendedb64a:
    for i2 in extendedb64a:
        for i3 in extendedb64a:
            tx = encode(first_part+i1+i2+'aaa'+i3+last_part)
            if("WU]Wipuk\cYAvtEXHsR" in tx):
                print(tx, i1, i2, i3)

assert encode('valentine{t3xt_me_w1nky_f4ce}') == enc
