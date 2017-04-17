import math
import binascii
import sys

kunci='irzal123'
kunci1=int(binascii.hexlify(kunci[:4]),16)   #diambil 4 huruf dikiri
kunci2=int(binascii.hexlify(kunci[4:8]),16)  #diambil 4 huruf dikanan

def encrypt(pesan):
    hexmessage=int(binascii.hexlify(pesan),16) #merubah asci ke biner karena string hnya bsa asci
    hasil=hexmessage^kunci1  #di xor jika sama 0 jika beda 1
    hasil=hasil+kunci2      #
    hasil=hasil%pow(2,32)
    return binascii.unhexlify('%x'%hasil)#dikembalikan ke asci
#rumus encrypt C=(p+k1)^k0

def decrypt(encrypted):
    decrypted=int(binascii.hexlify(encrypted),16)
    decrypted-=kunci2
    decrypted%=pow(2,32)
    decrypted=decrypted^kunci1
    return binascii.unhexlify('%x' %decrypted)
#rumus decrypt M=(C-k1%32)+k0
def konvert32bit(pesan,kategori):
    counter=0
    hasil=''
    while counter<len(pesan):
        if(kategori=='encryptnya'):
            hasil+=encrypt(pesan[counter:counter+4])
            counter+=4
        elif(kategori=='decryptnya'):
            hasil+=decrypt(pesan[counter:counter+4])
            counter+=4
    return hasil

p=raw_input('Masukan kata : ')
encrypted=konvert32bit(p,'encryptnya')
print 'Encrypted : ' + encrypted
print 'Decrypted : ' + konvert32bit(encrypted,'decryptnya')
