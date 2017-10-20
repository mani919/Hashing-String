import hashlib
import Crypto.Hash._RIPEMD160
from Crypto.Hash._RIPEMD160 import hashlib

class Encoder(object):
    def __init__(self, inputstr):
        self.inputstr = inputstr

    def encode(self):
        return hashlib.sha256(self.inputstr).hexdigest()

    def __init__(self, data=None):
        HashAlgo.__init__(self, hashFactory, data)


encoder = Encoder(inputstr= 'sha256')
inph = encoder.encode()
print inph















