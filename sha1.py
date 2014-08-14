#!/usr/local/bin/python

#### Description: This script generates a SHA-1 hash of an input value, 
#### which below is represented by "idfa". 

import hashlib

idfa="sampleidfa"

def get_sha1_hex(idfa):
    my_sh1 = hashlib.sha1()
    my_sh1.update(idfa)
    idfa_local_sh1 = my_sh1.hexdigest()
    return idfa_local_sh1

idfa_local_sh1 = get_sha1_hex(idfa)
print idfa_local_sh1

