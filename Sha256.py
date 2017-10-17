import hashlib

import Crypto.Hash._RIPEMD160


class Encoder(object):
    def __init__(self, inputstr):
        self.inputstr = inputstr

    def encode(self):
        return hashlib.sha256(self.inputstr).hexdigest()


encoder = Encoder(inputstr= 'sha256')
encoder.encode()
if __name__ == '__main__':
    decode = _RIPEMD160
decode.up


class Decoder(Encoder):

    def decode1(self):
        return _RIPEMD160

enc = Decoder()
print enc.decode1()





