import hashlib

class Utils():

    @classmethod
    def txt2Sha3(self,text=''):
        return hashlib.sha3_256(text.encode('utf-8')).hexdigest()        
