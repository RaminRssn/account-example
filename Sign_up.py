from Password_checker import passchecker
import datetime
from encryption_controller import encryption
from Sq import SQL

#  ===========================   SIGN-UP Controller  ========================== #
"""
S_U_MESSAGE = []
USER_NAME = input('Enter your Username : ')
PASSWORD = input('Enter your Password :')
NAME = input('Enter your full name :')
while True:  
    ID_NUMBER = input("Enter ID-Number : ")
    PHONE = input("Enter Phone number : ")
    if ID_NUMBER.isnumeric() and PHONE.isnumeric(): break
    print('Failure : ID or Phone value error..\nPlease re-Enter the values correctly..')

SU = Signup(USER_NAME, PASSWORD, NAME, ID_NUMBER, PHONE)
SU.su_user_check()
S_U_MESSAGE.append('Username is already exists; try another username..') if SU.USER_CHK_R == False else S_U_MESSAGE.append('Username is accepted..')
SU.su_pass_check()
[S_U_MESSAGE.append(i) for i in SU.PSWCHK.reason if SU.PSWCHK.result == 'Not OK']

for i in S_U_MESSAGE:
    print(i)

if SU.USER_CHK_R == True and SU.PSWCHK.result == 'OK': SU.register()
"""
#  ============================================================================ #

class Signup:
    def __init__(self, USER_NAME, PASS, NAME = None, ID_NUMBER = None, PHONE = None, DATE = None):

        self.USER_NAME = USER_NAME
        self.PASS = PASS
        self.NAME = NAME
        self.ID_NUMBER = ID_NUMBER
        self.PHONE = PHONE
        self.DATE = DATE
        self.USER_CHK_R = False
        self.PSWCHK = None
        self.ENCRYPTED_PASS = None
        self.ENCRYPTED_ID_NUMBER = None
        self.ENCRYPTED_PHONE = None
        
    def su_user_check(self):
        """ Username checking in the Database.
        """
        USER_VAL = SQL(self.USER_NAME)
        USER_VAL.sql_connection()
        next(USER_VAL.__iter__())
        if USER_VAL.COND == 0: self.USER_CHK_R = True

    def su_pass_check(self):
        """ SignUp password checker
        """        
        self.PSWCHK = passchecker(self.PASS)
        self.PSWCHK.check()
        
    def register(self):
        """ENCRYPT AND REGISTER SOME NEW VALUES
        """
        SU_ENI = encryption(self.PASS)  
        SU_ENII = encryption(self.ID_NUMBER)
        SU_ENIII = encryption(self.PHONE)
        
        self.ENCRYPTED_PASS = SU_ENI.Encrypt()
        self.ENCRYPTED_ID_NUMBER = SU_ENII.Encrypt()
        self.ENCRYPTED_PHONE = SU_ENIII.Encrypt()
        
        entities = (self.USER_NAME, self.ENCRYPTED_PASS, datetime.datetime.now(), self.NAME,
                    '', '', '', '', 0, self.ENCRYPTED_ID_NUMBER, self.ENCRYPTED_PHONE)
        REGISTER = SQL(entities)
        REGISTER.Exec_values()

#  =========================================================================================  #
