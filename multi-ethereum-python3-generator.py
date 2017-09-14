#!/usr/bin/env python3
from ethereum import utils
import multiprocessing
import subprocess
import time

t = time.time()
outputNumber = 1000

def ethereumGen(_):
    try:
        p = subprocess.Popen("openssl ecparam -name secp256k1 -genkey -noout | openssl ec -text -noout 2> /dev/null | grep priv -A 3 | tail -n +2 | tr -d '\n[:space:]:' | sed 's/^00//'", shell=True, stdout=subprocess.PIPE)
        out, _ = p.communicate()
        privateKey = out.decode('utf-8').replace('\n','')
        raw_address = utils.privtoaddr(privateKey)
        publicKey = utils.checksum_encode(raw_address)
        return privateKey, publicKey
    except:
        pass

if __name__ == '__main__':
    ranger = range(outputNumber)
    P = multiprocessing.Pool(20)
    p = P.map(ethereumGen, ranger)
    f = open('file','w')
    for x in range(len(p)):
        try:
            f.write(p[x][0] + ',' + p[x][1] + '\n')
        except:
            pass
    f.close()
    tt = time.time()
    resultTime = tt - t
    print('time taken: ' + str(resultTime))
    print(str(outputNumber / resultTime) + '/sec') 
