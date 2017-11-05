import hashlib
import nacl.utils
import nacl.secret



class Encoder(object):
    def __init__(self, inputstr):
        self.inputstr = inputstr

    def encode(self):
        return hashlib.sha256(self.inputstr).hexdigest()


encoder = Encoder(inputstr= 'sha256')

cipher = encoder.encode()
print(cipher)
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
box = nacl.secret.SecretBox(key)
print(box)
encrypt = box.encrypt(cipher)
print(encrypt)
decrypt = box.decrypt(encrypt)
print(decrypt)























