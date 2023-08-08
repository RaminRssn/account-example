from cryptography.fernet import Fernet
#  =============================== Encrypt values using cryptography Module from Python standard library ========================== #
'''
                                            VAL = encryption(VALUE)
                                            
                                            ENCRYPTED_VALUE = VAL.Encrypt()
                                            DECRYPTED_VALUE = encryption(ENCRYPTED_VALUE).Decrypt()
'''
#  ================================================================================================================================ #



#===========================================================#
celid = b'fpOT6P8EFz35--6ohVcHRppNOz07F4R9792c324neE8='#====#
#===========================================================#
class encryption:
    def __init__(self, value):
        self.value = value
        self.celid = celid
    def Encrypt(self):
        cipher = Fernet(self.celid)
        encrypted_value = cipher.encrypt(self.value.encode())
        return encrypted_value
    def Decrypt(self):
        cipher = Fernet(self.celid)
        decrypted_value = cipher.decrypt(self.value).decode()
        return decrypted_value

#  ================================================================  #
'''
A = encryption('ramin')
print(A.Encrypt())

val = A.Encrypt()
B = encryption(val)

print(B.Decrypt())
'''
