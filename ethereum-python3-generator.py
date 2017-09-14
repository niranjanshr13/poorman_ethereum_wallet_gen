#!/usr/bin/env python3
from ethereum import utils
import multiprocessing
import subprocess


def ethereumGen():
    p = subprocess.Popen("openssl ecparam -name secp256k1 -genkey -noout | openssl ec -text -noout 2> /dev/null | grep priv -A 3 | tail -n +2 | tr -d '\n[:space:]:' | sed 's/^00//'", shell=True, stdout=subprocess.PIPE)
    out, _ = p.communicate()
    privateKey = out.decode('utf-8').replace('\n','')
    raw_address = utils.privtoaddr(privateKey)
    publicKey = utils.checksum_encode(raw_address)
    return privateKey, publicKey


if __name__ == '__main__':
    for _ in range(0,1000):
        try:
            privateKey, publicKey = ethereumGen()
            fPrivateKey = open('privateKey.txt','a+')
            fPrivateKey.write(privateKey + '\n')
            fPrivateKey.close()
            fPublicKey = open('publicKey.txt','a+')
            fPublicKey.write(publicKey + '\n')
            fPublicKey.close()
        except:
            pass
