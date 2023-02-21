import hashlib
from datetime import datetime

class Utils():

    @classmethod
    def txt2Sha3(self,text=''):
        return hashlib.sha3_256(text.encode('utf-8')).hexdigest()        

    @classmethod
    def getAge(self,birth=''):
        if birth=="":
            return ""
        fecha_nacimiento = datetime.strptime(birth, "%d/%m/%Y")
        hoy = datetime.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad