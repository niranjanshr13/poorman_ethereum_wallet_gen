#!/usr/bin/env python2
from ethereum import utils
import subprocess
import time
import os
import glob


def ethereumGen():
    p = subprocess.Popen("openssl ecparam -name secp256k1 -genkey -noout | openssl ec -text -noout 2> /dev/null | grep priv -A 3 | tail -n +2 | tr -d '\n[:space:]:' | sed 's/^00//'", shell=True, stdout=subprocess.PIPE)
    out, _ = p.communicate()
    privateKey = out.decode('utf-8').replace('\n','')
    raw_address = utils.privtoaddr(privateKey)
    publicKey = utils.checksum_encode(raw_address)
    return privateKey, publicKey


if __name__ == '__main__':
    qrprivate,qrpublic = ethereumGen()
    subprocess.Popen(['qrencode', '-s', '10', '-o', 'publicKey.png', qrpublic])
    subprocess.Popen(['qrencode', '-s', '10', '-o', 'privateKey.png', qrprivate])
    subprocess.Popen(['convert', 'privateKey.png', 'publicKey.png', '+append', '1.png'])
    time.sleep(5)
    qrprivate,qrpublic = ethereumGen()
    subprocess.Popen(['qrencode', '-s', '10', '-o', 'publicKey2.png', qrpublic])
    subprocess.Popen(['qrencode', '-s', '10', '-o', 'privateKey2.png', qrprivate])
    subprocess.Popen(['convert', 'privateKey2.png', 'publicKey2.png', '+append', '2.png'])
    time.sleep(5)
    subprocess.Popen(['convert', '1.png', '2.png', '-append', '3.jpg'])
    time.sleep(5)
    for xx in glob.glob("*.png"):
        os.remove(xx)
